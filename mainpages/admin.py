from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from .models import Food, User

admin.site.register(User)


@admin.register(Food)
class PostImportExportAction(ImportExportActionModelAdmin):
    pass
