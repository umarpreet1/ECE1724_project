import grpc
import protos.location_server_pb2_grpc as ls_grpc
import protos.location_server_pb2 as ls

write_case = {'bbt.sheldon':'Jim Parsons','friends.chandler':'Mathew Parry','office.michel':'Steve Carel'}

read_case = {'friends.chandler':'Mathew Parry'}

host = 'localhost'
server_port = 50052


channel = grpc.insecure_channel(
            '{}:{}'.format(host, server_port))

stub = ls_grpc.location_serverStub(channel)

for each in write_case.keys():
    value = write_case[each]
    message = ls.write_request(key = each, value = value, prefix = 'com')
    print(message)
    stub.write(message)

message = ls.read_request(key='friends.chandler')
response = stub.read(message)
print(message)
print(response)