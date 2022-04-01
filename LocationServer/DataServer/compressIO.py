import lz4.block
import pickle
import json

def compress_block(data):
    compressed = lz4.block.compress(data.encode('utf-8'), 'fast')
    return compressed


def decompress_data(compressed):
    data = lz4.block.decompress(compressed)
    return data


def write_block(block_name, data):
    fl = open('../block/'+block_name, 'wb')
    pickle.dump(data, fl)
    fl.close()


def read_block(block_name):
    fl = open('../block/'+block_name, 'rb')
    compressed = pickle.load(fl)
    fl.close()
    return compressed

def fetch_data(block_name,key):
    compressed = read_block(block_name)
    data = decompress_data(compressed)
    data = json.loads(data)
    required_data = data[key]
    return required_data

def dump_data(block_name,key,value):
    compressed = read_block(block_name)
    data = decompress_data(compressed)
    data = json.loads(data)
    data[key] = value
    data = json.dumps(data)
    compressed = compress_block(data)
    write_block(block_name,compressed)
