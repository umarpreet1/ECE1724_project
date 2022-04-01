from flask import Flask,request
from flask import render_template
from DataServer import server as dataserver
from LocationServer import server as locationserver
import random
import grpc
import protos.location_server_pb2 as ls
import protos.location_server_pb2_grpc as ls_grpc

app=Flask(__name__)

dataservers = []
dataservers_info = {}
locationservers = []
locationservers_info = {}

@app.route('/')
def main():
    return render_template("index.html",dataservers_info = dataservers_info,locationservers_info = locationservers_info)

@app.route('/new_ds',methods=['POST'])
def new_ds():
    id = request.form.get('id')
    port = request.form.get('port')
    ds = dataserver.Server(int(id),int(port))
    ds.start()
    dataservers_info[id] = port
    dataservers.append(ds)
    return  render_template("index.html",dataservers_info = dataservers_info,locationservers_info = locationservers_info)

@app.route('/new_ls',methods=['POST'])
def new_ls():
    id = request.form.get('id_ls')
    port = request.form.get('port_ls')
    ls = locationserver.Server(int(id),int(port))
    ls.connect_ds(dataservers_info)
    ls.start()
    locationservers_info[id]=port
    locationservers.append(ls)
    return render_template("index.html",dataservers_info = dataservers_info,locationservers_info = locationservers_info)


@app.route('/test_init')
def test_init():
    ds_ports = [50050,50051,50053]
    for i in range(len(ds_ports)):
        ds = dataserver.Server(i, ds_ports[i])
        ds.start()
        dataservers_info[i] = ds_ports[i]
        dataservers.append(ds)
    ls_ports = [40001,40002,40003]
    for i in range(len(ls_ports)):
        ls = locationserver.Server(i, ls_ports[i])
        ls.connect_ds(dataservers_info)
        ls.start()
        locationservers_info[i] = ls_ports[i]
        locationservers.append(ls)
    return render_template("index.html", dataservers_info=dataservers_info, locationservers_info=locationservers_info)

@app.route('/read_write',methods=['GET'])
def read_write():
    return render_template('read_write.html',val=None,success=False)

@app.route('/write',methods=['POST'])
def write():
    key = request.form.get('key')
    value = request.form.get('value')
    randomLS = random.randint(0,len(locationservers)-1)
    server_port =  locationservers_info[randomLS]
    host = 'localhost'

    channel = grpc.insecure_channel(
        '{}:{}'.format(host, server_port))

    stub = ls_grpc.location_serverStub(channel)
    message = ls.write_request(key=key, value=value, prefix='com')
    stub.write(message)
    return render_template('read_write.html',val=None,success=True)

@app.route('/read',methods=['POST'])
def read():
    return render_template('read_write.html', val="hello", success=False)