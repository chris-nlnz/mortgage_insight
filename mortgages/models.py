from django.db import models
from django.urls import reverse

NULLABLE = {
    'blank': True,
    'null': True
}


# TODO also model house price increase, LVR, equity over time, houses/house types/purpose (investment vs living),
#      rent income offset for investment properties.. maybe model a portfolio even.


class Mortgage(models.Model):
    # TODO uuid as PK?
    description = models.TextField(**NULLABLE)
    amount = models.PositiveIntegerField()
    interest_rate = models.DecimalField(decimal_places=2, max_digits=4)
    weekly_payment = models.DecimalField(decimal_places=2, max_digits=8)
    total_years = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description or '${} at {}% for {} years'.format(
            self.amount, self.interest_rate, self.total_years
        )

    def get_absolute_url(self):
        return reverse('mortgages-detail', args=[str(self.pk)])

