import time
from datetime import datetime
from concurrent import futures

import grpc
from grpc_reflection.v1alpha import reflection

import doubler_pb2
import doubler_pb2_grpc
import inanemath


class Doubler(doubler_pb2_grpc.DoublerServicer):

    def Double(self, request, context):
        response = doubler_pb2.Number()
        response.value = inanemath.double(request.value)
        print(f'{datetime.now()}\tDouble\tReceived: {request.value}\tReturning: {response.value}')
        return response

    def AnotherDouble(self, request, context):
        response = doubler_pb2.Number()
        response.value = inanemath.double(request.value)
        print(f'{datetime.now()}\tAnotherDouble\tReceived: {request.value}\tReturning: {response.value}')
        return response


if __name__ == '__main__':
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    doubler_pb2_grpc.add_DoublerServicer_to_server(Doubler(), server)
    SERVICE_NAMES = (
        doubler_pb2.DESCRIPTOR.services_by_name['Doubler'].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)
    print('Starting server with reflection enabled on port 50051')
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)
