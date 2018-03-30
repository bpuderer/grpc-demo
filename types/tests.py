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


    def test_demo(self):
        """test demo"""

        with open("request1.json") as f:
            json_str = f.read()
        request = json_format.Parse(json_str, TestRequest())
        print "REQUEST:\n{}-----".format(request)

        response = self._stub.TypesDemo(request)
        print "RESPONSE:\n{}".format(response)

        self.assertEqual(response.status, "OK")


if __name__ == '__main__':
    unittest.main()
