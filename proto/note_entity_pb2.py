# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: note_entity.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='note_entity.proto',
  package='sync_pb',
  syntax='proto2',
  serialized_options=b'\n%org.chromium.components.sync.protocolH\003P\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x11note_entity.proto\x12\x07sync_pb\"\xc7\x01\n\nNoteEntity\x12\x12\n\nplain_text\x18\x01 \x01(\t\x12\x11\n\trich_text\x18\x02 \x01(\t\x12\x33\n\x0btarget_type\x18\x03 \x01(\x0e\x32\x1e.sync_pb.NoteEntity.TargetType\x12\x1c\n\x14\x63urrent_note_version\x18\x04 \x01(\x05\"?\n\nTargetType\x12\x1b\n\x17TARGET_TYPE_UNSPECIFIED\x10\x00\x12\x14\n\x10TARGET_TYPE_PAGE\x10\x01\x42+\n%org.chromium.components.sync.protocolH\x03P\x01'
)



_NOTEENTITY_TARGETTYPE = _descriptor.EnumDescriptor(
  name='TargetType',
  full_name='sync_pb.NoteEntity.TargetType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TARGET_TYPE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TARGET_TYPE_PAGE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=167,
  serialized_end=230,
)
_sym_db.RegisterEnumDescriptor(_NOTEENTITY_TARGETTYPE)


_NOTEENTITY = _descriptor.Descriptor(
  name='NoteEntity',
  full_name='sync_pb.NoteEntity',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='plain_text', full_name='sync_pb.NoteEntity.plain_text', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rich_text', full_name='sync_pb.NoteEntity.rich_text', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='target_type', full_name='sync_pb.NoteEntity.target_type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='current_note_version', full_name='sync_pb.NoteEntity.current_note_version', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _NOTEENTITY_TARGETTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=31,
  serialized_end=230,
)

_NOTEENTITY.fields_by_name['target_type'].enum_type = _NOTEENTITY_TARGETTYPE
_NOTEENTITY_TARGETTYPE.containing_type = _NOTEENTITY
DESCRIPTOR.message_types_by_name['NoteEntity'] = _NOTEENTITY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NoteEntity = _reflection.GeneratedProtocolMessageType('NoteEntity', (_message.Message,), {
  'DESCRIPTOR' : _NOTEENTITY,
  '__module__' : 'note_entity_pb2'
  # @@protoc_insertion_point(class_scope:sync_pb.NoteEntity)
  })
_sym_db.RegisterMessage(NoteEntity)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
