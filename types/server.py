import time
from concurrent import futures

import grpc

import types_pb2
import types_pb2_grpc



class TypesDemoService(types_pb2_grpc.TypesDemoServiceServicer):

    def TypesDemo(self, request, context):
        print "RECEIVED:\n{}-----".format(request)
        response = types_pb2.TestResponse()
        response.str_field = 'str_field value from server'
        response.int_field = 43
        response.bool_field = False
        response.float_field = 3.28
        response.enum_field = 0
        response.repeated_str_field.extend(['eggs', 'spam'])
        response.map_field['a'] = 10
        response.map_field['b'] = 9
        response.number_field.value = 3.0
        # response.oneof_str = "oneof string"
        response.oneof_int32 = 28
        response.timestamp_field.FromJsonString("2017-12-02T20:00:20.021-04:00")
        print "SENDING:\n{}".format(response)
        return response


if __name__ == '__main__':
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    types_pb2_grpc.add_TypesDemoServiceServicer_to_server(TypesDemoService(), server)
    print 'Starting server on port 50051'
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)
