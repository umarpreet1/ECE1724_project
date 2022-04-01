# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/location_server.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1cprotos/location_server.proto\x12\x0elocationserver\"\x1b\n\x0cread_request\x12\x0b\n\x03key\x18\x01 \x02(\t\";\n\rwrite_request\x12\x0b\n\x03key\x18\x01 \x02(\t\x12\r\n\x05value\x18\x02 \x02(\t\x12\x0e\n\x06prefix\x18\x03 \x02(\t\"\x1e\n\rread_response\x12\r\n\x05value\x18\x01 \x02(\t\" \n\x0ewrite_response\x12\x0e\n\x06status\x18\x01 \x02(\t2\xe7\x01\n\x0flocation_server\x12\x43\n\x04read\x12\x1c.locationserver.read_request\x1a\x1d.locationserver.read_response\x12\x46\n\x05write\x12\x1d.locationserver.write_request\x1a\x1e.locationserver.write_response\x12G\n\x06update\x12\x1d.locationserver.write_request\x1a\x1e.locationserver.write_response')



_READ_REQUEST = DESCRIPTOR.message_types_by_name['read_request']
_WRITE_REQUEST = DESCRIPTOR.message_types_by_name['write_request']
_READ_RESPONSE = DESCRIPTOR.message_types_by_name['read_response']
_WRITE_RESPONSE = DESCRIPTOR.message_types_by_name['write_response']
read_request = _reflection.GeneratedProtocolMessageType('read_request', (_message.Message,), {
  'DESCRIPTOR' : _READ_REQUEST,
  '__module__' : 'protos.location_server_pb2'
  # @@protoc_insertion_point(class_scope:locationserver.read_request)
  })
_sym_db.RegisterMessage(read_request)

write_request = _reflection.GeneratedProtocolMessageType('write_request', (_message.Message,), {
  'DESCRIPTOR' : _WRITE_REQUEST,
  '__module__' : 'protos.location_server_pb2'
  # @@protoc_insertion_point(class_scope:locationserver.write_request)
  })
_sym_db.RegisterMessage(write_request)

read_response = _reflection.GeneratedProtocolMessageType('read_response', (_message.Message,), {
  'DESCRIPTOR' : _READ_RESPONSE,
  '__module__' : 'protos.location_server_pb2'
  # @@protoc_insertion_point(class_scope:locationserver.read_response)
  })
_sym_db.RegisterMessage(read_response)

write_response = _reflection.GeneratedProtocolMessageType('write_response', (_message.Message,), {
  'DESCRIPTOR' : _WRITE_RESPONSE,
  '__module__' : 'protos.location_server_pb2'
  # @@protoc_insertion_point(class_scope:locationserver.write_response)
  })
_sym_db.RegisterMessage(write_response)

_LOCATION_SERVER = DESCRIPTOR.services_by_name['location_server']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _READ_REQUEST._serialized_start=48
  _READ_REQUEST._serialized_end=75
  _WRITE_REQUEST._serialized_start=77
  _WRITE_REQUEST._serialized_end=136
  _READ_RESPONSE._serialized_start=138
  _READ_RESPONSE._serialized_end=168
  _WRITE_RESPONSE._serialized_start=170
  _WRITE_RESPONSE._serialized_end=202
  _LOCATION_SERVER._serialized_start=205
  _LOCATION_SERVER._serialized_end=436
# @@protoc_insertion_point(module_scope)