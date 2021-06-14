from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.

@login_required(login_url='/home')
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required(login_url='/home')
def invoice_entry(request):
    return render(request, 'ainvoice_entry.html')

@login_required(login_url='/home')
def view_unapprove_invoice(request):
    return render(request, 'view_unapprove_invoice.html')

@login_required(login_url='/home')
def edit_unapprove_invoice(request):
    return render(request, 'edit_unapprove_invoice.html')

@login_required(login_url='/home')
def invoice_entry_approve(request):
    return render(request, 'invoice_entry_approve.html')

@login_required(login_url='/home')
def cash_entry(request):
    return render(request, 'cash_entry.html')

@login_required(login_url='/home')
def cash_entry_approve(request):
    return render(request, 'cash_entry_approve.html')

@login_required(login_url='/home')
def syn_supplier(request):
    return render(request, 'syn_supplier.html')

@login_required(login_url='/home')
def add_user(request):
    return render(request, 'add_user.html')

@login_required(login_url='/home')
def modify_user(request):
    return render(request, 'modify_user.html')