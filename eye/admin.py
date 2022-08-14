from django.contrib import admin
from eye.models import Stock, Info, Financial, Portfolio, History

admin.site.register(Stock)
admin.site.register(Info)
admin.site.register(Financial)
admin.site.register(Portfolio)
admin.site.register(History)