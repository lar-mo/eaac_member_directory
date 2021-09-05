from django.db import models
from django.contrib.auth.models import User

def all_member_count(user):
    number_of_all_members = Member.objects.count()
    return number_of_all_members
User.add_to_class('all_member_count', all_member_count)

def board_member_count(user):
    number_of_board_members = Member.objects.filter(membership_type='board').count()
    return number_of_board_members
User.add_to_class('board_member_count', board_member_count)

def active_member_count(user):
    number_of_active_members = Member.objects.filter(membership_status='active').count()
    return number_of_active_members
User.add_to_class('active_member_count', active_member_count)

def inactive_member_count(user):
    number_of_inactive_members = Member.objects.filter(membership_status='inactive').count()
    return number_of_inactive_members
User.add_to_class('inactive_member_count', inactive_member_count)

def needs_review_count(user):
    number_of_needs_review = Member.objects.filter(needs_review=1).count()
    return number_of_needs_review
User.add_to_class('needs_review_count', needs_review_count)

class Member(models.Model):
    name1               = models.CharField(max_length=100)
    sort_by             = models.CharField(max_length=100)
    byline              = models.CharField(max_length=200, blank=True)
    name2               = models.CharField(max_length=100, blank=True)
    note                = models.CharField(max_length=100, blank=True)
    phone_number1       = models.CharField(max_length=100, blank=True)
    phone_number2       = models.CharField(max_length=100, blank=True)
    address1            = models.CharField(max_length=200, blank=True)
    address2            = models.CharField(max_length=200, blank=True)
    city                = models.CharField(max_length=100, blank=True)
    state               = models.CharField(max_length=30, blank=True)
    postal_code         = models.CharField(max_length=10, blank=True)
    email1              = models.CharField(max_length=200, blank=True)
    email2              = models.CharField(max_length=200, blank=True)
    ACTIVE = 'active'
    INACTIVE = 'inactive'
    MEMBERSHIP_STATUS_CHOICES = [
        (ACTIVE, 'active'),
        (INACTIVE, 'inactive'),
    ]
    membership_status = models.CharField(
        max_length=10,
        choices=MEMBERSHIP_STATUS_CHOICES,
        default=ACTIVE,
        blank=True,
    )
    SUPPORTER = 'supporter'
    VOLUNTEER = 'volunteer'
    HONORARY = 'honorary'
    PAM_STAFF = 'PAM staff'
    BOARD = 'board'
    MEMBER_TYPE_CHOICES = [
        (SUPPORTER, 'supporter'),
        (VOLUNTEER, 'volunteer'),
        (HONORARY, 'honorary'),
        (PAM_STAFF, 'PAM staff'),
        (BOARD, 'board'),
    ]
    membership_type = models.CharField(
        max_length=10,
        choices=MEMBER_TYPE_CHOICES,
        default=SUPPORTER,
        blank=True,
    )
    role                = models.CharField(max_length=200, blank=True)
    directory_optout    = models.BooleanField(default=False)
    needs_review        = models.BooleanField(default=False)
    reason_for_review   = models.CharField(max_length=200, blank=True)

    class Meta:
        ordering = ['sort_by',]

    def __str__(self):
        output = self.name1
        if self.name2 != '':
            output += ' and ' + self.name2
        return output
