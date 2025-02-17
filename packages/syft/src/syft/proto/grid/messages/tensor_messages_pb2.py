# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/grid/messages/tensor_messages.proto
"""Generated protocol buffer code."""
# third party
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


# syft absolute
from syft.proto.core.common import (
    common_object_pb2 as proto_dot_core_dot_common_dot_common__object__pb2,
)
from syft.proto.core.io import address_pb2 as proto_dot_core_dot_io_dot_address__pb2

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n)proto/grid/messages/tensor_messages.proto\x12\x12syft.grid.messages\x1a%proto/core/common/common_object.proto\x1a\x1bproto/core/io/address.proto"\x9e\x01\n\x13\x43reateTensorMessage\x12%\n\x06msg_id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12&\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0b\x32\x15.syft.core.io.Address\x12\x0f\n\x07\x63ontent\x18\x03 \x01(\t\x12\'\n\x08reply_to\x18\x04 \x01(\x0b\x32\x15.syft.core.io.Address"\x8b\x01\n\x14\x43reateTensorResponse\x12%\n\x06msg_id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12\x13\n\x0bstatus_code\x18\x02 \x01(\x05\x12\x0f\n\x07\x63ontent\x18\x03 \x01(\t\x12&\n\x07\x61\x64\x64ress\x18\x04 \x01(\x0b\x32\x15.syft.core.io.Address"\x9b\x01\n\x10GetTensorMessage\x12%\n\x06msg_id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12&\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0b\x32\x15.syft.core.io.Address\x12\x0f\n\x07\x63ontent\x18\x03 \x01(\t\x12\'\n\x08reply_to\x18\x04 \x01(\x0b\x32\x15.syft.core.io.Address"\x88\x01\n\x11GetTensorResponse\x12%\n\x06msg_id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12\x13\n\x0bstatus_code\x18\x02 \x01(\x05\x12\x0f\n\x07\x63ontent\x18\x03 \x01(\t\x12&\n\x07\x61\x64\x64ress\x18\x04 \x01(\x0b\x32\x15.syft.core.io.Address"\x9c\x01\n\x11GetTensorsMessage\x12%\n\x06msg_id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12&\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0b\x32\x15.syft.core.io.Address\x12\x0f\n\x07\x63ontent\x18\x03 \x01(\t\x12\'\n\x08reply_to\x18\x04 \x01(\x0b\x32\x15.syft.core.io.Address"\x89\x01\n\x12GetTensorsResponse\x12%\n\x06msg_id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12\x13\n\x0bstatus_code\x18\x02 \x01(\x05\x12\x0f\n\x07\x63ontent\x18\x03 \x01(\t\x12&\n\x07\x61\x64\x64ress\x18\x04 \x01(\x0b\x32\x15.syft.core.io.Address"\x9e\x01\n\x13\x44\x65leteTensorMessage\x12%\n\x06msg_id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12&\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0b\x32\x15.syft.core.io.Address\x12\x0f\n\x07\x63ontent\x18\x03 \x01(\t\x12\'\n\x08reply_to\x18\x04 \x01(\x0b\x32\x15.syft.core.io.Address"\x8b\x01\n\x14\x44\x65leteTensorResponse\x12%\n\x06msg_id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12\x13\n\x0bstatus_code\x18\x02 \x01(\x05\x12\x0f\n\x07\x63ontent\x18\x03 \x01(\t\x12&\n\x07\x61\x64\x64ress\x18\x04 \x01(\x0b\x32\x15.syft.core.io.Address"\x9e\x01\n\x13UpdateTensorMessage\x12%\n\x06msg_id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12&\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0b\x32\x15.syft.core.io.Address\x12\x0f\n\x07\x63ontent\x18\x03 \x01(\t\x12\'\n\x08reply_to\x18\x04 \x01(\x0b\x32\x15.syft.core.io.Address"\x8b\x01\n\x14UpdateTensorResponse\x12%\n\x06msg_id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12\x13\n\x0bstatus_code\x18\x02 \x01(\x05\x12\x0f\n\x07\x63ontent\x18\x03 \x01(\t\x12&\n\x07\x61\x64\x64ress\x18\x04 \x01(\x0b\x32\x15.syft.core.io.Addressb\x06proto3'
)


_CREATETENSORMESSAGE = DESCRIPTOR.message_types_by_name["CreateTensorMessage"]
_CREATETENSORRESPONSE = DESCRIPTOR.message_types_by_name["CreateTensorResponse"]
_GETTENSORMESSAGE = DESCRIPTOR.message_types_by_name["GetTensorMessage"]
_GETTENSORRESPONSE = DESCRIPTOR.message_types_by_name["GetTensorResponse"]
_GETTENSORSMESSAGE = DESCRIPTOR.message_types_by_name["GetTensorsMessage"]
_GETTENSORSRESPONSE = DESCRIPTOR.message_types_by_name["GetTensorsResponse"]
_DELETETENSORMESSAGE = DESCRIPTOR.message_types_by_name["DeleteTensorMessage"]
_DELETETENSORRESPONSE = DESCRIPTOR.message_types_by_name["DeleteTensorResponse"]
_UPDATETENSORMESSAGE = DESCRIPTOR.message_types_by_name["UpdateTensorMessage"]
_UPDATETENSORRESPONSE = DESCRIPTOR.message_types_by_name["UpdateTensorResponse"]
CreateTensorMessage = _reflection.GeneratedProtocolMessageType(
    "CreateTensorMessage",
    (_message.Message,),
    {
        "DESCRIPTOR": _CREATETENSORMESSAGE,
        "__module__": "proto.grid.messages.tensor_messages_pb2"
        # @@protoc_insertion_point(class_scope:syft.grid.messages.CreateTensorMessage)
    },
)
_sym_db.RegisterMessage(CreateTensorMessage)

CreateTensorResponse = _reflection.GeneratedProtocolMessageType(
    "CreateTensorResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _CREATETENSORRESPONSE,
        "__module__": "proto.grid.messages.tensor_messages_pb2"
        # @@protoc_insertion_point(class_scope:syft.grid.messages.CreateTensorResponse)
    },
)
_sym_db.RegisterMessage(CreateTensorResponse)

GetTensorMessage = _reflection.GeneratedProtocolMessageType(
    "GetTensorMessage",
    (_message.Message,),
    {
        "DESCRIPTOR": _GETTENSORMESSAGE,
        "__module__": "proto.grid.messages.tensor_messages_pb2"
        # @@protoc_insertion_point(class_scope:syft.grid.messages.GetTensorMessage)
    },
)
_sym_db.RegisterMessage(GetTensorMessage)

GetTensorResponse = _reflection.GeneratedProtocolMessageType(
    "GetTensorResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _GETTENSORRESPONSE,
        "__module__": "proto.grid.messages.tensor_messages_pb2"
        # @@protoc_insertion_point(class_scope:syft.grid.messages.GetTensorResponse)
    },
)
_sym_db.RegisterMessage(GetTensorResponse)

GetTensorsMessage = _reflection.GeneratedProtocolMessageType(
    "GetTensorsMessage",
    (_message.Message,),
    {
        "DESCRIPTOR": _GETTENSORSMESSAGE,
        "__module__": "proto.grid.messages.tensor_messages_pb2"
        # @@protoc_insertion_point(class_scope:syft.grid.messages.GetTensorsMessage)
    },
)
_sym_db.RegisterMessage(GetTensorsMessage)

GetTensorsResponse = _reflection.GeneratedProtocolMessageType(
    "GetTensorsResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _GETTENSORSRESPONSE,
        "__module__": "proto.grid.messages.tensor_messages_pb2"
        # @@protoc_insertion_point(class_scope:syft.grid.messages.GetTensorsResponse)
    },
)
_sym_db.RegisterMessage(GetTensorsResponse)

DeleteTensorMessage = _reflection.GeneratedProtocolMessageType(
    "DeleteTensorMessage",
    (_message.Message,),
    {
        "DESCRIPTOR": _DELETETENSORMESSAGE,
        "__module__": "proto.grid.messages.tensor_messages_pb2"
        # @@protoc_insertion_point(class_scope:syft.grid.messages.DeleteTensorMessage)
    },
)
_sym_db.RegisterMessage(DeleteTensorMessage)

DeleteTensorResponse = _reflection.GeneratedProtocolMessageType(
    "DeleteTensorResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _DELETETENSORRESPONSE,
        "__module__": "proto.grid.messages.tensor_messages_pb2"
        # @@protoc_insertion_point(class_scope:syft.grid.messages.DeleteTensorResponse)
    },
)
_sym_db.RegisterMessage(DeleteTensorResponse)

UpdateTensorMessage = _reflection.GeneratedProtocolMessageType(
    "UpdateTensorMessage",
    (_message.Message,),
    {
        "DESCRIPTOR": _UPDATETENSORMESSAGE,
        "__module__": "proto.grid.messages.tensor_messages_pb2"
        # @@protoc_insertion_point(class_scope:syft.grid.messages.UpdateTensorMessage)
    },
)
_sym_db.RegisterMessage(UpdateTensorMessage)

UpdateTensorResponse = _reflection.GeneratedProtocolMessageType(
    "UpdateTensorResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _UPDATETENSORRESPONSE,
        "__module__": "proto.grid.messages.tensor_messages_pb2"
        # @@protoc_insertion_point(class_scope:syft.grid.messages.UpdateTensorResponse)
    },
)
_sym_db.RegisterMessage(UpdateTensorResponse)

if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _CREATETENSORMESSAGE._serialized_start = 134
    _CREATETENSORMESSAGE._serialized_end = 292
    _CREATETENSORRESPONSE._serialized_start = 295
    _CREATETENSORRESPONSE._serialized_end = 434
    _GETTENSORMESSAGE._serialized_start = 437
    _GETTENSORMESSAGE._serialized_end = 592
    _GETTENSORRESPONSE._serialized_start = 595
    _GETTENSORRESPONSE._serialized_end = 731
    _GETTENSORSMESSAGE._serialized_start = 734
    _GETTENSORSMESSAGE._serialized_end = 890
    _GETTENSORSRESPONSE._serialized_start = 893
    _GETTENSORSRESPONSE._serialized_end = 1030
    _DELETETENSORMESSAGE._serialized_start = 1033
    _DELETETENSORMESSAGE._serialized_end = 1191
    _DELETETENSORRESPONSE._serialized_start = 1194
    _DELETETENSORRESPONSE._serialized_end = 1333
    _UPDATETENSORMESSAGE._serialized_start = 1336
    _UPDATETENSORMESSAGE._serialized_end = 1494
    _UPDATETENSORRESPONSE._serialized_start = 1497
    _UPDATETENSORRESPONSE._serialized_end = 1636
# @@protoc_insertion_point(module_scope)
