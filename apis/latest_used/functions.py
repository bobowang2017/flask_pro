import datetime

from sqlalchemy import Numeric


def serializer(data, many=False):
    def _convert_datetime(item):
        for k, v in item.items():
            if isinstance(v, datetime.datetime):
                item[k] = v.strftime("%Y-%m-%d %H:%M:%S")
            elif isinstance(v, Numeric):
                item[k] = float(v)
    if many:
        for _data in data:
            _convert_datetime(_data)
    else:
        _convert_datetime(data)
    return data
