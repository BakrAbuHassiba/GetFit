from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from .models import Foods, User

# admin.site.register()


@admin.register(Foods)
@admin.register(User)
class PostImportExportAction(ImportExportActionModelAdmin):
    pass
