import unittest


class Test(unittest.TestCase):

    def setUp(self):
        self.XXX = None

    def test_print_name(self):
        _configs = [{
            'configType': 'application',
            'data': [{
                'key': '1', 'value': '2', 'readonly': 'False'},
                {'key': '1', 'value': '2', 'readonly': 'True'},
                {'key': '100', 'value': '200', 'readonly': 'True'}
            ]}, {
            'configType': 'redis',
            'data': [{
                'key': '1', 'value': '1', 'readonly': 'True'},
                {'key': '1', 'value': '1', 'readonly': 'True'}
            ]
        }]
        result = [{'configType':  _c['configType'], 'key': _cc['key'], 'value': _cc['value']} for _c in _configs for _cc in _c['data']]
        print(result)
