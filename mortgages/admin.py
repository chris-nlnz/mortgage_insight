from django.contrib import admin

from mortgages.models import Mortgage


class MortgageAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'description', 'amount', 'interest_rate', 'weekly_payment',
        'total_years', 'created_at'
    )
    ordering = ('pk', )
admin.site.register(Mortgage, MortgageAdmin)
