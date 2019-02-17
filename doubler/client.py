import grpc

import doubler_pb2
import doubler_pb2_grpc


TIMEOUT_SEC = 1

if __name__ == '__main__':
    # https://grpc.io/grpc/python/grpc.html#create-client
    channel = grpc.insecure_channel('localhost:50051')
    stub = doubler_pb2_grpc.DoublerStub(channel)
    number = doubler_pb2.Number(value=3.0)
    # https://grpc.io/grpc/python/grpc.html#multi-callable-interfaces
    response = stub.Double(number, timeout=TIMEOUT_SEC)
    print("received: {}".format(response.value))
