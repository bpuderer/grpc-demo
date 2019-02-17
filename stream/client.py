import grpc

from streamer_pb2 import Request
import streamer_pb2_grpc


TIMEOUT_SEC = 1

if __name__ == '__main__':
    channel = grpc.insecure_channel('localhost:50051')
    stub = streamer_pb2_grpc.TriplingStreamerStub(channel)

    requests = (Request(num=n) for n in range(4))

    for resp in stub.Triple(requests, timeout=TIMEOUT_SEC):
        print("RECEIVED:\n{}".format(resp))
