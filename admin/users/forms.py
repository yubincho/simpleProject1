from django import forms
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# class SearchForm(forms.Form):
#    keyword = forms.CharField({"error_messages": "키워드를 입력해주세요."}, max_length=30)


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password", "password2"]


"""
class RegisterForm(forms.ModelForm):

    email = forms.EmailField(
        error_messages={"required": "이메일을 입력해주세요."}, max_length=200, label="email"
    )
    password = forms.CharField(
        error_messages={"required": "비밀번호를 입력해주세요."},
        widget=forms.PasswordInput,
        label="password",
    )
    re_password = forms.CharField(
        error_messages={"required": "비밀번호를 확인해주세요."},
        widget=forms.PasswordInput,
        label="re_password",
    )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")
        re_password = cleaned_data.get("re_password")

        if password and re_password:
            if password != re_password:
                self.add_error("password", "비밀번호가 서로 다릅니다.")
                self.add_error("re_password", "비밀번호가 서로 다릅니다.")

            else:
                users = User(email=email, password=make_password(password))
                users.save()
"""


class LoginForm(forms.ModelForm):

    email = forms.EmailField(
        error_messages={"required": "이메일을 입력해주세요."}, max_length=200, label="email"
    )
    password = forms.CharField(
        error_messages={"required": "비밀번호를 입력해주세요."},
        widget=forms.PasswordInput,
        label="password",
    )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")

        if email and password:
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                self.add_error("email", "아이디가 없습니다.")
                return

            if not check_password(password, user.password):
                self.add_error("password", "비밀번호를 틀렸습니다.")
            else:
                self.user_id = user.id
