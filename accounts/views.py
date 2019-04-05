from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect, render
from epin.models import Epin
from .models import Profile
import datetime
from django.http import HttpResponse
from .forms import (EpinActivationForm, EpinCreationForm, ProfileUpdateForm,
                    UserRegisterForm, UserUpdateForm)
from .models import Profile
from .payments import direct_sponser_income, royalty_income
from django.shortcuts import get_object_or_404
from django.contrib import messages
from payments.views import sponser_income
from payments.models import DirectSponsorIncome, RoyaltyIncome, SingleLegIncome, Closing, WithdrawlBill, GrandTotal
from posts.models import Message, Notification, Post


def login(request):
    if user.is_authenticated:
        return redirect('profile')
    else:
        if request.method == "POST":
            user = auth.authenticate(
                username=request.POST['username'], password=request.POST['password'])
            if user is not None:
                auth.login(request, user)
                return redirect('profile')
            else:
                return render(request, 'accounts/login.html', {'error': 'Username Or password is incorrect'})
        else:
            return render(request, 'accounts/login.html')

def logout(request):
    if request.method == "POST":
        auth.logout(request)
        return redirect('home')


def register(request):
    referror_name_url = request.GET.get('user')
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            referror_username = form.cleaned_data.get('referror')
            full_name = request.POST.get('full_name')
            u_password = form.cleaned_data.get('password1')
            mobile_no = request.POST.get('mobile_no')
            try:
                r_user = User.objects.get(username=referror_username)
            except User.DoesNotExist:
                r_user = None
            if r_user is None:
                messages.success(
                    request, 'Referror User does not exist please try again')
                return redirect('register')
            else:
                form.save()
                p_referror = Profile.objects.get(user=r_user)
                n_user = User.objects.get(username=username)
                n_profile = Profile.objects.get(user=n_user)
                n_profile.refered_by = r_user
                n_profile.full_name = full_name
                n_profile.user_contact_no = mobile_no
                n_profile.save()
                p_referror.sponsored_user.add(n_user)
                messages.success(request, 'Accounts created Successfully For ' + username +
                                 ' Refered by:-' + referror_username + ' With password :-' + u_password)
                return redirect('user-profile')

        else:
            return render(request, 'accounts/signup.html', {'form': form})
    else:
        if referror_name_url:
            form = UserRegisterForm(initial={'referror': referror_name_url})
        else:
            form = UserRegisterForm()
        return render(request, 'accounts/signup.html', {'form': form})


@login_required
def profile_view(request):
    user = request.user
    u_profile = Profile.objects.get(user=user)
    message = Message.objects.filter(send_to=u_profile)
    total_message_count = message.count()
    notifications = Notification.objects.all()
    total_notifications_count = notifications.count()
    total_user_count = User.objects.all().count
    total_activated_user = Profile.objects.filter(activated=True)
    total_activated_user_count = total_activated_user.count()
    posts = Post.objects.all().order_by('-date')
    return render(request, 'accounts/profile.html', {'u_profile': u_profile, 'message': message,
                                                     'notifications': notifications,
                                                     'total_notifications_count': total_notifications_count,
                                                     'total_message_count': total_message_count,
                                                     'total_activated_user': total_activated_user,
                                                     'total_activated_user_count': total_activated_user_count,
                                                     'total_user_count': total_user_count,
                                                     'posts': posts,
                                                     })


@login_required
def activate_view(request):
    if request.method == 'POST':
        user = request.user
        serial_no = request.POST.get('serial_no')
        try:
            pin = Epin.objects.get(serial_no=serial_no)
        except Epin.DoesNotExist:
            pin = None
        if pin:
            u_profile = Profile.objects.get(user=user)
            if u_profile.activated == False and pin.used == False:
                u_profile.activated = True
                u_profile.activated_date = datetime.datetime.now()
                u_profile.save()
                pin.used_by = user
                pin.used_at = datetime.datetime.now()
                pin.used = True
                pin.save()
                messages.success(request, 'Your account has been activated!!!')
                return redirect('user-profile')
            elif pin.used == True:
                messages.error(
                    request, 'Sorry pin has already been used! Get another pin or try again')
        else:
            messages.error(
                request, 'Sorry Pin doesnot Exists Try again please')
    return render(request, 'accounts/activate.html')


@login_required
def user_settings_veiw(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        u_prof = Profile.objects.get(user=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=u_prof)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('user-profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        u_prof = Profile.objects.get(user=request.user)
        p_form = ProfileUpdateForm(instance=u_prof)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'accounts/user_settings.html', context)


@login_required
def payments_view(request):
    user = request.user
    u_profile = Profile.objects.get(user=user)
    if u_profile.sponsored_user.count() < 1:
        messages.success(
            request, 'Sorry user you should have one direct to start payments')
        return redirect('user-profile')
    elif u_profile.activated == False:
        messages.success(
            request, 'Sorry user you should get your product and epin and, You should activate your account!!')
        return redirect('user-profile')
    else:
        if u_profile.activated == True:
            user = request.user
            username = user.username
            return redirect ('withdraw')
@login_required
def withdraw_view(request):
    user = request.user
    username = user.username
    profile = Profile.objects.get(user=user)
    direct = DirectSponsorIncome.objects.filter(profile=profile).order_by('id')
    a = 0
    for direct_income in direct:
        user_ammount = direct_income.ammount
        total_sponsor_income = a + user_ammount
        a = total_sponsor_income
    royalty = RoyaltyIncome.objects.filter(profile=profile)
    total_sponsor_income = a
    x = 0
    for royalty_income in royalty:
        user_ammount = royalty_income.ammount
        total_royalty_income = x + user_ammount
        x = total_royalty_income
    single_leg = SingleLegIncome.objects.filter(profile=profile)
    total_royalty_income = x
    p = 0
    for user in single_leg:
        user_ammount = user.ammount
        single_leg_income = p + user_ammount
        p = single_leg_income
    single_leg_income = p
    grand_total = single_leg_income + total_sponsor_income + total_royalty_income
    try:
        user_grand_total = GrandTotal.objects.get(profile=profile)
        user_grand_total.total = grand_total
        user_grand_total.save()
    except:
        user_grand_total = GrandTotal(profile=profile)
        user_grand_total.save()

    if request.method == 'POST':
        if not request.POST['ammount']:
            messages.success(request, 'Enter Valid Ammount Please')
            return redirect('withdraw')
        grand = GrandTotal.objects.get(profile=profile)
        p_method = request.POST.get('method')
        p_ammount = request.POST.get('ammount')
        adm_charge = (15 / 100) * int(p_ammount)
        if int(p_ammount) >= 10 and int(p_ammount) <= int(grand_total) - int(grand.withdrawn):
            withdraw_bill = WithdrawlBill(profile=profile)
            total_withdrwan = grand.withdrawn
            withdraw_bill.ammount = int(p_ammount) - adm_charge
            withdraw_bill.method = p_method
            grand_total = grand.total
            grand.withdrawn = int(grand.withdrawn) + int(p_ammount)
            grand.remaining = int(grand.total) - int(grand.withdrawn)
            grand.save()
            withdraw_bill.save()
            return redirect('withdraw')
        elif int(p_ammount) <= int(grand_total) - int(grand.withdrawn):
            messages.success(request, 'You have no money left earn more ')
            return redirect('withdraw')
        else:
            messages.success(request, 'Enter Valid ammount')
    grand = GrandTotal.objects.get(profile=profile)
    withdrawl = WithdrawlBill.objects.filter(profile=profile).order_by('-id')
    context = {
        'royalty': royalty,
        'single_leg': single_leg,
        'direct': direct,
        'single_leg_income': single_leg_income,
        'total_sponsor_income': total_sponsor_income,
        'total_royalty_income': total_royalty_income,
        'grand': grand,
        'withdrawl': withdrawl,
    }
    return render(request, 'accounts/withdraw.html', context)