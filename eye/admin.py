from django.contrib import admin
from eye.models import Stock, Info, Cashflow
from import_export import resources

admin.site.register(Stock)
admin.site.register(Info)
admin.site.register(Cashflow)