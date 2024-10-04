# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: otc/v1/types.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12otc/v1/types.proto\x12\x06otc.v1*\x9a\x01\n\x0cOtcErrorCode\x12\x1e\n\x1aOTC_ERROR_CODE_UNSPECIFIED\x10\x00\x12\"\n\x1eOTC_ERROR_CODE_INVALID_REQUEST\x10\x01\x12\"\n\x1eOTC_ERROR_CODE_NOT_IMPLEMENTED\x10\x02\x12\"\n\x1eOTC_ERROR_CODE_UNAUTHENTICATED\x10\x03*9\n\x04Side\x12\x14\n\x10SIDE_UNSPECIFIED\x10\x00\x12\x0c\n\x08SIDE_BUY\x10\x01\x12\r\n\tSIDE_SELL\x10\x02*\x83\x01\n\x12SubscriptionStatus\x12#\n\x1fSUBSCRIPTION_STATUS_UNSPECIFIED\x10\x00\x12\"\n\x1eSUBSCRIPTION_STATUS_SUBSCRIBED\x10\x01\x12$\n SUBSCRIPTION_STATUS_UNSUBSCRIBED\x10\x02*W\n\x0bOtcExchange\x12\x1c\n\x18OTC_EXCHANGE_UNSPECIFIED\x10\x00\x12\x14\n\x10OTC_EXCHANGE_ICE\x10\x01\x12\x14\n\x10OTC_EXCHANGE_CME\x10\x02*D\n\tOrderType\x12\x1a\n\x16ORDER_TYPE_UNSPECIFIED\x10\x00\x12\x1b\n\x17ORDER_TYPE_FILL_OR_KILL\x10\x01*\xc1\x01\n\nOrderState\x12\x1b\n\x17ORDER_STATE_UNSPECIFIED\x10\x00\x12\x1f\n\x1bORDER_STATE_PENDING_CREATED\x10\x01\x12\x17\n\x13ORDER_STATE_CREATED\x10\x02\x12\x13\n\x0fORDER_STATE_NEW\x10\x03\x12\x16\n\x12ORDER_STATE_FILLED\x10\x06\x12\x16\n\x12ORDER_STATE_KILLED\x10\x08\x12\x17\n\x13ORDER_STATE_ERRORED\x10\n*\xa4\x02\n\x0fOrderActionType\x12!\n\x1dORDER_ACTION_TYPE_UNSPECIFIED\x10\x00\x12%\n!ORDER_ACTION_TYPE_PENDING_CREATED\x10\x0b\x12\x1d\n\x19ORDER_ACTION_TYPE_CREATED\x10\x15\x12\x1e\n\x1aORDER_ACTION_TYPE_REJECTED\x10\x1f\x12%\n!ORDER_ACTION_TYPE_UPDATE_REJECTED\x10 \x12\x1a\n\x16ORDER_ACTION_TYPE_FILL\x10)\x12\"\n\x1eORDER_ACTION_TYPE_FILL_CORRECT\x10*\x12!\n\x1dORDER_ACTION_TYPE_FILL_CANCEL\x10+*\\\n\x0cNewsFeedType\x12\x1e\n\x1aNEWS_FEED_TYPE_UNSPECIFIED\x10\x00\x12\x16\n\x12NEWS_FEED_TYPE_RSS\x10\x01\x12\x14\n\x10NEWS_FEED_TYPE_X\x10\x02*\xcd\x03\n\x0cTradingError\x12\x1d\n\x19TRADING_ERROR_UNSPECIFIED\x10\x00\x12\x1c\n\x17TRADING_ERROR_FORBIDDEN\x10\x93\x03\x12\x1c\n\x17TRADING_ERROR_NOT_FOUND\x10\x94\x03\x12#\n\x1eTRADING_ERROR_TRADING_DISABLED\x10\x95\x03\x12$\n\x1fTRADING_ERROR_TRADING_SUSPENDED\x10\x96\x03\x12!\n\x1cTRADING_ERROR_NOT_SUBSCRIBED\x10\x97\x03\x12!\n\x1cTRADING_ERROR_INVALID_SYMBOL\x10\x9d\x03\x12 \n\x1bTRADING_ERROR_INVALID_VALUE\x10\xa6\x03\x12 \n\x1bTRADING_ERROR_INVALID_STATE\x10\xa8\x03\x12 \n\x1bTRADING_ERROR_INVALID_PRICE\x10\xa9\x03\x12$\n\x1fTRADING_ERROR_CONTRACT_EXPIRING\x10\xaa\x03\x12!\n\x1cTRADING_ERROR_INTERNAL_ERROR\x10\xf4\x03\x12\"\n\x1dTRADING_ERROR_NOT_IMPLEMENTED\x10\xf5\x03*6\n\x07\x43hannel\x12\x17\n\x13\x43HANNEL_UNSPECIFIED\x10\x00\x12\x12\n\x0e\x43HANNEL_ORDERS\x10\x01\x42\x0b\xaa\x02\x08Onyx.Otcb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'otc.v1.types_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\252\002\010Onyx.Otc'
  _globals['_OTCERRORCODE']._serialized_start=31
  _globals['_OTCERRORCODE']._serialized_end=185
  _globals['_SIDE']._serialized_start=187
  _globals['_SIDE']._serialized_end=244
  _globals['_SUBSCRIPTIONSTATUS']._serialized_start=247
  _globals['_SUBSCRIPTIONSTATUS']._serialized_end=378
  _globals['_OTCEXCHANGE']._serialized_start=380
  _globals['_OTCEXCHANGE']._serialized_end=467
  _globals['_ORDERTYPE']._serialized_start=469
  _globals['_ORDERTYPE']._serialized_end=537
  _globals['_ORDERSTATE']._serialized_start=540
  _globals['_ORDERSTATE']._serialized_end=733
  _globals['_ORDERACTIONTYPE']._serialized_start=736
  _globals['_ORDERACTIONTYPE']._serialized_end=1028
  _globals['_NEWSFEEDTYPE']._serialized_start=1030
  _globals['_NEWSFEEDTYPE']._serialized_end=1122
  _globals['_TRADINGERROR']._serialized_start=1125
  _globals['_TRADINGERROR']._serialized_end=1586
  _globals['_CHANNEL']._serialized_start=1588
  _globals['_CHANNEL']._serialized_end=1642
# @@protoc_insertion_point(module_scope)
