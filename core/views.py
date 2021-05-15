from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, QuestionBankForm
from django.core.paginator import Paginator
from .models import Subject, QuestionBank

# Create your views here.


def login_page(request):
	if request.user.is_authenticated:
		return redirect('core:index')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')
			user = authenticate(request, username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect('core:index')
			else:
				messages.info(request, 'Something went wrong! try again.')

		context = {}
		return render(request, 'core/login.html', context)


@login_required(login_url='/login')
def index(request):
	total_subjects = Subject.objects.all().count()
	total_questions = QuestionBank.objects.all().count()
	context = {'total_subjects':total_subjects, 'total_questions': total_questions}
	return render(request, 'core/index.html', context)


@login_required(login_url='/login')
def logout_view(request):
	logout(request)
	messages.info(request, 'You have successfully logged out!')
	return redirect("core:login")
    # Redirect to a success page.


@login_required(login_url='/login')
def question_bank(request):
	questions = QuestionBank.objects.all().filter(status__in=['P', 'C'])
	paginator = Paginator(questions, 50)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	return render(request, 'core/question_bank.html', {'page_obj': page_obj})


@login_required(login_url='/login')
def update_question_bank(request, pk):
	question = QuestionBank.objects.get(id=pk)
	form = QuestionBankForm(instance=question)

	if request.method == 'POST':
		form = QuestionBankForm(request.POST, instance=question)
		if form.is_valid():
			form.save()
			return redirect('/close')

	context = {'form':form}
	return render(request, 'core/question_bank_update.html', context)


class ClosePageView(TemplateView):
    template_name = "core/blank.html"



