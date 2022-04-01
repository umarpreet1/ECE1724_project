import grpc
import protos.serve_data_pb2_grpc as sd_grpc
import protos.serve_data_pb2 as sd

class DSConnection:

    def __init__(self,host,port):
        self.host = host
        self.port = port
        self.channel = grpc.insecure_channel(
            '{}:{}'.format(host, port))
        self.stub  = sd_grpc.data_serverStub(self.channel)

    def read(self,key):
        message = sd.read_request(key=key)
        response  = self.stub.read(message)
        print(response)
        return response.value

    def write(self,key,value):
        message = sd.write_request(key=key,value=value)
        response = self.stub.write_data(message)
        return response



class DSManager:

    def __init__(self):
        self.connections = {}

    def add_dataServer(self,id,port):
        print("Connecting DataServer with id : ",id," port : ",port)
        dataserver = DSConnection('localhost',port)
        self.connections[id] = dataserver
        print("Connected DataServer with id : ", id, " port : ", port)


    def read(self,id,key):
        value = self.connections[id].read(key)
        return value

    def write(self,id,key,value):
        self.connections[id].write(key,value)
