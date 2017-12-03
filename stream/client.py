import grpc

import streamer_pb2
import streamer_pb2_grpc


if __name__ == '__main__':
    channel = grpc.insecure_channel('localhost:50051')
    stub = streamer_pb2_grpc.StreamerStub(channel)
    response = stub.Stream(streamer_pb2.Request(value=3.0))

    for resp in response:
        print "RECEIVED:\n{}".format(resp)
