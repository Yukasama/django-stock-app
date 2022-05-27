from django.contrib import admin
from eye.models import Stock, Info, Financial
from import_export import resources

admin.site.register(Stock)
admin.site.register(Info)
admin.site.register(Financial)