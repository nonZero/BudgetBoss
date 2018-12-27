from django import forms
from django.shortcuts import render, get_object_or_404

from expenses.models import Expense


def expense_list(request):
    return render(request, "expenses/expense_list.html", {
        'object_list': Expense.objects.all(),
    })


def expense_detail(request, pk):
    o = get_object_or_404(Expense, pk=pk)

    return render(request, "expenses/expense_detail.html", {
        'object': o,
    })


class ContactUsForm(forms.Form):
    name = forms.CharField(max_length=100)
    age = forms.IntegerField(required=False)
    message = forms.CharField(widget=forms.Textarea())


def expense_create(request):
    if request.method == "POST":
        form = ContactUsForm(request.POST)
        if form.is_valid():
            assert False, form.cleaned_data

    form = ContactUsForm()
    return render(request, "expenses/expense_form.html", {
        'form': form,
    })
