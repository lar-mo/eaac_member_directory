from django.http import HttpResponse
from django.shortcuts import render, reverse
from django.contrib.auth.decorators import login_required

from .models import Member
from .forms import EditMemberInfo

# def index(request):
#     return HttpResponse("Hello world!")

@login_required
def index(request):
    members = Member.objects.all()
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
    # name1.split(' ')[-1]
    # REGEX \b(\w+)$
    members = Member.objects.filter(membership_status='active')
    # members = Member.objects.filter(membership_status='active').order_by('name1')
    # members = Member.objects.filter(membership_status='active').extra(select={'lname1' : "SUBSTR(name1, -1 ,)"}).order_by('lname1')
    print(members)
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
def needs_review(request):
    members = Member.objects.filter(needs_review=1)
    context = {
    'members': members,
    }
    return render(request, 'members/output.html', context)

@login_required
def search_results(request):
    search_term = request.GET['q']
    members = Member.objects.filter(name1__iregex=r'\b{0}\b'.format(search_term)) | Member.objects.filter(name2__iregex=r'\b{0}\b'.format(search_term))
    context = {
    'members': members,
    }
    return render(request, 'members/output.html', context)

@login_required
def edit_member_info(request, member_id):
    print(member_id)
    form = EditMemberInfo()
    member = Member.objects.get(id=member_id)
    context = {'member': member, 'form': form}
    return render(request, 'members/edit_member_info.html', context)

def save_member_info(request):
    # user_info = Member.objects.get(id=request.user.id)
    # user_info.first_name = request.POST['first_name'].strip()
    # user_info.last_name = request.POST['last_name'].strip()
    # user_info.email = request.POST['email'].strip()
    # user_info.save()

    return HttpResponseRedirect(reverse('members_app:index')+'?message=info_saved')
