from django.shortcuts import render
from django.http import HttpResponse
from .forms import HelloForm

## getリクエストの受け取り方
# Create your views here.
# def index(request):
#     if 'msg' in request.GET:
#         msg = request.GET['msg']
#         result = 'you typed:"' + msg + '".'
#     else:
#         result = 'please send msg parameter!'

## 
# def index(request,id,nickname):
#     result = 'id: ' + str(id) + "name: " + nickname
#     return HttpResponse(result)

## ３ページ遷移
# def index(request):
#     params = {
#         'title':'hello/index',
#         'msg':'this is sample page',
#         'goto':'next'
#     }
#     return render(request,'hello/index.html',params)
# def next(request):
#     params = {
#         'title':'hello/next',
#         'msg':'this is next page',
#         'goto':'test'
#     }
#     return render(request,'hello/index.html',params)
# def test(request):
#     params = {
#         'title':'hello/test',
#         'msg':'this is test page',
#         'goto':'index'
#     }
#     return render(request,'hello/index.html',params)

## formを作る
# def index(request):
#     params = {
#         'title':'Hello/Index',
#         'msg':'お名前は?'
#     }
#     return render(request, 'hello/index.html', params)

# def form(request):
#     msg = request.POST['msg']
#     params = {
#         'title':'Hello/Form',
#         'msg':'こんにちは' + msg + 'さん。'
#     }
#     return render(request, 'hello/index.html', params)

## forms.pyを使ってformを作る
def index(request):
    params = {
        'title':'Hello',
        'message':'your data',
        'form':HelloForm()
    }
    if request.method == 'POST':
        params['message'] = '名前' + request.POST['name'] + \
            '<br>メール:' + request.POST['mail'] + \
            '<br>年齢:' + request.POST['age']
        params['form'] = HelloForm(request.POST)
    return render(request,'hello/index.html',params)