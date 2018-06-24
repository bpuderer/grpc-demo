import time
from concurrent import futures

import grpc

from streamer_pb2 import Response
import streamer_pb2_grpc


class Streamer(streamer_pb2_grpc.TriplingStreamerServicer):

    def Triple(self, requests, context):
        for request in requests:
            print("RECEIVED:\n{}".format(request))
            response = Response(result=request.num*3)
            print("SENDING:\n{}".format(response))
            yield response


if __name__ == '__main__':
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    streamer_pb2_grpc.add_TriplingStreamerServicer_to_server(Streamer(), server)
    print('Starting server on port 50051')
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)
