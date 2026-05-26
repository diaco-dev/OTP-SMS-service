from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from otp_fz.models import User


class UserResource(resources.ModelResource):
    class Meta:
        model = User

@admin.register(User)
class UserResource(ImportExportModelAdmin):
    resource_class = UserResource

#
