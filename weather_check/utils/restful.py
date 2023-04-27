# -*- coding: utf-8 -*-
# FileName  : restful.py
from django.http import JsonResponse


class HttpCode(object):
    ok = 200
    # 参数错误
    paraesrror = 400
    # 没有授权
    unauth = 401
    # 请求方法错误
    methoderror = 405
    # 服务器内部错误
    servererror = 500
    # 检测花卉概率过低
    flowererror = 40002


def result(code=HttpCode.ok, message="", data=None, kwargs=None):
    json_dict = {'code': code, 'message': message, 'data': data}
    if kwargs and isinstance(kwargs, dict) and kwargs.keys():
        json_dict.update(kwargs)
    return JsonResponse(json_dict)


# 一切正常
def ok(message='ok', data=None):
    return result(code=HttpCode.ok, message=message, data=data)


# 检测花卉错误
def flower_error(message="", data=None):
    return result(code=HttpCode.flowererror, message=message, data=data)


# 参数错误
def params_error(message="", data=None):
    return result(code=HttpCode.paraesrror, message=message, data=data)


# 权限错误
def unauth(message="", data=None):
    return result(code=HttpCode.unauth, message=message, data=data)


# 请求方式错误
def method_error(message="", data=None):
    return result(code=HttpCode.methoderror, message=message, data=data)


# 服务器内部错误
def server_error(message="", data=None):
    return result(code=HttpCode.servererror, message=message, data=data)
