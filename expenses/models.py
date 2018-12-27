from django.db import models


# ORM: Object-Relational Mapper
class Expense(models.Model):
    date = models.DateField()
    amount = models.DecimalField(decimal_places=2, max_digits=12)
    title = models.CharField(max_length=300)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"[#{self.id}] {self.title} @{self.date}"

    def is_expensive(self):
        return self.amount > 1000
