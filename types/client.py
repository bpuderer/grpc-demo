from datetime import datetime

import grpc

import types_pb2
import types_pb2_grpc


if __name__ == '__main__':
    channel = grpc.insecure_channel('localhost:50051')
    stub = types_pb2_grpc.TypesDemoServiceStub(channel)

    request = types_pb2.TestRequest()
    request.str_field = 'str_field value'
    request.int_field = 42
    request.bool_field = True
    request.float_field = 28.3
    request.enum_field = 1
    request.repeated_str_field.extend(['spam', 'eggs'])
    request.map_field['a'] = 9
    request.map_field['b'] = 10
    request.number_field.value = 2.0
    #request.timestamp_field.GetCurrentTime()
    #request.timestamp_field.FromJsonString("2017-12-02T20:00:20.021-04:00")
    #request.timestamp_field.FromDatetime(datetime.utcnow())
    request.timestamp_field.FromDatetime(datetime(2017, 12, 2))

    print "SENDING: \n{}-----".format(request)
    response = stub.TypesDemo(request)
    print "RECEIVED:\n{}".format(response)
