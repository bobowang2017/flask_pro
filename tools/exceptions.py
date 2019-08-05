import traceback


class ApiError(Exception):
    def __init__(self, value="UnKnow Reason", op="", data=None):
        self.value = str(value)
        self.data = data
        self.op = str(op)
        if op:
            self.value = "{cls}.{op}: {value}".format(cls=self.__class__.__name__, op=str(self.op),
                                                      value=str(self.value))
        else:
            self.value = "{value}".format(value=str(self.value))
        super().__init__(self.value)

    @property
    def is_exist_error(self):
        if not hasattr(self, "_exist"):
            self._exist = False
        return self._exist

    @property
    def is_not_exist_error(self):
        if not hasattr(self, "_not_exist"):
            self._not_exist = False
        return self._not_exist


class NoAccess(ApiError):
    def __init__(self, value="Forbidden", data=None):
        self.data = data
        super().__init__(value="无访问权限")


class NoExistError(ApiError):
    def __init__(self, value="无数据异常", data=None):
        self._noexist = True
        self.data = data
        super().__init__(value)


class InputError(ApiError):
    def __init__(self, value="输入错误", data=None):
        self.data = data
        if isinstance(value, dict):
            value = "\n".join([str(k) + " " + ".".join(v) for k, v in value.items()])
        super().__init__(value)


class ErrorReturnData(ApiError):
    def __init__(self, value="unknow reason", data=None, op=""):
        self.data = data
        super().__init__(value, op)


class NeedRecordError(ApiError):
    def __init__(self, value="unknow reason", data=None):
        self.data = data
        super().__init__(value)


class InternalError(ApiError):
    def __init__(self, value="内部错误", data=None):
        self.data = data
        super().__init__(value)

