#coding=utf-8
"""
    （1）新建文件view.py
"""

from django.http import HttpResponse

import json

def main(request):

    return HttpResponse("hello world")

def login(request):
    # data = {code:200,msg:"success"}
    #获取前端的数据
    data = {"code":200,"msg":"success"}
    return HttpResponse(json.dumps(data))