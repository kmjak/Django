from django import forms
from .models import Products

class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['name','price','stack','category']
        labels = {'name':"商品名",'price':"価格",'stack':"在庫",'category':"カテゴリー"}

class SearchForm(forms.Form):
    p_id = forms.IntegerField(label="id")
