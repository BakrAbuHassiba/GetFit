from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from .models import Foods

# admin.site.register()
@admin.register(Foods)
class PostImportExportAction(ImportExportActionModelAdmin):
    pass
