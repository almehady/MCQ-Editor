from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import QuestionBank, ModelTest
from django.forms import ModelForm
from django import forms
from tinymce.widgets import TinyMCE


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']


class QuestionBankForm(ModelForm):
	class Meta:
		model = QuestionBank
		fields = ['question', 'option_1', 'option_2', 'option_3', 'option_4', 'option_5', 'correct_answer', 'explanation', 'explanation_image', 'hints', 'subject', 'sub_subject', 'other_exam', 'status']


class AddModelTestForm(ModelForm):
	add_model_test = forms.BooleanField(label='Are you sure?', required = False)
	class Meta:
		model = QuestionBank
		fields = ['model_test', 'add_model_test']


class ModelTestForm(ModelForm):
	class Meta:
		model = ModelTest
		fields = ['title', 'status']