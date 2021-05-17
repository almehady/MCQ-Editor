from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, QuestionBankForm, AddModelTestForm
from django.core.paginator import Paginator
from .models import Subject, QuestionBank
from .filters import QuestionBankSearchFilter

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
	total_model_test_question = QuestionBank.objects.all().filter(add_model_test=True).count()
	context = {'total_subjects':total_subjects, 'total_questions': total_questions, 'total_model_test_question': total_model_test_question}
	return render(request, 'core/index.html', context)


@login_required(login_url='/login')
def logout_view(request):
	logout(request)
	messages.info(request, 'You have successfully logged out!')
	return redirect("core:login")
    # Redirect to a success page.


# trips_filter = TripSearchFilter(request.GET, queryset=Trip.objects.all())
# 	trips = trips_filter.qs
# 	paginator = Paginator(trips, 20)
# 	page_number = request.GET.get('page')
# 	page_obj = paginator.get_page(page_number)
# 	count_trips = trips.count()
# 	context = {'trips': trips, 'trips_filter': trips_filter, 'count_trips': count_trips}
# 	return render(request, 'trips.html', {'page_obj': page_obj, 'trips_filter': trips_filter, 'count_trips': count_trips})
#
@login_required(login_url='/login')
def question_bank(request):
	question_filter = QuestionBankSearchFilter(request.GET, queryset=QuestionBank.objects.all().filter(add_model_test=False))
	questions = question_filter.qs
	# questions = QuestionBank.objects.all().filter(status__in=['P', 'C'])
	paginator = Paginator(questions, 25)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	return render(request, 'core/question_bank.html', {'page_obj': page_obj, 'question_filter': question_filter})


@login_required(login_url='/login')
def model_test(request):
	question_filter = QuestionBankSearchFilter(request.GET, queryset=QuestionBank.objects.all().filter(add_model_test=True))
	questions = question_filter.qs
	filterer_question_count = questions.count()
	# questions = QuestionBank.objects.all().filter(status__in=['P', 'C'])
	paginator = Paginator(questions, 25)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	return render(request, 'core/model_test.html', {'page_obj': page_obj, 'question_filter': question_filter, 'filterer_question_count': filterer_question_count})


@login_required(login_url='/login')
def update_question_bank(request, pk):
	question = QuestionBank.objects.get(id=pk)
	form = QuestionBankForm(instance=question)

	if request.method == 'POST':
		form = QuestionBankForm(request.POST, request.FILES, instance=question)
		if form.is_valid():
			form.save()
			return redirect('/close')

	context = {'form':form}
	return render(request, 'core/question_bank_update.html', context)


@login_required(login_url='/login')
def update_add_model_test(request, pk):
	question = QuestionBank.objects.get(id=pk)
	form = AddModelTestForm(instance=question)

	if request.method == 'POST':
		form = AddModelTestForm(request.POST, instance=question)
		if form.is_valid():
			form.save()
			return redirect('/close')
	context = {'form':form}
	return render(request, 'core/add_to_model_test.html', context)


class ClosePageView(TemplateView):
    template_name = "core/blank.html"



