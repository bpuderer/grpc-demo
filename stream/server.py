import time
from concurrent import futures

import grpc

import streamer_pb2
import streamer_pb2_grpc


class Streamer(streamer_pb2_grpc.StreamerServicer):

    def Stream(self, request, context):
        print "RECEIVED:\n{}".format(request)

        for resp in [2.0, 4.0, 6.0]:
            print "SENDING:\n{}".format(resp)
            yield streamer_pb2.Response(value=resp)


if __name__ == '__main__':
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    streamer_pb2_grpc.add_StreamerServicer_to_server(Streamer(), server)
    print 'Starting server on port 50051'
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)
