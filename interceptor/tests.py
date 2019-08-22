import unittest

import grpc

from header_manipulator_client_interceptor import header_adder_interceptor
from types_pb2 import TestRequest
from types_pb2_grpc import TypesDemoServiceStub


TIMEOUT_SEC = 0.15
METADATA = [('key1', 'val1'), ('key2', 'val2'),]

class GrpcTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        interceptor = header_adder_interceptor(METADATA)
        cls._channel = grpc.insecure_channel('localhost:50051')
        intercept_channel = grpc.intercept_channel(cls._channel, interceptor)
        cls._stub = TypesDemoServiceStub(intercept_channel)


    @classmethod
    def tearDownClass(cls):
        cls._channel.close()


    def test_types_demo(self):
        response = self._stub.TypesDemo(TestRequest(str_field='str_field value'), timeout=TIMEOUT_SEC)
        self.assertEqual(response.status, 'OK')


if __name__ == '__main__':
    unittest.main()
