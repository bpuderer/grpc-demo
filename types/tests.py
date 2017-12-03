""" grpc tests """

import unittest

import grpc

import types_pb2
import types_pb2_grpc


class GrpcTestCase(unittest.TestCase):
    """ grpc test case """

    @classmethod
    def setUpClass(cls):
        """class setup"""
        cls._channel = grpc.insecure_channel('localhost:50051')
        cls._stub = types_pb2_grpc.TypesDemoServiceStub(cls._channel)

    @staticmethod
    def request_builder(str_field=None, int_field=None, bool_field=None, float_field=None,
                        enum_field=None, repeated_str_field=None, map_field=None,
                        number_field=None, timestamp_field_json_str=None):
        """Build TestRequest"""

        request = types_pb2.TestRequest()
        if str_field is not None:
            request.str_field = str_field
        if int_field is not None:
            request.int_field = int_field
        if bool_field is not None:
            request.bool_field = bool_field
        if float_field is not None:
            request.float_field = float_field
        if enum_field is not None:
            request.enum_field = enum_field
        if repeated_str_field is not None:
            request.repeated_str_field.extend(repeated_str_field)
        if map_field is not None:
            for key, val in map_field.iteritems():
                request.map_field[key] = val
        if number_field is not None:
            request.number_field.value = number_field
        if timestamp_field_json_str is not None:
            request.timestamp_field.FromJsonString(timestamp_field_json_str)
        return request


    def test_demo(self):
        """test demo"""

        request = self.request_builder("str_field value", 42, True, 28.3, 1, ["spam", "eggs"],
                                       {'a': 9, 'b': 10}, 2.0, "2017-12-03T14:17:00.000-04:00")

        response = self._stub.TypesDemo(request)

        self.assertEqual(response.str_field, "str_field value from server")


if __name__ == '__main__':
    unittest.main()
