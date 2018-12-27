from django.test import TestCase

from expenses.models import Expense


class ExpensesTestCase(TestCase):
    def test_expense(self):
        self.assertEqual(Expense.objects.count(), 0)

        e = Expense(
            date="2018-10-23",
            amount="12.45",
            title="Pizza",
            description="Exceellent cheese and mushrooms...."
        )
        e.save()

        self.assertEqual(Expense.objects.count(), 1)



