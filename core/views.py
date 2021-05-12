from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
# Create your views here.


def login_page(request):
	if request.user.is_authenticated:
		return redirect('core:index')
	else:
		if request.method == 'POST':
			email = request.POST.get('email')
			password =request.POST.get('password')
			user = authenticate(request, email=email, password=password)
			if user is not None:
				login(request, user)
				return redirect('core:index')
			else:
				messages.info(request, 'Something went wrong! try again.')

		context = {}
		return render(request, 'core/login.html', context)


class IndexView(TemplateView):
    template_name = "core/index.html"


# @login_required(login_url='/admin/login')
# def index(request):
# 	total_trips = Trip.objects.all().count()
# 	drivers = CustomUser.objects.filter(role='D')
# 	total_driver = drivers.count()
# 	company = CustomUser.objects.filter(role='C')
# 	total_company = company.count()
# 	context = {'total_driver':total_driver, 'total_company':total_company, 'total_trips': total_trips }
# 	return render(request, 'index.html', context)
