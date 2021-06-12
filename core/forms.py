from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import QuestionBank, ModelTest
from django.forms import ModelForm
from django import forms
from .widgets import MyTextarea, CustomTextArea
from django.forms import ModelForm, Textarea


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']


class QuestionBankForm(ModelForm):
	question = forms.CharField(widget=MyTextarea, required=False)
	option_1 = forms.CharField(widget=MyTextarea, required=False)
	option_2 = forms.CharField(widget=MyTextarea, required=False)
	option_3 = forms.CharField(widget=MyTextarea, required=False)
	option_4 = forms.CharField(widget=MyTextarea, required=False)
	option_5 = forms.CharField(widget=MyTextarea, required=False)
	correct_answer = forms.CharField(widget=MyTextarea, required=False)
	explanation = forms.CharField(widget=MyTextarea, required=False)
	hints = forms.CharField(widget=MyTextarea, required=False)
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