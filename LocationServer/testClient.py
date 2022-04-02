import grpc
import protos.location_server_pb2_grpc as ls_grpc
import protos.serve_data_pb2 as ds
import protos.serve_data_pb2_grpc as ds_grpc

write_case = {'bbt.sheldon':'Jim Parsons','friends.chandler':'Mathew Parry','office.michel':'Steve Carel'}

read_case = {'friends.chandler':'Mathew Parry'}

host = 'localhost'
server_port = 8034


channel = grpc.insecure_channel(
            '{}:{}'.format(host, server_port))

stub = ds_grpc.data_serverStub(channel)

for each in write_case.keys():
    value = write_case[each]
    message = ds.write_request(key = each, value = value)
    print(message)
    stub.write_data(message)

message = ds.read_request(key='friends.chandler')
response = stub.read(message)
print(message)
print(response)