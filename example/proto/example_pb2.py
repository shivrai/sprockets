# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: example.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='example.proto',
  package='bar',
  syntax='proto2',
  serialized_pb=_b('\n\rexample.proto\x12\x03\x62\x61r\"4\n\tSimpleMsg\x12\x0b\n\x03\x66oo\x18\x01 \x02(\t\x12\x0c\n\x04\x66izz\x18\x02 \x01(\x05\x12\x0c\n\x04\x62uzz\x18\x03 \x03(\x08\x42\x02H\x03')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_SIMPLEMSG = _descriptor.Descriptor(
  name='SimpleMsg',
  full_name='bar.SimpleMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='foo', full_name='bar.SimpleMsg.foo', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fizz', full_name='bar.SimpleMsg.fizz', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='buzz', full_name='bar.SimpleMsg.buzz', index=2,
      number=3, type=8, cpp_type=7, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=22,
  serialized_end=74,
)

DESCRIPTOR.message_types_by_name['SimpleMsg'] = _SIMPLEMSG

SimpleMsg = _reflection.GeneratedProtocolMessageType('SimpleMsg', (_message.Message,), dict(
  DESCRIPTOR = _SIMPLEMSG,
  __module__ = 'example_pb2'
  # @@protoc_insertion_point(class_scope:bar.SimpleMsg)
  ))
_sym_db.RegisterMessage(SimpleMsg)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('H\003'))
# @@protoc_insertion_point(module_scope)
