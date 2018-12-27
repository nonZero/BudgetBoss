import silly
from django.core.management.base import BaseCommand
import random

from expenses.models import Expense


class Command(BaseCommand):
    help = "Create some silly expenses."

    def add_arguments(self, parser):
        parser.add_argument('n', type=int)

    def handle(self, n, *args, **options):
        for i in range(n):
            o = Expense(
                date=f"20{random.randint(15, 25)}-{random.randint(1,12):02d}-{random.randint(1,25):02d}",
                amount=random.randint(1,20000) / 100,
                title=silly.thing(),
                description="\n".join(silly.paragraph() for i in range(random.randint(1,4)))
            )
            o.save()
