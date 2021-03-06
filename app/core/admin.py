"""
Personalização do administrador do Django
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from core import models


class UserAdmin(BaseUserAdmin):
    """
    Definir as páginas de administração para usuários
    """

    ordering = ['id']
    list_display = [
        'id',
        'email',
        'name',
        'is_active',
        'is_staff',
        'is_superuser'
    ]
    fieldsets = (
        (None, {'fields': ('email', 'name', 'password')}),
        (
            _('Permissões'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            }
        ),
        (_('Data de acesso'), {'fields': ('last_login',)}),
    )
    readonly_fields = ['last_login']
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'password1',
                'password2',
                'name',
                'is_active',
                'is_staff',
                'is_superuser',
            )
        }),
    )


admin.site.register(models.User, UserAdmin)
