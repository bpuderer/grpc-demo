from types_pb2 import TestRequest, TestResponse


def test_request_builder(str_field=None, int_field=None, bool_field=None, float_field=None,
                         enum_field=None, repeated_str_field=None, map_field=None,
                         number_field=None, oneof_str=None, oneof_int32=None,
                         timestamp_field=None):
    """Build TestRequest"""

    request = TestRequest()
    if str_field is not None:
        request.str_field = str_field
    if int_field is not None:
        request.int_field = int_field
    if bool_field is not None:
        request.bool_field = bool_field
    if float_field is not None:
        request.float_field = float_field
    if enum_field is not None:
        request.enum_field = enum_field
    if repeated_str_field is not None:
        request.repeated_str_field.extend(repeated_str_field)
    if map_field is not None:
        for key, val in map_field.iteritems():
            request.map_field[key] = val
    if number_field is not None:
        request.number_field.value = number_field
    if oneof_str is not None:
        request.oneof_str = oneof_str
    if oneof_int32 is not None:
        request.oneof_int32 = oneof_int32
    if timestamp_field is not None:
        # >>> from google.protobuf import timestamp_pb2
        # >>> help(timestamp_pb2)
        #request.timestamp_field.GetCurrentTime()
        #request.timestamp_field.FromJsonString("2018-03-16T12:00:00-04:00")
        #request.timestamp_field.FromDatetime(datetime.utcnow())
        #request.timestamp_field.FromSeconds(1521187200)
        request.timestamp_field.FromJsonString(timestamp_field)

    return request


def test_response_builder(status=None, tracking_id=None):
    """Build TestResponse"""

    response = TestResponse()
    if status is not None:
        response.status = status
    if tracking_id is not None:
        response.tracking_id = tracking_id

    return response
