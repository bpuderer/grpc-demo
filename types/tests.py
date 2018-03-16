"""grpc tests"""

import unittest

import grpc

from types_pb2_grpc import TypesDemoServiceStub
from builders import test_request_builder


class GrpcTestCase(unittest.TestCase):
    """grpc test case"""

    @classmethod
    def setUpClass(cls):
        """class setup"""

        cls._channel = grpc.insecure_channel('localhost:50051')
        cls._stub = TypesDemoServiceStub(cls._channel)


    def test_demo(self):
        """test demo"""

        request_args = {"str_field": "str_field value", "int_field": 42, "bool_field": True, "float_field": 28.3, "enum_field": 1, "repeated_str_field": ["spam", "eggs"], "map_field": {"a": 9, "b": 10}, "number_field": 2.0, "oneof_int32": 28, "timestamp_field": "2018-03-16T08:00:00Z"}
        request = test_request_builder(**request_args)
        #print "REQUEST:\n{}-----".format(request)
        response = self._stub.TypesDemo(request)
        #print "RESPONSE:\n{}".format(response)
        self.assertEqual(response.status, "OK")


if __name__ == '__main__':
    unittest.main()
