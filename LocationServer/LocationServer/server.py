from concurrent import futures
import grpc
import protos.location_server_pb2_grpc as ls_grpc
import protos.location_server_pb2 as ls
from LocationServer import dataServerManager as ds
from LocationServer.trie import BaseTrie

class location_server(ls_grpc.location_serverServicer):

    def __init__(self,dataServer_Manager,trie):
        self.dataServer_Manager = dataServer_Manager
        self.trie = trie

    def read(self, request, context):
        key = request.key
        id = self.trie.get_node(key)
        print("id",id)
        value = self.dataServer_Manager.read(id,key)

        response = ls.read_response(value=value)
        return response

    def write(self, request, context):
        key = request.key
        value = request.value
        self.dataServer_Manager.write(0,key,value)
        self.trie.add_node(key,0)
        response = ls.write_response(status='Done')
        return response


class Server:
    def __init__(self,id,port):
        print("Creating Location server with id : ", id, " port : ", port)
        self.id = id
        self.port = port
        self.dsManager = ds.DSManager()
        self.mytrie = BaseTrie()
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        ls_grpc.add_location_serverServicer_to_server(location_server(dataServer_Manager=self.dsManager, trie=self.mytrie),
                                                      self.server)
        self.server.add_insecure_port('[::]:'+str(port))
        print("Location server is created with id : ", id, " port : ", port)

    def connect_ds(self,dataservers_info):
        print("Connecting all available DataServers with LocationServer id : ", self.id, " port : ", self.port)
        for id in dataservers_info.keys():
            self.dsManager.add_dataServer(id,dataservers_info[id])
        print("Connected all available DataServers with LocationServer id : ", self.id, " port : ", self.port)

    def start(self):
        print("Starting Location server with id : ", self.id, " port : ", self.port)
        self.server.start()
        print("Location server started with id : ", self.id, " port : ", self.port)

    def stop(self):
        self.server.stop()


def serve():
    dsManager = ds.DSManager()
    dsManager.add_dataServer(0,'localhost',50051)
    mytrie = BaseTrie()
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    ls_grpc.add_location_serverServicer_to_server(location_server(dataServer_Manager=dsManager,trie=mytrie), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
