from django.contrib.auth.models import User
import datetime
from accounts.models import Profile
from django.shortcuts import get_list_or_404
import pytz
from django.utils.timezone import make_aware
def royalty_income(username):
    first_level_royalty = False
    second_level_royalty = False
    third_level_royalty = False
    tz = pytz.timezone('Asia/Kolkata')
    date_today  = datetime.datetime.today()
    username = username
    user = User.objects.get(username=username)
    u_prof = Profile.objects.get(user=user)
    if u_prof.activated:
        user_activation_date = u_prof.activated_date
        today = datetime.date.today()
        reqdays_for_r1 = datetime.timedelta(days=10)
        reqdays_for_r2 = datetime.timedelta(days=20)
        reqdays_for_r3 = datetime.timedelta(days=30)
        r1_date = user_activation_date + reqdays_for_r1
        r2_date = user_activation_date + reqdays_for_r2
        r3_date = user_activation_date + reqdays_for_r3
        sponsored_user = u_prof.sponsored_user.all().filter(profile__activated=True)
        sponsored_user_count = sponsored_user.count()
        if user_activation_date >= r1_date and sponsored_user_count >= 10:
            first_level_royalty = True

        if user_activation_date >= r2_date and sponsored_user_count >= 20:
            second_level_royalty = True

        if user_activation_date >= r3_date and sponsored_user_count >= 30:
            third_level_royalty = True
        return {
            'first_level_royalty':first_level_royalty,
            'second_level_royalty':second_level_royalty,
            'third_level_royalty':third_level_royalty
        }



def direct_sponser_user_formula(username):
    username = username
    user = User.objects.get(username=username)
    p = Profile.objects.get(user=user)
    s = p.sponsored_user.filter(profile_user__activated = True)
    total_direct_user = s.exclude(profile_user__activated = False)
    return total_direct_user

def direct_sponser_income(user, *args, **kwargs ):
    lev_one = 0
    lev_two = 0
    lev_three = 0
    lev_four = 0
    lev_five = 0
    lev_six = 0
    lev_seven = 0
    lev_eight = 0
    lev_nine = 0
    lev_ten = 0
    lev_one = direct_sponser_user_formula(user)
    if lev_one:
        for user in lev_one:
            if user:
                lev_two = direct_sponser_user_formula(user)
                for user in lev_two:
                    if user:
                        lev_three = direct_sponser_user_formula(user)
                        for user in lev_three:
                            if user:
                                lev_four = direct_sponser_user_formula(user)
                                for user in lev_four:
                                    if user:
                                        lev_five = direct_sponser_user_formula(user)
                                        for user in lev_five:
                                            if user:
                                                lev_six = direct_sponser_user_formula(user)
                                                for user in lev_six:
                                                    if user:
                                                        lev_seven = direct_sponser_user_formula(user)
                                                        for user in lev_seven:
                                                            lev_eight = direct_sponser_user_formula(user)
                                                            for user in lev_eight:
                                                                if user:
                                                                    lev_nine = direct_sponser_user_formula(user)
                                                                    for user in lev_nine:
                                                                        if user:
                                                                            lev_ten = direct_sponser_user_formula(user)

                        return {
                        'lev_one':lev_one,
                        'lev_two':lev_two,
                        'lev_three':lev_three,
                        'lev_four':lev_four,
                        'lev_five':lev_five,
                        'lev_six': lev_six,
                        'lev_seven':lev_seven,
                        'lev_eight':lev_eight,
                        'lev_nine':lev_nine,
                        'lev_ten':lev_ten,
                         }


def turnover_calculation(date):
    closing_day = datetime.timedelta(days=1)
    yesterday = date.today() - closing_day
    p = Profile.objects.filter(activated_date__date = yesterday)
    total_activated_user = Profile.objects.filter(activated = True)
    yesterday_total_user = p
    yesterday_total_user_count = yesterday_total_user.count()
    return {
    'yesterday_total_user_count':yesterday_total_user_count,
    'yesterday_total_user': yesterday_total_user,
    'total_activated_user':total_activated_user,
     }