# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/lib/python/collections/ordered_dict.proto
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

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n/proto/lib/python/collections/ordered_dict.proto\x12\x1bsyft.lib.python.collections\x1a%proto/core/common/common_object.proto"N\n\x0bOrderedDict\x12\x0c\n\x04keys\x18\x01 \x03(\x0c\x12\x0e\n\x06values\x18\x02 \x03(\x0c\x12!\n\x02id\x18\x03 \x01(\x0b\x32\x15.syft.core.common.UIDb\x06proto3'
)


_ORDEREDDICT = DESCRIPTOR.message_types_by_name["OrderedDict"]
OrderedDict = _reflection.GeneratedProtocolMessageType(
    "OrderedDict",
    (_message.Message,),
    {
        "DESCRIPTOR": _ORDEREDDICT,
        "__module__": "proto.lib.python.collections.ordered_dict_pb2"
        # @@protoc_insertion_point(class_scope:syft.lib.python.collections.OrderedDict)
    },
)
_sym_db.RegisterMessage(OrderedDict)

if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _ORDEREDDICT._serialized_start = 119
    _ORDEREDDICT._serialized_end = 197
# @@protoc_insertion_point(module_scope)
