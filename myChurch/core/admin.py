from django.contrib import admin
from django.utils.html import format_html
from core.models import Contact,Payment, AccDet

admin.site.register(Contact)
admin.site.register(AccDet)

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'display_image')

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        return '-'

admin.site.register(Payment, PaymentAdmin)