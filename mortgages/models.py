import math
import uuid
from decimal import Decimal, ROUND_HALF_UP

from django.db import models
from django.urls import reverse


NULLABLE = {
    'blank': True,
    'null': True
}


def _decimal_and_round_to_two(number):
    return Decimal(number).quantize(Decimal('.01'), rounding=ROUND_HALF_UP)

# TODO also model house price increase, LVR, equity over time, houses/house types/purpose (investment vs living),
#      rent income offset for investment properties.. maybe model a portfolio even.


class Mortgage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.TextField(**NULLABLE)
    principal = models.PositiveIntegerField()
    effective_annual_interest_rate = models.DecimalField(decimal_places=2, max_digits=4)
    term = models.PositiveIntegerField(help_text="Total term of the loan, in years")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description or '${} at {}% for {} years'.format(
            self.principal, self.effective_annual_interest_rate, self.term
        )

    def get_absolute_url(self):
        return reverse('mortgages-detail', args=[str(self.pk)])

    @property
    def annual_interest_as_multiplier(self):
        return self.effective_annual_interest_rate / Decimal(100.0)

    def interest_rate_per_period(self, periods_per_year):
        return self.annual_interest_as_multiplier / Decimal(periods_per_year)

    def periodic_payments(self, periods_per_year):
        interest_rate_per_period = self.interest_rate_per_period(periods_per_year)
        total_periods = periods_per_year*self.term
        x = Decimal(1 + interest_rate_per_period) ** Decimal(total_periods)
        return Decimal(
            self.principal * (interest_rate_per_period * x) / (x - 1)
        ).quantize(Decimal('.01'), rounding=ROUND_HALF_UP)

    @property
    def weekly_payments(self):
        return self.periodic_payments(periods_per_year=52.0)

    @property
    def fortnightly_payments(self):
        return self.periodic_payments(periods_per_year=26.0)

    @property
    def monthly_payments(self):
        return self.periodic_payments(periods_per_year=12.0)

    def amortization_schedule(self, periods_per_year=52):
        """
        Calculates an amortization schedule. Periods per year indicates
        the frequency of payments (52 for weekly, 26 for fortnightly,
        12 for monthly, etc).

        :param periods_per_year: frequency of payments (52 for weekly, 26 for fortnightly, etc).
        :return:
        """
        schedule = []
        repayment_per_period = self.periodic_payments(periods_per_year)
        interest_rate_per_period = self.interest_rate_per_period(periods_per_year)
        total_number_of_payments = self.term * periods_per_year
        index = 1
        balance = self.principal
        while index <= total_number_of_payments:
            interest_component = balance * interest_rate_per_period
            principal_component = repayment_per_period - interest_component
            balance -= principal_component

            readable_index = "Year {}, period {}".format(
                math.floor(index / periods_per_year), index % periods_per_year
            )

            schedule.append((
                index,
                readable_index,
                _decimal_and_round_to_two(repayment_per_period),
                _decimal_and_round_to_two(interest_component),
                _decimal_and_round_to_two(principal_component),
                _decimal_and_round_to_two(max(balance, 0)),
            ))
            index += 1
        return schedule

    def print_tabulated_amortization_schedule(self, periods_per_year=52):
        from tabulate import tabulate
        print(tabulate(
            self.amortization_schedule(periods_per_year),
            headers=["Payment", "Date", "Amount", "Interest", "Principal", "Balance"],
            floatfmt=",.2f",
            numalign="right"
        ))

