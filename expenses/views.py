from django.http import JsonResponse, Http404
from django.shortcuts import render, get_object_or_404

from expenses.models import Expense


def expense_list(request):
    return render(request, "expenses/expense_list.html", {
        'object_list': Expense.objects.all(),
    })

def expense_detail(request, pk):
    # try:
    #     o = Expense.objects.get(pk=pk)
    # except Expense.DoesNotExist:
    #     raise Http404()
    o = get_object_or_404(Expense, pk=pk)

    return render(request, "expenses/expense_detail.html", {
        'object': o,
    })
