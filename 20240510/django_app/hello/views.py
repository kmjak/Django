from django.shortcuts import render
from django.shortcuts import redirect
from django.db.models import Count
from django.db.models import Sum
from django.db.models import Avg
from django.db.models import Max
from django.db.models import Min
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.views.generic import ListView
from django.views.generic import DetailView
# from .forms import SessionForm
from .models import Friend
from .models import Message
from .forms import SearchForm
# from .forms import HelloForm
from .forms import FriendForm
from .forms import FindForm
from .forms import CheckForm
from .forms import MessageForm
from django.db.models import Q

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
# def index(request):
#     params = {
#         'title':'Hello',
#         'message':'your data',
#         'form':HelloForm()
#     }
#     if request.method == 'POST':
#         params['message'] = '名前' + request.POST['name'] + \
#             '<br>メール:' + request.POST['mail'] + \
#             '<br>年齢:' + request.POST['age']
#         params['form'] = HelloForm(request.POST)
#     return render(request,'hello/index.html',params)

## HelloViewクラスを作る
# class HelloView(TemplateView):
#     def __init__(self):
#         self.params = {
#             'title':'Hello',
#             'message': 'your data',
#             'form': HelloForm()
#         }
#     def get(self,request):
#         return render(request, 'hello/index.html', self.params)
#     def post(self,request):
#         msg = 'あなたは、<b>' + request.POST['name'] + '(' + request.POST['age'] + ')</b>さんです。<br>メールアドレスは<b>' + request.POST['mail'] + '</b>ですね。'
#         self.params['message'] = msg
#         self.params['form'] = HelloForm(request.POST)
#         return render(request,"hello/index.html",self.params)

## checkboxをクリックするとsuccessと表示する
# class HelloView(TemplateView):
#     def __init__(self):
#         self.params = {
#             'title' : 'hello',
#             'form' : HelloForm(),
#             'result' :  None
#         }
#     def get(self,request):
#         return render(request,"hello/index.html",self.params)
#     def post(self,request):
#         if('check' in request.POST):
#             self.params['result'] = 'Checked!!'
#         else:
#             self.params['result'] = "Not Checked.."
#         self.params['form'] = HelloForm(request.POST)
#         return render(request,"hello/index.html",self.params)

## null も含めたcheck box
# class HelloView(TemplateView):
#     def __init__(self):
#         self.params = {
#             'title':'',
#             'form':HelloForm(),
#             'result':None
#         }
#     def get(self,request):
#         return render(request,"hello/index.html",self.params)
#     def post(self,request):
#         chk = request.POST['check']
#         self.params['result'] = "you checked " + chk + "."
#         self.params['form'] = HelloForm(request.POST)
#         return render(request,"hello/index.html",self.params)

## プルダウンメニューの作成(ラジオボタン、選択リストでも同じでできる)
# class HelloView(TemplateView):
#     def __init__(self):
#         self.params = {
#             'title':'',
#             'form':HelloForm(),
#             'result':None
#         }
#     def get(self,request):
#         return render(request,"hello/index.html",self.params)
#     def post(self,request):
#         ch = request.POST['choice']
#         self.params['result'] = "you checked " + ch + "."
#         self.params['form'] = HelloForm(request.POST)
#         return render(request,"hello/index.html",self.params)

## 複数選択項目リスト
# class HelloView(TemplateView):
#     def __init__(self):
#         self.params = {
#             'title':'',
#             'form':HelloForm(),
#             'result':None
#         }
#     def get(self,request):
#         return render(request,"hello/index.html",self.params)
#     def post(self,request):
#         ch = request.POST.getlist('choice')
#         self.params['result'] = "you checked " + str(ch) + "."
#         self.params['form'] = HelloForm(request.POST)
#         return render(request,"hello/index.html",self.params)

## session 
# class HelloView(TemplateView):
#     def __init__(self):
#         self.params = {
#             'title':'',
#             'form':SessionForm(),
#             'result':None
#         }
#     def get(self,request):
#         self.params['result'] = request.session.get('last_msg','No message')
#         return render(request,"hello/index.html",self.params)
#     def post(self,request):
#         ses = request.POST['session']
#         self.params['result'] = "send : '" + ses + "'."
#         request.session['last_msg'] = ses
#         self.params['form'] = SessionForm(request.POST)
#         self.params['s'] = request.session.keys()
#         return render(request,"hello/index.html",self.params)

## ミドルウェア
def sample_middleware(get_response):

    def middleware(request):
        counter = request.session.get('counter',0)
        request.session['counter'] = counter + 1
        response = get_response(request)
        print("count:" + str(counter))
        return response
    return middleware

# def index(request):
#     data = Friend.objects.all()
#     msg = str(Friend.objects.aggregate(Count('age')))
#     msg += "<br>" + str(Friend.objects.aggregate(Sum('age')))
#     msg += "<br>" + str(Friend.objects.aggregate(Avg('age')))
#     msg += "<br>" + str(Friend.objects.aggregate(Min('age')))
#     msg += "<br>" + str(Friend.objects.aggregate(Max('age')))
#     params = {
#         'title':'Hello',
#         'message': msg,
#         'form':SearchForm(),
#         'data':data,
#     }
#     if(request.method == "POST"):
#         num = request.POST['id']
#         try:
#             item = Friend.objects.get(id=num)
#             params['data'] = [item]
#         except:
#             pass
#         params['form'] = SearchForm(request.POST)
#     return render(request,"hello/index.html",params)

def create(request):
    if(request.method == "POST"):
        obj = Friend()
        friend = FriendForm(request.POST,instance=obj)
        friend.save()
        return redirect(to="/hello")
    params={
        "title":"Hello",
        "form":FriendForm(),
        # "form":HelloForm(),
    }
    # if(request.method=="POST"):
    #     name = request.POST['name']
    #     mail = request.POST['mail']
    #     gender = "gender" in request.POST
    #     age = request.POST['age']
    #     birthday = request.POST['birthday']
    #     friend = Friend(name=name,mail=mail,gender=gender,age=age,birthday=birthday)

    #     friend.save()
        
    #     return redirect(to="/hello")

    return render(request,"hello/create.html",params)



def edit(request,id):
    obj = Friend.objects.get(id=id)
    if(request.method == "POST"):
        friend = FriendForm(request.POST,instance=obj)
        friend.save()
        return redirect(to="/hello")
    params={
        "title":"Hello",
        "form":FriendForm(instance=obj),
        "id":id,
        # "form":HelloForm(),
    }
    return render(request,"hello/edit.html",params)

def delete(request,id):
    obj = Friend.objects.get(id=id)
    if(request.method == "POST"):
        obj.delete()
        return redirect(to="/hello")
    params={
        "title":"Hello",
        "obj":obj,
        "id":id,
        # "form":HelloForm(),
    }
    return render(request,"hello/delete.html",params)

class FriendList(ListView):
    model = Friend


class FriendDetail(DetailView):
    model = Friend


## 検索をマスターしよう
def find(request):
    params = {
        'title':'Hello/Find',
        'msg':"search word..",
        'form': FindForm(),
        'data':Friend.objects.all(),
    }
    if request.method == "POST":
        params["form"] = FindForm(request.POST)
        find = request.POST['find']
        l = find.split()
        sql = 'select * from hello_friend'
        # params["data"] = Friend.objects.filter(Q(name__icontains=find)|Q(mail__icontains=find))
        # params["data"] = Friend.objects.all()[int(l[0]):int(l[1])]
        if(find):
            sql += ' where name like "%' + find +'%"'
        params["data"] = Friend.objects.raw(sql)
        # params["msg"] = 'Result:' + str(params["data"].count())

    return render(request,'hello/find.html',params)

def check(request):
    params = {
        'title':'Hello',
        'message':'check validation',
        'form':FriendForm()
    }
    if request.method == "POST":
        obj = Friend()
        form = FriendForm(request.POST,instance=obj)
        params['form'] = form
        if (form.is_valid()):
            params['message'] = 'OK!'
        else:
            params['message'] = 'no good'
    return render(request,'hello/check.html',params)

def index(request,num=1):
    data = Friend.objects.all()
    page = Paginator(data,3)
    params ={
        'title':'Hello',
        'message':str(num) + "ページ",
        'data':page.get_page(num),
    }
    return render(request, 'hello/index.html',params)

def message(request,page=1):
    if request.method == "POST":
        obj = Message()
        form = MessageForm(request.POST, instance=obj)
        form.save()
    data = Message.objects.all().reverse()
    paginator = Paginator(data,2)
    params = {
        'title': 'Message',
        'form': MessageForm(),
        'data': paginator.get_page(page),
    }
    return render(request, 'hello/message.html',params)