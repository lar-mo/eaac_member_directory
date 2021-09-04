from django.http import HttpResponse
from django.shortcuts import render, reverse
from django.contrib.auth.decorators import login_required

from .models import Member

# def index(request):
#     return HttpResponse("Hello world!")

@login_required
def index(request):
    members = Member.objects.all().order_by('name1')
    context = {
    'members': members,
    }
    return render(request, 'members/output.html', context)

@login_required
def list_members_grid(request):
    members = Member.objects.all()
    context = {
    'members': members,
    }
    return render(request, 'members/grid.html', context)

@login_required
def list_board(request):
    members = Member.objects.filter(membership_type='board')
    context = {
    'members': members,
    }
    return render(request, 'members/output.html', context)

@login_required
def list_active(request):
    members = Member.objects.filter(membership_status='active')
    context = {
    'members': members,
    }
    return render(request, 'members/output.html', context)

@login_required
def list_inactive(request):
    members = Member.objects.filter(membership_status='inactive')
    context = {
    'members': members,
    }
    return render(request, 'members/output.html', context)

@login_required
def search_results(request):
    search_term = request.GET['q']
    # members_all = Member.objects.all()
    members = Member.objects.filter(name1__iregex=r'\b{0}\b'.format(search_term)) | Member.objects.filter(name2__iregex=r'\b{0}\b'.format(search_term))
    context = {
    'members': members,
    }
    return render(request, 'members/output.html', context)
