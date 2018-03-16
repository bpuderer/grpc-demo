import time
import uuid
from concurrent import futures

import grpc

import types_pb2_grpc
from builders import test_response_builder


class TypesDemoService(types_pb2_grpc.TypesDemoServiceServicer):

    def TypesDemo(self, request, context):
        print "RECEIVED:\n{}-----".format(request)
        response = test_response_builder("OK", str(uuid.uuid4()))
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
