from django import forms


class UserForm(forms.Form):
    username = forms.CharField(label="", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

# class RegisterForm(forms.Form):
#     user_type = {
#         ('company', '公司'),
#         ('government', '政府'),
#         ('center', '维修中心')
#     }
#     username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
#     password1 = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
#     password2 = forms.CharField(label="确认密码", max_length=256,
#                                 widget=forms.PasswordInput(attrs={'class': 'form-control'}))
#     usertype = forms.CharField(max_length=32, choices=user_type)
