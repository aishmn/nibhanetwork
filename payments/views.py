from django.shortcuts import render, redirect
from accounts.models import Profile
# from datetime import datetime
from django.contrib.auth.models import User
import datetime
from accounts.models import Profile
from django.shortcuts import get_list_or_404
import pytz
from django.core.exceptions import ObjectDoesNotExist
from django.utils.timezone import make_aware
from .models import Closing
from django.contrib import messages
from .models import SingleLegIncome, RoyaltyIncome, DirectSponsorIncome, WithdrawlBill
from django.contrib.auth.decorators import login_required
from payments.models import DirectSponsorIncome
from epin.models import Epin

def direct_sponser_user_formula(username):
	user = User.objects.get(username=username)
	p = Profile.objects.get(user=user)
	s = p.sponsored_user.filter(profile_user__activated = True)
	total_direct_user = s
	return total_direct_user
def sponser_income(username):
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
	username = username
	lev_one = direct_sponser_user_formula(username)
	main_user_user = User.objects.get(username = username)
	main_user_profile = Profile.objects.get(user = main_user_user )
	if lev_one:
		for user in lev_one:
			u1_profile = Profile.objects.get(user = user)
			d1_income, created = DirectSponsorIncome.objects.get_or_create(profile=main_user_profile, level = 'level_one')
			if d1_income:
				d1_income.users.add(u1_profile)
				d1_income.total_users = d1_income.users.all().count()
				d1_income.ammount =  d1_income.total_users * 50
				d1_income.save()
			lev_two_user = d1_income.users.all()
			for user in lev_two_user:
				username = user.user.username
				lev_two = direct_sponser_user_formula(username)
				if lev_two:
					for user in lev_two:
						u2_profile = Profile.objects.get(user = user)
						d2_income, created = DirectSponsorIncome.objects.get_or_create(profile=main_user_profile, level = 'level_two')
						if d2_income:
							d2_income.users.add(u2_profile)
							d2_income.total_users = d2_income.users.all().count()
							d2_income.ammount =  d2_income.total_users * 10
							d2_income.save()
						lev_three_user = d2_income.users.all()
						for user in lev_three_user:
							username = user.user.username
							lev_three = direct_sponser_user_formula(username)
							if lev_three:
								for user in lev_three:
									u3_profile = Profile.objects.get(user = user)
									d3_income, created = DirectSponsorIncome.objects.get_or_create(profile=main_user_profile, level = 'level_three')
									if d3_income:
										d3_income.users.add(u3_profile)
										d3_income.total_users = d3_income.users.all().count()
										d3_income.ammount =  d3_income.total_users * 9
										d3_income.save()
									lev_four_user = d3_income.users.all()
									for user in lev_four_user:
										username = user.user.username
										lev_four = direct_sponser_user_formula(username)
										if lev_four:
											for user in lev_four:
												u4_profile = Profile.objects.get(user = user)
												d4_income, created = DirectSponsorIncome.objects.get_or_create(profile=main_user_profile, level = 'level_four')
												if d4_income:
													d4_income.users.add(u4_profile)
													d4_income.total_users = d4_income.users.all().count()
													d4_income.ammount =  d4_income.total_users * 8
													d4_income.save()
												lev_five_user = d4_income.users.all()
												for user in lev_five_user:
													username = user.user.username
													lev_five = direct_sponser_user_formula(username)
													if lev_five:
														for user in lev_five:
															u5_profile = Profile.objects.get(user = user)
															d5_income, created = DirectSponsorIncome.objects.get_or_create(profile=main_user_profile, level = 'level_five')
															if d5_income:
																d5_income.users.add(u5_profile)
																d5_income.total_users = d5_income.users.all().count()
																d5_income.ammount =  d5_income.total_users * 7
																d5_income.save()
															lev_six_user = d5_income.users.all()
															for user in lev_six_user:
																username = user.user.username
																lev_six = direct_sponser_user_formula(username)
																if lev_six:
																	for user in lev_six:
																		u6_profile = Profile.objects.get(user = user)
																		d6_income, created = DirectSponsorIncome.objects.get_or_create(profile=main_user_profile, level = 'level_six')
																		if d6_income:
																			d6_income.users.add(u6_profile)
																			d6_income.total_users = d6_income.users.all().count()
																			d6_income.ammount =  d6_income.total_users * 5
																			d6_income.save()
																		lev_seven_user = d6_income.users.all()
																		for user in lev_seven_user:
																			username = user.user.username
																			lev_seven = direct_sponser_user_formula(username)
																			if lev_seven:
																				for user in lev_seven:
																					u7_profile = Profile.objects.get(user = user)
																					d7_income, created = DirectSponsorIncome.objects.get_or_create(profile=main_user_profile, level = 'level_seven')
																					if d7_income:
																						d7_income.users.add(u7_profile)
																						d7_income.total_users = d7_income.users.all().count()
																						d7_income.ammount =  d7_income.total_users * 3
																						d7_income.save()
																					lev_eight_user = d7_income.users.all()
																					for user in lev_eight_user:
																						username = user.user.username
																						lev_eight = direct_sponser_user_formula(username)
																						if lev_eight:
																							for user in lev_eight:
																								u8_profile = Profile.objects.get(user = user)
																								d8_income, created = DirectSponsorIncome.objects.get_or_create(profile=main_user_profile, level = 'level_eight')
																								if d8_income:
																									d8_income.users.add(u8_profile)
																									d8_income.total_users = d8_income.users.all().count()
																									d8_income.ammount =  d8_income.total_users * 3
																									d8_income.save()
																								lev_nine_user = d8_income.users.all()
																								for user in lev_nine_user:
																									username = user.user.username
																									lev_nine = direct_sponser_user_formula(username)
																									if lev_nine:
																										for user in lev_nine:
																											u9_profile = Profile.objects.get(user = user)
																											d9_income, created = DirectSponsorIncome.objects.get_or_create(profile=main_user_profile, level = 'level_nine')
																											if d9_income:
																												d9_income.users.add(u9_profile)
																												d9_income.total_users = d9_income.users.all().count()
																												d9_income.ammount =  d9_income.total_users * 3
																												d9_income.save()
																											lev_ten_user = d9_income.users.all()
																											for user in lev_ten_user:
																												username = user.user.username
																												lev_ten = direct_sponser_user_formula(username)

																												if lev_ten:
																													for user in lev_ten:
																														u10_profile = Profile.objects.get(user = user)
																														d10_income, created = DirectSponsorIncome.objects.get_or_create(profile=main_user_profile, level = 'level_ten')
																														if d10_income:
																															d10_income.users.add(u10_profile)
																															d10_income.total_users = d10_income.users.all().count()
																															d10_income.ammount =  d10_income.total_users * 2
																															d10_income.save()







def turnover_userinfo(request):
	closing_day = datetime.timedelta(days=1)
	yesterday = datetime.datetime.now() - closing_day
	p = Profile.objects.filter(activated_date__date = yesterday)
	total_activated_user = Profile.objects.filter(activated=True).order_by('-activated_date')
	yesterday_total_user = p
	yesterday_total_user_count = yesterday_total_user.count()
	return {
		'yesterday_total_user_count':yesterday_total_user_count,
		'yesterday_total_user': yesterday_total_user,
		'total_activated_user':total_activated_user,
     	}

def royalty_income(user, closing_total_ammount):
	user = user
	username = user.username
	tprofileoday = datetime.datetime.today()
	u_profile = Profile.objects.get(user=user)
	user_activated_date = u_profile.activated_date.date()
	today = datetime.datetime.today()
	today_date = today.date()
	try:
		level_one_user= DirectSponsorIncome.objects.get(profile=u_profile, level = 'level_one')
		total_direct = level_one_user.total_users
	except DirectSponsorIncome.DoesNotExist:
		total_direct = 0
	total_activated_user = Profile.objects.filter(activated=True).order_by('activated_date')
	total_activated_user_count = total_activated_user.count()
	b = datetime.timedelta(days=10)
	if today_date >= user_activated_date + b and total_direct >= 10:
		try:
			r1_income = RoyaltyIncome.objects.get(profile = u_profile, level='level_one')
			r1_income_ammount = r1_income.ammount
		except:
			r1_income = RoyaltyIncome(profile = u_profile, level='level_one')
			r1_income_ammount = 0
		level_ammount = 3/100 * closing_total_ammount
		r1_income.level = 'level_one'
		a = level_ammount / total_activated_user_count
		r1_income.ammount = r1_income_ammount + a
		r1_income.withdrawl_ammount = 0
		r1_income.save()
	d = datetime.timedelta(days=20)
	if today_date >= user_activated_date + b and total_direct >= 20:
		try:
			r2_income = RoyaltyIncome.objects.get(profile = u_profile, level='level_two')
			r2_income_ammount = r2_income.ammount
		except RoyaltyIncome.DoesNotExist:
			r2_income = RoyaltyIncome(profile = u_profile, level='level_two')
			r2_income_ammount = 0
		level_ammount = 4/100 * closing_total_ammount
		a = level_ammount / total_activated_user_count
		r2_income.ammount = r2_income_ammount + a
		r2_income.withdrawl_ammount = 0
		r2_income.save()
	e = datetime.timedelta(days=30)
	if today_date >= user_activated_date + e and total_direct >= 30:
		try:
			r3_income = RoyaltyIncome.objects.get(profile = u_profile, level='level_three')
			r3_income_ammount = r2_income.ammount
		except:
			r3_income = RoyaltyIncome(profile = u_profile, level='level_three')
			r3_income_ammount = 0
		level_ammount = 5/100 * closing_total_ammount
		a = level_ammount / total_activated_user_count
		r3_income.ammount = r3_income_ammount + a
		r3_income.withdrawl_ammount = 0
		r3_income.save()

@login_required
def do_closing_view(request):
	login_user = request.user
	if login_user.is_superuser:
		if request.method == 'POST':
			n_value = 'ABC'
			value = request.POST.get('value')
			if value == n_value:
				t_date = datetime.datetime.today()
				p = turnover_userinfo(request)
				yesterday_total_user_count = p['yesterday_total_user_count']
				yesterday_total_user = p['yesterday_total_user']
				total_activated_user = p['total_activated_user']
				if yesterday_total_user_count >= 1:
					closing_total_user = yesterday_total_user_count
					closing_total_ammount = closing_total_user * 1000
					closing = Closing(date=t_date)
					closing.total_user = closing_total_user
					closing.ammount = closing_total_ammount
					closing.save()
					closing_level_percentage = 5/100 * closing_total_ammount
					i = 0
					for user in total_activated_user:
						if user.sponsored_user.all().count() >= 1:
							sponser_income(user.user.username)
							i = i + 1
					total_activated_user_with_one_direct = i
					for user in total_activated_user:
						r = royalty_income(user.user, closing_total_ammount)
					if total_activated_user.count() <= 99:
						for user in total_activated_user.reverse()[:99]:
							if user.sponsored_user.all().count() >= 1:
								s_income , created = SingleLegIncome.objects.get_or_create(profile = user, level = 'level_one')
								a = closing_level_percentage / total_activated_user_with_one_direct
								if s_income.ammount is None:
									s_ammount = 0
								else:
									s_ammount = s_income.ammount
								s_income.ammount = a + s_ammount
								s_income.paid = False
								s_income.date = datetime.date.today()
								s_income.withdrawl_ammount = 0
								s_income.save()

					if total_activated_user.count() >= 99 and total_activated_user.count() <= 999:
						for user in total_activated_user.reverse()[100:999]:
							if user.sponsored_user.all().count() >= 1:
								s2_income , created = SingleLegIncome.objects.get_or_create(profile = user, level = 'level_two')
								a = closing_level_percentage / total_activated_user.count()
								if s_income.ammount is None:
									s_ammount = 0
								else:
									s_ammount = s_income.ammount
								s2_income.ammount = a + s2_ammount
								s2_income.paid = False
								s2_income.date = datetime.date.today()
								s2_income.withdrawl_ammount = 0
								s2_income.save()

					if total_activated_user.count() >= 999 and total_activated_user.count() <= 4999:
						for user in total_activated_user.reverse()[999:4999]:
							try:
								s3_income = SingleLegIncome.objects.get(profile=user, level = 'level_three')
								s3_ammount = s3_income.ammount
							except:
								s3_income = SingleLegIncome(profile=user, level = 'level_three')
								s3_ammount = 0
							a = closing_level_percentage / total_activated_user.count()
							s3_income.ammount = a + s3_ammount
							s3_income.paid = False
							s3_income.date = datetime.date.today()
							s3_income.withdrawl_ammount = 0
							s3_income.save()

					if total_activated_user.count() >= 4999 and total_activated_user.count() <= 9999:
						for user in total_activated_user.reverse()[4999:9999]:
							try:
								s4_income = SingleLegIncome.objects.get(profile=user, level = 'level_four')
								s4_ammount = s4_income.ammount
							except:
								s4_income = SingleLegIncome(profile=user, level = 'level_four')
								s4_ammount = 0
							a = closing_level_percentage / total_activated_user.count()
							s4_income.ammount = a + s4_ammount
							s4_income.paid = False
							s4_income.date = datetime.date.today()
							s4_income.withdrawl_ammount = 0
							s4_income.save()

					if total_activated_user.count() >= 9999 and total_activated_user.count() <= 19999:
						for user in total_activated_user.reverse()[9999:19999]:
							try:
								s5_income = SingleLegIncome.objects.get(profile=user, level = 'level_five')
								s5_ammount = s5_income.ammount
							except:
								s5_income = SingleLegIncome(profile=user, level = 'level_five')
								s5_ammount = 0
							a = closing_level_percentage / total_activated_user.count()
							s5_income.ammount = a + s5_ammount
							s5_income.paid = False
							s5_income.date = datetime.date.today()
							s5_income.withdrawl_ammount = 0
							s5_income.save()
					if total_activated_user.count() >= 19999 and total_activated_user.count() <= 39999:
						for user in total_activated_user.reverse()[19999:39999]:
							try:
								s6_income = SingleLegIncome.objects.get(profile=user, level = 'level_six')
								s6_ammount = s6_income.ammount
							except:
								s6_income = SingleLegIncome(profile=user, level = 'level_six')
								s6_ammount = 0
							a = closing_level_percentage / total_activated_user.count()
							s6_income.ammount = a + s6_ammount
							s6_income.paid = False
							s6_income.date = datetime.date.today()
							s6_income.withdrawl_ammount = 0
							s6_income.save()
					if total_activated_user.count() >= 39999 and total_activated_user.count() <= 59999:
						for user in total_activated_user.reverse()[39999:59999]:
							try:
								s7_income = SingleLegIncome.objects.get(profile=user, level = 'level_seven')
								s7_ammount = s7_income.ammount
							except:
								s7_income = SingleLegIncome(profile=user, level = 'level_seven')
								s7_ammount = 0
							a = closing_level_percentage / total_activated_user.count()
							s7_income.ammount = a + s7_ammount
							s7_income.paid = False
							s7_income.date = datetime.date.today()
							s7_income.withdrawl_ammount = 0
							s7_income.save()
					if total_activated_user.count() >= 59999 and total_activated_user.count() <= 79999:
						for user in total_activated_user.reverse()[59999:79999]:
							try:
								s8_income = SingleLegIncome.objects.get(profile=user, level = 'level_eight')
								s8_ammount = s3_income.ammount
							except:
								s8_income = SingleLegIncome(profile=user, level = 'level_eight')
								s8_ammount = 0
							a = closing_level_percentage / total_activated_user.count()
							s8_income.ammount = a + s8_ammount
							s8_income = SingleLegIncome(profile=user)
							s8_income.paid = False
							s8_income.date = datetime.date.today()
							s8_income.withdrawl_ammount = 0
							s8_income.save()
					if total_activated_user.count() >= 79999 and total_activated_user.count() <= 99999:
						for user in total_activated_userreverse()[79999:99999]:
							try:
								s9_income = SingleLegIncome.objects.get(profile=user, level = 'level_nine')
								s9_ammount = s3_income.ammount
							except:
								s9_income = SingleLegIncome(profile=user, level = 'level_nine')
								s9_ammount = 0
							a = closing_level_percentage / total_activated_user.count()
							s9_income.ammount = a + s9_ammount
							s9_income.paid = False
							s9_income.date = datetime.date.today()
							s9_income.withdrawl_ammount = 0
							s9_income.save()
					if total_activated_user.count() >= 99999 and total_activated_user.count() <= 119999:
						for user in total_activated_user.reverse()[99999:119999]:
							try:
								s10_income = SingleLegIncome.objects.get(profile=user, level = 'level_ten')
								s10_ammount = s10_income.ammount
							except:
								s10_income = SingleLegIncome(profile=user, level = 'level_ten')
								s10_ammount = 0
							a = closing_level_percentage / total_activated_user.count()
							s10_income.ammount = a + s10_ammount
							s10_income = SingleLegIncome(profile=user)
							s10_income.paid = False
							s10_income.date = datetime.date.today()
							s10_income.withdrawl_ammount = 0
							s10_income.save()
					if total_activated_user.count() >= 119999 and total_activated_user.count() <= 139999:
						for user in total_activated_user.reverse()[119999:139999]:
							try:
								s11_income = SingleLegIncome.objects.get(profile=user, level = 'level_eleven')
								s11_ammount = s11_income.ammount
							except:
								s11_income = SingleLegIncome(profile=user, level = 'level_eleven')
								s11_ammount = 0
							a = closing_level_percentage / total_activated_user.count()
							s11_income.ammount = a + s11_ammount
							s11_income = SingleLegIncome(profile=user)
							s11_income.paid = False
							s11_income.date = datetime.date.today()
							s11_income.withdrawl_ammount = 0
							s11_income.save()
					if total_activated_user.count() >= 139999 and total_activated_user.count() <= 159999:
						for user in total_activated_user.reverse()[139999:159999]:
							try:
								s12_income = SingleLegIncome.objects.get(profile=user, level = 'level_twelve')
								s12_ammount = s12_income.ammount
							except:
								s12_income = SingleLegIncome(profile=user, level = 'level_twelve')
								s12_ammount = 0
							a = closing_level_percentage / total_activated_user.count()
							s12_income.ammount = a + s12_ammount
							s12_income.paid = False
							s12_income.date = datetime.date.today()
							s12_income.withdrawl_ammount = 0
							s12_income.save()
					if total_activated_user.count() >= 159999 and total_activated_user.count() <= 179999:
						for user in total_activated_suser.reverse()[159999:179999]:
							try:
								s13_income = SingleLegIncome.objects.get(profile=user, level = 'level_thirteen')
								s13_ammount = s13_income.ammount
							except:
								s13_income = SingleLegIncome(profile=user, level = 'level_thirteen')
								s13_ammount = 0
							a = closing_level_percentage / total_activated_user.count()
							s13_income.ammount = a + s13_ammount
							s13_income.paid = False
							s13_income.date = datetime.date.today()
							s13_income.withdrawl_ammount = 0
							s13_income.save()
					if total_activated_user.count() >= 179999 and total_activated_user.count() <= 199999:
						for user in total_activated_user.reverse()[179999:199999]:
							try:
								s14_income = SingleLegIncome.objects.get(profile=user, level = 'level_fourteen')
								s14_ammount = s14_income.ammount
							except:
								s14_income = SingleLegIncome(profile=user, level = 'level_fourteen')
								s14_ammount = 0
							a = closing_level_percentage / total_activated_user.count()
							s14_income.ammount = a + s14_ammount
							s14_income.paid = False
							s14_income.date = datetime.date.today()
							s14_income.withdrawl_ammount = 0
							s14_income.save()
					if total_activated_user.count() == 200000:
						for user in total_activated_userreverse()[19999:200000]:
							try:
								s15_income = SingleLegIncome.objects.get(profile=user, level = 'level_fifteen')
								s15_ammount = s15_income.ammount
							except:
								s15_income = SingleLegIncome(profile=user, level = 'level_fifteen')
								s15_ammount = 0
							a = closing_level_percentage / total_activated_user.count()
							s15_income.ammount = a + s15_ammount
							s15_income.paid = False
							s15_income.date = datetime.date.today()
							s15_income.withdrawl_ammount = 0
							s15_income.save()
					messages.success(request, 'Ammount Distrubated')
					messages.success(request, 'Todays Closing Done Succesfully !! Great luck ')
					return redirect('do-closing')
				elif p['yesterday_total_user_count'] <= 1:
					messages.success(request, 'Closing Cant be done with Zero User')
					return redirect('do-closing')
			else:
				messages.error(request, 'You Entered It wrong Please Try again')
				return redirect('do-closing')
		return render(request,'payments/do-closing.html')
	else:
		messages.error(request, 'You are not a super user !!!!')
		return redirect('home')


def payments_management_view(request):
	user = request.user
	if user.is_superuser:
		closing_day = datetime.timedelta(days=1)
		yesterday = datetime.datetime.today() - closing_day
		y = make_aware(yesterday)
		today = datetime.datetime.today().date()
		today_single_leg_payments = SingleLegIncome.objects.all().filter(date=today)
		withdrawl = WithdrawlBill.objects.filter(date__date = datetime.date.today()).order_by('-date')
		total_user = User.objects.all()
		total_user_count = total_user.count()
		total_activated_user = Profile.objects.filter(activated = True)
		total_activated_user_count = total_activated_user.count()
		total_epin = Epin.objects.all()
		total_epin_count = total_epin.count()

		context = {
			'total_epin':total_epin,
			'total_epin_count': total_epin_count,
			'total_user_count':total_user_count,
			'total_activated_user_count':total_activated_user_count,
			'total_user':total_user,
			'total_activated_user':total_activated_user,
			'today_single_leg_payments': today_single_leg_payments,
			'withdrawl':withdrawl,

			}
		return render(request, 'payments/payments-management.html', context )
	else:
		return redirect('home')
def ammount_paid(request):
	if request.method == 'POST':
		r = request.POST.get('id')
		w = WithdrawlBill.objects.get(id=r)
		w.paid = True
		w.save()
		messages.success(request, 'Successfully paid')
		return redirect('payment-management')