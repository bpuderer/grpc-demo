import time
import uuid
from concurrent import futures

import grpc

import types_pb2_grpc
from types_pb2 import TestResponse


class TypesDemoService(types_pb2_grpc.TypesDemoServiceServicer):

    def TypesDemo(self, request, context):
        for k,v in context.invocation_metadata():
            print(f'Received metadata: key={k} value={v}')

        print(f'RECEIVED:\n{request}-----')

        response = TestResponse(status='OK', tracking_id=str(uuid.uuid4()))
        response.timestamp_field.GetCurrentTime()
        print(f'SENDING:\n{response}')
        return response


    def EmptyRequestDemo(self, request, context):
        for k,v in context.invocation_metadata():
            print(f'Received metadata: key={k} value={v}')

        print(f'RECEIVED:\n{request}-----')

        response = TestResponse(status='OK', tracking_id=str(uuid.uuid4()))
        response.timestamp_field.GetCurrentTime()
        print(f'SENDING:\n{response}')
        return response


if __name__ == '__main__':
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    types_pb2_grpc.add_TypesDemoServiceServicer_to_server(TypesDemoService(), server)
    print('Starting server on port 50051')
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)
