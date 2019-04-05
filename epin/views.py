from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
from django.utils.crypto import get_random_string
from epin.models import Epin
# Create your views here.


def create_epin_view(request):
	if request.method == "POST":
		ammount = request.POST.get('ammount')
		value = request.POST.get('value')
		if not value and not ammount:
			messages.success(request, 'Enter valid Ammount and Value!! ')
			return redirect('epin_management')
		elif ammount and value :
			for x in range(1, int(ammount)+1):
				serial_nom = (get_random_string(10))
				epin =  Epin(serial_no = serial_nom)
				epin.pin_value = int(value)
				epin.save()
			messages.success(request, 'Epin Generated!!')
			return redirect('epin_management')


def epin_management_view(request):
	user = request.user
	if user.is_superuser:
		epin = Epin.objects.all().order_by('-id', 'used')
		context = {
			'epin':epin,
		}
		return render(request, 'epin/epin-management.html', context)
	elif not user.is_superuser:
		messages.success(request,'You must be superuser to Go to the pin section sorry!')
		return redirect('home')
	