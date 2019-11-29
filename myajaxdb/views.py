from django.shortcuts import render
from myajaxdb.models import Sangdata
from django.http.response import HttpResponse
import json

# Create your views here.
def MainFunc(request):
    return render(request, 'list.html')

def ListFunc(request):
    sdata = Sangdata.objects.all()
    #print(sdata)
    datas = [] # list
    for s in sdata:
        dic = {'code':s.code,'sang':s.sang,'su':s.su,'dan':s.dan}
        datas.append(dic)  # append for을 계속 더해주는 메서드
    #print(datas)
    return HttpResponse(json.dumps(datas), content_type="application/json") # HttpResponse는 요청이 들어온 곳으로 데이터를 넘겨줌   #dumps = dict->string으로 바꿔줌