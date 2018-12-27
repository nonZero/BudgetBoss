from django.shortcuts import render


def expense_list(request):
    return render(request, "expenses/expense_list.html", {
        'xxx': 12345,
        'yyy': ["cookies", "milk", "coffee"],
    })
