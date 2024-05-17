from django import forms

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
class SessionForm(forms.Form):
    session = forms.CharField(label="session", required=False,widget=forms.TextInput(attrs={'class':'form-control'}))