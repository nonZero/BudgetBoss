from django import forms
from django.shortcuts import render, get_object_or_404, redirect

from expenses.models import Expense


def expense_list(request):
    return render(request, "expenses/expense_list.html", {
        'object_list': Expense.objects.order_by("-date"),
    })


def expense_detail(request, pk):
    o = get_object_or_404(Expense, pk=pk)

    return render(request, "expenses/expense_detail.html", {
        'object': o,
    })


#
# class ContactUsForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     age = forms.IntegerField(required=False)
#     message = forms.CharField(widget=forms.Textarea())

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = "__all__"


def expense_create(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("expenses:list")
    else:
        form = ExpenseForm()
    return render(request, "expenses/expense_form.html", {
        'form': form,
    })
