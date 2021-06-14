from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.


@login_required(login_url='/home')
def udashboard(request):
    return render(request, 'udashboard.html')

@login_required(login_url='/home')
def uinvoice_entry(request):
    return render(request, 'uinvoice_entry.html')

@login_required(login_url='/home')
def uview_unapprove_invoice(request):
    return render(request, 'uview_unapprove_invoice.html')

@login_required(login_url='/home')
def uedit_unapprove_invoice(request):
    return render(request, 'uedit_unapprove_invoice.html')

@login_required(login_url='/home')
def ucash_entry(request):
    return render(request, 'ucash_entry.html')

@login_required(login_url='/home')
def usyn_supplier(request):
    return render(request, 'usyn_supplier.html')