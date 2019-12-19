from django.contrib import admin

from mortgages.models import Mortgage


class MortgageAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'description', 'principal', 'effective_annual_interest_rate', 'term',
        'weekly_payments', 'created_at'
    )
    ordering = ('pk', )


admin.site.register(Mortgage, MortgageAdmin)
