from django.contrib import admin

from Accounts.models import User
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm, CustomUserCreationForm

admin.site.unregister(Group)

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'gr_key')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    def create_date(self, obj):
        return obj.date_joined.strftime("%d.%m.%Y")

    create_date.admin_order_field = 'date_joined'
    create_date.short_description = 'Дата регистрации'

    def _last_login(self, obj):
        if obj.last_login:
            return obj.last_login.strftime("%d.%m.%Y %H:%M:%S")
        return None

    _last_login.admin_order_field = 'last_login'
    _last_login.short_description = 'Дата авторизации'

    @staticmethod
    def _mail_dt(obj):
        if obj.mail_dt:
            return obj.mail_dt.strftime("%d.%m.%Y %H:%M:%S")
        return None

    list_display = ['id', 'email', 'create_date', '_last_login']

    list_display_links = ['email']

    readonly_fields = ['password', '_last_login', 'create_date', '_mail_dt']
    exclude = ['last_login', 'date_joined', 'mail_dt', 'groups', 'user_permissions']