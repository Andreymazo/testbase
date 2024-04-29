import json
import re
from django.shortcuts import render
from django.http import HttpResponse
from testbase.models import RealEstateObject
from django.views.decorators.csrf import csrf_exempt
import requests

def values_to_param(filter_query, param):
    if not re.compile(f"{param}=(.*)&"):
      param = re.compile(f"{param}=(\d+)&")
    param = re.compile(f"{param}=(\d+)")
    param = param.findall(filter_query)
    return param
    
@csrf_exempt
def home(request):
    print('We at testbase home')
    result = False
    cad_num = 'cad_num'
    shirota = 'shirota'
    dolgota = 'dolgota'
    # print('request.META'  , request.META)
    # print("request.META['QUERY_STRING']", request.META['QUERY_STRING']) ## cad_num=23&shirota=23&dolgota=23
    # print('request.__dict__', request.__dict__)
    filter_query = request.META['QUERY_STRING']
    print('filter_query', filter_query)
    cad_num = values_to_param(filter_query, cad_num)
    shirota = values_to_param(filter_query, shirota)
    dolgota = values_to_param(filter_query, dolgota)
    filter_query_all = (cad_num[0], shirota[0], dolgota[0])
    # print('dolgota______________________________', dolgota)
    # cad_num = re.compile(f"{cad_num}=(\d+)&")
    # cad_num = cad_num.findall(filter_query)
    # print('cad_num______________________________', cad_num[0])
        # clear_query=re.compile("cad_num \(ts\/tv\) =")
        # clear_query = re.compile("cad_num=(.*)&")
    

    # clear_query = re.compile(f"{cad_num}=(\d+)&")
    # clear_query = clear_query.findall(filter_query)[0]
    # print('print(request.POST.__dict__)', request.POST.__dict__)
    filter_lst = RealEstateObject.objects.all().values_list('cad_num', 'shirota', 'dolgota')
    if filter_query_all in filter_lst:
        result = True
    # print("filter_query = request.META['QUERY_STRING']", filter_query)

    print('almost finish ))))))))))))))))))')
    
    url = 'http://127.0.0.1:8000/result/receive'
    data = {result:result}
   
    response = requests.post(url, params=data)#, headers={ 'X-CSRFToken': clear_token})
    # print('response.headers', response_get.headers)
    # print('request.META', request.META['HTTP_COOKIE'])
    data = json.dumps(result)
    print('filter_query_all', filter_query_all, 'filter_lst', filter_lst)
    print('result', result)
    print(response.content)
    # if request.method == "POST":

    #   try:
    #         # reobject=RealEstateObject.objects.all().get(cad_num=cad_num, shirota=shirota, dolgota=dolgota)
    #         result=True
    #         context = {
    #             'result':result

    #     }
    #        # time.sleep(7)# Не обязательно все 60 сек ждать, достаточно 7
    #         print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

    #   except :
    #     print('--------------------------------------------iiii--------------------------------------')
    #     context = [{
    #     'result':result
    #     }]
    #   return HttpResponse(data, content_type='json')

    return HttpResponse(data, content_type='json')

#import json

#from django.http import HttpResponse
#from django.core import serializers

#def get_object(request, name):
#    name = request.GET.get('name', '')
#    if name is not None:
#        obj = Company.objects.get(name=name)
#        company = serializers.serialize('json', [obj,])
#        struct = json.loads(company)
#        data = json.dumps(struct[0])
#        return HttpResponse(data, content_type='json')
#, render(request, 'testbase/templates/testrestapi/home.html', context)

