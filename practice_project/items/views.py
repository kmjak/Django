from django.shortcuts import render
from django.shortcuts import redirect
from .forms import ProductsForm
from .models import Products

from django.db.models import Q

from django.views.generic import ListView,DetailView

# Create your views here.
def index(request):
    params = {
        "title":"インデックスページ",
    }
    return render(request,"items/index.html",params)

def register(request):
    params = {
        "title":"登録ページ",
        'form': ProductsForm(),
    }
    if request.method == "POST":
        obj = Products()
        product = ProductsForm(request.POST,instance=obj)
        product.save()
        return redirect(to="/items/register")
    return render(request,"items/register.html",params)

class ProductsList(ListView):
    model = Products

class ProductsDetail(DetailView):
    model = Products

def detail(request):
    # try:
    search = request.POST["search"]
    obj = Products.objects.filter(Q(name__icontains=search)|Q(category__icontains=search))
    params = {"object":obj}
    return render(request,"items/products_detail.html",params)
    # except:
    #     return redirect(to="/items/list")

def edit(request,p_id):
    obj = Products.objects.get(id=p_id)
    if request.method == "POST":
        product = ProductsForm(request.POST,instance=obj)
        product.save()
        return redirect(to="/items/list")
    params = {
        "title":"更新ページ",
        "id":p_id,
        "form":ProductsForm(instance=obj),
    }
    return render(request,"items/edit.html",params)

def delete(request,p_id):
    obj = Products.objects.get(id=p_id)
    if request.method == "POST":
        obj.delete()
        return redirect(to="/items/list")
    params = {
        "title":"削除ページ",
        "id":p_id,
        "object":obj
    }
    return render(request,"items/delete.html",params)
