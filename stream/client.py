import grpc

from streamer_pb2 import Request
import streamer_pb2_grpc


if __name__ == '__main__':
    channel = grpc.insecure_channel('localhost:50051')
    stub = streamer_pb2_grpc.TriplingStreamerStub(channel)

    requests = (Request(num=n) for n in xrange(4))

    response = stub.Triple(requests)
    for resp in response:
        print "RECEIVED:\n{}".format(resp)
