import json

from django.http import HttpResponse
from django.conf import settings

def render_json(data=None,code=0):
    """规定json返回的数据"""
    result = {
        'data':data,
        'code':code,
    }
    if settings.DEBUG:
        json_result = json.dumps(result,ensure_ascii=False,indent=4,sort_keys=True)
    else:
        json_result = json.dumps(result,ensure_ascii=False,separators=(",",":"))
    return HttpResponse(json_result)