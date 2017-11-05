import grpc

import doubler_pb2
import doubler_pb2_grpc


if __name__ == '__main__':
    channel = grpc.insecure_channel('localhost:50051')
    stub = doubler_pb2_grpc.DoublerStub(channel)
    number = doubler_pb2.Number(value=3.0)
    response = stub.Double(number)
    print "received: {}".format(response.value)
