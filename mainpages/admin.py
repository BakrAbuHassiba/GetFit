from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from .models import Foods ,User

admin.site.register(User)
@admin.register(Foods)
class PostImportExportAction(ImportExportActionModelAdmin):
    pass
