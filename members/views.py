from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from functools import reduce
from .models import Member
from .forms import EditMemberInfo
from itertools import chain

# def index(request):
#     return HttpResponse("Hello world!")

@login_required
def list_all(request):
    all_members = Member.objects.all()
    paginator = Paginator(all_members, 10)
    page_number = request.GET.get('page')
    members = paginator.get_page(page_number)
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
    board_members = Member.objects.filter(membership_type='Board Member')
    paginator = Paginator(board_members, 10)
    page_number = request.GET.get('page')
    members = paginator.get_page(page_number)
    context = {
        'members': members,
    }
    return render(request, 'members/output.html', context)

@login_required
def list_active(request):
    # name1.split(' ')[-1]
    # REGEX \b(\w+)$
    active_members = Member.objects.filter(membership_status='Active')
    # members = Member.objects.filter(membership_status='active').order_by('name1')
    # members = Member.objects.filter(membership_status='active').extra(select={'lname1' : "SUBSTR(name1, -1 ,)"}).order_by('lname1')
    # print(members)
    paginator = Paginator(active_members, 10)
    page_number = request.GET.get('page')
    members = paginator.get_page(page_number)
    context = {
        'members': members,
    }
    return render(request, 'members/output.html', context)

@login_required
def list_inactive(request):
    inactive_members = Member.objects.filter(membership_status='Inactive')
    paginator = Paginator(inactive_members, 10)
    page_number = request.GET.get('page')
    members = paginator.get_page(page_number)
    context = {
        'members': members,
    }
    return render(request, 'members/output.html', context)

@login_required
def needs_review(request):
    needs_review = Member.objects.filter(needs_review=1)
    paginator = Paginator(needs_review, 10)
    page_number = request.GET.get('page')
    members = paginator.get_page(page_number)
    context = {
        'members': members,
    }
    return render(request, 'members/output.html', context)

@login_required
def search_results(request):
    querystring = request.GET['q']
    two_names_orig = querystring.split("and")
    # two_names_cleaned = [name for name in two_names if name.strip()]
    two_names = []
    for name in two_names_orig:
        two_names.append(name.strip())

    search_terms = querystring.split()
    search_terms = list(dict.fromkeys(search_terms))
    try:
        search_terms.remove('and')
    except:
        pass
    # print(search_terms)
    # print(two_names)

    exact_match = Member.objects.filter(name1=querystring)
    members_name1 = Member.objects.filter(reduce(Q.__or__, [Q(name1__icontains=word) for word in two_names]))
    members_name2 = Member.objects.filter(reduce(Q.__or__, [Q(name2__icontains=word) for word in two_names]))

    # print(exact_match.exists())
    # print(members_name1.exists())
    # print(members_name2.exists())

    if exact_match.exists():
        context = {
            'members': exact_match,
        }
        return render(request, 'members/output.html', context)
    elif members_name1.exists() or members_name2.exists():
        members = list(dict.fromkeys(chain(members_name1, members_name2)))
        context = {
            'members': members,
        }
        return render(request, 'members/output.html', context)
    else:
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
    context = {
        'member': member,
        'form': form
    }
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
