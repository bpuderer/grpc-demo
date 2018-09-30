"""grpc tests"""

import unittest

import grpc
from google.protobuf import json_format

from types_pb2 import TestRequest
from types_pb2_grpc import TypesDemoServiceStub


class GrpcTestCase(unittest.TestCase):
    """grpc test case"""

    @classmethod
    def setUpClass(cls):
        """class setup"""

        cls._channel = grpc.insecure_channel('localhost:50051')
        cls._stub = TypesDemoServiceStub(cls._channel)

    @classmethod
    def tearDownClass(cls):
        """class teardown"""

        cls._channel.close()

    @staticmethod
    def build_request(filename, request):
        """build request from json file"""
        with open(filename) as f:
            json_str = f.read()
        return json_format.Parse(json_str, request)


    def test_demo(self):
        """test demo"""

        request = GrpcTestCase.build_request('./request1.json', TestRequest())

        # change some vals
        request.repeated_str_field.append('spam')
        request.map_field['c'] = 11
        request.number_field.value = 28
        request.bytes_field = 'bytes_field val'.encode()
        # from google.protobuf import duration_pb2, timestamp_pb2
        # help(duration_pb2)
        # help(timestamp_pb2)
        request.timestamp_field.GetCurrentTime()
        request.duration_field.FromSeconds(283)

        print(f'REQUEST:\n{request}-----')

        response = self._stub.TypesDemo(request)
        print(f'RESPONSE:\n{response}')

        # MessageToJson returns str
        print(f'in JSON format:\n{json_format.MessageToJson(response)}')

        self.assertEqual(response.status, 'OK')


if __name__ == '__main__':
    unittest.main()
