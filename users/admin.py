from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

from users.models import User


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label="비밀번호", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="비밀번호 확인", widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ["email",]

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("입력된 비밀번호가 다릅니다.")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ["email", "password", "is_active", "is_admin"]


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ["id", "email", "is_admin"]
    list_filter = ["is_admin"]
    fieldsets = [
        (None, {"fields": ["email", "password",]}),
        ("Permissions", {"fields": ["is_admin"]}),
    ]
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "password1", "password2","age"],
            },
        ),
    ]
    search_fields = ["email"]
    ordering = ["email"]
    filter_horizontal = []


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
