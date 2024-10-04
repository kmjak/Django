from django.shortcuts import render
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.core.serializers import serialize
from django.forms.models import model_to_dict
from .models import Message2, Good2
import json

# Create your views here.
page_max = 10

@login_required(login_url='/admin/login/')
def index(request):
    return render(request, 'index.html')

@login_required(login_url='/admin/login/')
def msgs(request,page=1):
    msgs = Message2.objects.all()
    paginator = Paginator(msgs, page_max)
    page_items = paginator.page(page)
    serialized = serialize('json', page_items)
    return HttpResponse(serialized, content_type='application/json')

@login_required(login_url='/admin/login/')
def lastPage(request):
    msgs = Message2.objects.all()
    paginate = Paginator(msgs, page_max)
    last_page = paginate.num_pages
    return JsonResponse({"result":"OK","value":last_page})

@login_required(login_url='/admin/login/')
def userName(request,user_id= -1):
    if user_id == -1:
        user = request.user
    else:
        user = User.objects.filter(id=user_id).filter()
    return JsonResponse({"result":"OK","value":user.username})

@login_required(login_url='/admin/login/')
def post(request):
    if request.method == 'POST':
        byte_data = request.body.decode('utf-8')
        json_data = json.loads(byte_data)
        msg = Message2()
        msg.owner = request.user
        msg.message = request.user.username
        msg.content = json_data['content']
        msg.save()
        return JsonResponse({"result":"OK"})
    else:
        return JsonResponse({"result":"NG"})

@login_required(login_url='/admin/login/')
def good(request,msg_id):
    msg = Message2.objects.get(id=msg_id)
    is_good = Good2.objects.filter(owner=request.user).filter(message=msg).count()
    if is_good > 0:
        return JsonResponse({"result":"NG"})
    msg.good_count += 1
    msg.save()
    good = Good2()
    good.owner = request.user
    good.message = msg
    good.save()
    return JsonResponse({"result":"OK"})