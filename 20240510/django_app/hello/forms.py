from django import forms
from .models import Friend

# class HelloForm(forms.Form):
#     name = forms.CharField(label="name", widget=forms.TextInput(attrs={'class':'form-control'}))
#     mail = forms.EmailField(label="mail", widget=forms.EmailInput(attrs={'class':'form-control'}))
#     age = forms.IntegerField(label="age", widget=forms.NumberInput(attrs={'class':'form-control'}))

## check boxをcheckしたらsuccessと表示
# class HelloForm(forms.Form):
#     check = forms.BooleanField(label="checkbox",required=False)

## null も含めたcheck box
# class HelloForm(forms.Form):
#     check = forms.NullBooleanField(label="check box")

## プルダウンメニューを作る
# class HelloForm(forms.Form):
#     data = [
#         ('one', 'item 1'),
#         ('two', 'item 2'),
#         ('three', 'item 3'),
#     ]
#     choice = forms.ChoiceField(label="Choice",choices=data)

## radioボタンの作成
# class HelloForm(forms.Form):
#     data = [
#         ('one', 'radio 1'),
#         ('two', 'radio 2'),
#         ('three', 'radio 3'),
#     ]
#     choice = forms.ChoiceField(label="radio",choices=data,widget=forms.RadioSelect())

## 選択リストの作成
# class HelloForm(forms.Form):
#     data = [
#         ('one', 'item 1'),
#         ('two', 'item 2'),
#         ('three', 'item 3'),
#         ('four', 'item 4'),
#         ('five', 'item 5'),
#     ]
#     choice = forms.ChoiceField(label="radio",choices=data,widget=forms.Select(attrs={'size':'5','class':'form-select'}))

## 複数項目選択
# class HelloForm(forms.Form):
#     data = [
#         ('one', 'item 1'),
#         ('two', 'item 2'),
#         ('three', 'item 3'),
#         ('four', 'item 4'),
#         ('five', 'item 5'),
#     ]
#     choice = forms.MultipleChoiceField(label="radio",choices=data,widget=forms.SelectMultiple(attrs={'size':'5','class':'form-select'}))

## session
# class SessionForm(forms.Form):
#     session = forms.CharField(label="session", required=False,widget=forms.TextInput(attrs={'class':'form-control'}))

# class SessionForm(forms.Form):
#     session = forms.CharField(label='session',required=False,widget=forms.TextInput(attrs={'class':'form-control'}))

## database
class SearchForm(forms.Form):
    id = forms.IntegerField(label="id")

class HelloForm(forms.Form):
    name = forms.CharField(label="名前",widget=forms.TextInput(attrs={'class':'form-control'}))
    mail = forms.CharField(label="メールアドレス",widget=forms.TextInput(attrs={'class':'form-control'}))
    gender = forms.BooleanField(label="性別",required=False,widget=forms.CheckboxInput(attrs={'class':'form-check'}))
    age = forms.IntegerField(label="年齢",widget=forms.NumberInput(attrs={'class':'form-control'}))
    birthday = forms.DateField(label="誕生日",widget=forms.DateInput(attrs={'class':'form-control'}))

## modelsをもとにしたformの作り方
# class FriendForm(forms.ModelForm):
#     class Meta:
#         model = Friend
#         fields = ['name','mail','gender','age','birthday']
#         labels = {'name':"名前",'mail':"メール",'gender':"性別",'age':"年齢",'birthday':"誕生日"}

## 検索をマスターしよう
class FindForm(forms.Form):
    find = forms.CharField(label="Find",required=False,widget=forms.TextInput(attrs={'class':"form-control"}))

# class CheckForm(forms.Form):
#     empty = forms.CharField(label="Empty", empty_value=True,widget=forms.TextInput(attrs={'class':'form-control'}))
#     min = forms.CharField(label="min", min_length=10, widget=forms.TextInput(attrs={'class':'form-control'}))
#     max = forms.CharField(label="max", max_length=10, widget=forms.TextInput(attrs={'class':'form-control'}))
#     intmin = forms.IntegerField(label="int min", min_value=100, widget=forms.NumberInput(attrs={'class':'form-control'}))
#     intmax = forms.IntegerField(label="int max", max_value=1000, widget=forms.NumberInput(attrs={'class':'form-control'}))
#     date = forms.DateField(label='date', input_formats=['%d'], widget=forms.DateInput(attrs={'class':'form-control'}))
#     time = forms.TimeField(label='time', widget=forms.TimeInput(attrs={'class':'form-control'}))
#     timedate = forms.DateTimeField(label='date/time', widget=forms.DateTimeInput(attrs={'class':'form-control'}))

class CheckForm(forms.Form):
    s = forms.CharField(label='string', widget=forms.TextInput(attrs={'class':'form-control'}))

    def clean(self):
        cleaned_data = super().clean()
        s = cleaned_data['s']
        if s.lower().startswith('no'):
            raise forms.ValidationError('You input "NO"!')


class FriendForm(forms.ModelForm):
    class Meta:
        model = Friend
        fields = ["name","mail","gender","age","birthday"]
        widget = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'mail' : forms.EmailInput(attrs={'class':'form-control'}),
            'age' : forms.NumberInput(attrs={'class':'form-control'}),
            'birthday' : forms.DateInput(attrs={'class':'form-control'}),
        }