from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.

@login_required(login_url='/home')
def mdashboard(request):
    return render(request, 'mdashboard.html')

@login_required(login_url='/home')
def minvoice_entry(request):
    return render(request, 'minvoice_entry.html')

@login_required(login_url='/home')
def mview_unapprove_invoice(request):
    return render(request, 'mview_unapprove_invoice.html')

@login_required(login_url='/home')
def medit_unapprove_invoice(request):
    return render(request, 'medit_unapprove_invoice.html')

@login_required(login_url='/home')
def minvoice_entry_approve(request):
    return render(request, 'minvoice_entry_approve.html')

@login_required(login_url='/home')
def mcash_entry(request):
    return render(request, 'mcash_entry.html')

@login_required(login_url='/home')
def mcash_entry_approve(request):
    return render(request, 'mcash_entry_approve.html')

@login_required(login_url='/home')
def msyn_supplier(request):
    return render(request, 'msyn_supplier.html')