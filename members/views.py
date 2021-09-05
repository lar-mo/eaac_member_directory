from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse
from django.contrib.auth.decorators import login_required

from django.db.models import Q
from functools import reduce
from .models import Member
from .forms import EditMemberInfo
from itertools import chain

# def index(request):
#     return HttpResponse("Hello world!")

@login_required
def list_all(request):
    members = Member.objects.all()
    context = {
    'members': members,
    }
    return render(request, 'members/output.html', context)

@login_required
def list_all_grid(request):
    members = Member.objects.all()
    context = {
    'members': members,
    }
    return render(request, 'members/grid.html', context)

@login_required
def list_board(request):
    members = Member.objects.filter(membership_type='Board Member')
    context = {
    'members': members,
    }
    return render(request, 'members/output.html', context)

@login_required
def list_active(request):
    # name1.split(' ')[-1]
    # REGEX \b(\w+)$
    members = Member.objects.filter(membership_status='Active')
    # members = Member.objects.filter(membership_status='active').order_by('name1')
    # members = Member.objects.filter(membership_status='active').extra(select={'lname1' : "SUBSTR(name1, -1 ,)"}).order_by('lname1')
    # print(members)
    context = {
    'members': members,
    }
    return render(request, 'members/output.html', context)

@login_required
def list_inactive(request):
    members = Member.objects.filter(membership_status='Inactive')
    context = {
    'members': members,
    }
    return render(request, 'members/output.html', context)

@login_required
def needs_review(request):
    members = Member.objects.filter(needs_review=1)
    context = {
    'members': members,
    }
    return render(request, 'members/output.html', context)

@login_required
def search_results(request):
    search_terms = request.GET['q'].split()
    search_terms = list(dict.fromkeys(search_terms))
    try:
        search_terms.remove('and')
    except:
        pass
    print(search_terms)
    members_name1 = Member.objects.filter(reduce(Q.__or__, [Q(name1__icontains=word) for word in search_terms]))
    members_name2 = Member.objects.filter(reduce(Q.__or__, [Q(name2__icontains=word) for word in search_terms]))
    members = list(dict.fromkeys(chain(members_name1, members_name2)))
    context = {
        'members': members,
    }
    return render(request, 'members/output.html', context)

@login_required
def show_member_info(request, member_id):
    message = request.GET.get('message', '')
    member = Member.objects.filter(id=member_id)
    context = {
    'members': member,
    'message': message,
    }
    return render(request, 'members/output.html', context)

@login_required
def edit_member_info(request, member_id):
    form = EditMemberInfo()
    member = Member.objects.get(id=member_id)
    context = {'member': member, 'form': form}
    return render(request, 'members/edit_member_info.html', context)

def save_member_info(request):
    member_id = request.POST['member_id']
    # print(request.POST)
    member_info = Member.objects.get(id=member_id)
    member_info.name1 = request.POST['name1'].strip()
    member_info.sort_by = request.POST['sort_by'].strip()
    member_info.byline = request.POST['byline'].strip()
    member_info.name2 = request.POST['name2'].strip()
    member_info.note = request.POST['note'].strip()
    member_info.address1 = request.POST['address1'].strip()
    member_info.address2 = request.POST['address2'].strip()
    member_info.city = request.POST['city'].strip()
    member_info.state = request.POST['state'].strip()
    member_info.postal_code = request.POST['postal_code'].strip()
    member_info.email1 = request.POST['email1'].strip()
    member_info.email2 = request.POST['email2'].strip()
    member_info.phone_number1 = request.POST['phone_number1'].strip()
    member_info.phone_number2 = request.POST['phone_number2'].strip()
    member_info.membership_status = request.POST['membership_status']
    member_info.membership_type = request.POST['membership_type']
    try:
        member_info.role = request.POST['role'].strip()
    except:
        pass
    try:
        member_info.directory_optout = request.POST['directory_optout']
    except:
        pass
    try:
        member_info.needs_review = request.POST['needs_review']
    except:
        pass
    member_info.reason_for_review = request.POST['reason_for_review'].strip()
    member_info.save()

    return HttpResponseRedirect(reverse('members_app:show_member_info', kwargs={'member_id':member_id})+'?message=changes_saved')
