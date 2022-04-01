from concurrent import futures
import grpc
import os
import protos.serve_data_pb2_grpc as sd_grpc
import protos.serve_data_pb2 as sd
from DataServer.trie import BaseTrie
import time

class serve_data(sd_grpc.data_serverServicer):

    def __init__(self,id, mytrie):
        self.id = id
        self.mytrie = mytrie

    def read(self, request, context):
        key = request.key
        print("Read request received with key:", key)

        lock = self.mytrie.get_lock(key)
        while True:
            if lock.is_locked():
                continue
            else:
                print("Lock is in UNLOCKED state, key : ",key)
                lock.lock()
                file = open('data/data_'+str(self.id)+'/'+key+'.txt','r')
                value = file.readline()
                lock.unlock()
                print("Read and Lock is released, key : ",key)
                break
        response = sd.response_read(value = value)
        return response

    def write_data(self, request, context):
        key = request.key
        print("Write request received with key:", key)
        value = request.value
        print(value)
        lock = self.mytrie.get_lock(key)
        while True:
            if lock.is_locked():
                continue
            else:
                print("Lock is in UNLOCKED state, key : ", key)
                lock.lock()
                file = open('data/data_'+str(self.id)+'/'+key+'.txt','w')
                file.write(value)
                file.close()
                lock.unlock()
                print("Written and Lock is released, key : ", key)
                break
        response = sd.response(status = "SUCCESS")
        return response

    def update_data(self, request, context):
        key = request.key
        print("Update request received with key:", key)
        value = request.value
        file = open('data/data_'+str(self.id)+'/'+key+'.txt','w')
        file.write(value)
        file.close()
        response = sd.response(status = "SUCCESS")
        return response

class Server:
    def __init__(self,id,port):
        mytrie = BaseTrie()
        print("Creating Data server with id : ", id, " port : ", port)
        self.id = id
        if not 'data_'+str(id) in os.listdir('data'):
            os.mkdir('data/data_'+str(id))
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        sd_grpc.add_data_serverServicer_to_server(serve_data(id=id,mytrie = mytrie ), self.server)
        self.server.add_insecure_port('[::]:'+str(port))
        self.port = port
        print("Data server is created with id : ",id," port : ",port)

    def start(self):
        print("Starting Data server with id : ", self.id, " port : ", self.port)
        self.server.start()
        print("Data server started with id : ", self.id, " port : ", self.port)

    def stop(self):
        self.server.stop()


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    sd_grpc.add_data_serverServicer_to_server(serve_data(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()