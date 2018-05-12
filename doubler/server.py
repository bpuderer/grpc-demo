import time
from datetime import datetime
from concurrent import futures

import grpc

import doubler_pb2
import doubler_pb2_grpc
import inanemath


class Doubler(doubler_pb2_grpc.DoublerServicer):

    def Double(self, request, context):
        response = doubler_pb2.Number()
        response.value = inanemath.double(request.value)
        print "{}\tDouble\treceived: {}\treturning: {}".format(datetime.now(), request.value, response.value)
        return response

    def AnotherDouble(self, request, context):
        response = doubler_pb2.Number()
        response.value = inanemath.double(request.value)
        print "{}\tAnotherDouble\treceived: {}\treturning: {}".format(datetime.now(), request.value, response.value)
        return response

if __name__ == '__main__':
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    doubler_pb2_grpc.add_DoublerServicer_to_server(Doubler(), server)
    print 'Starting server on port 50051'
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)
