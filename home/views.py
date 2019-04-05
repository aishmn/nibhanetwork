from django.shortcuts import render
from franchise.models import Franchise
from home.models import Gallery,Terms

def index(request):
	galleries= Gallery.objects.all()
	franchises= Franchise.objects.all()
	terms = Terms.objects.all()
	context={
	'terms':terms,
	'franchises': franchises,
	'galleries': galleries }
	return render(request, 'home/pages/index.html', context)
