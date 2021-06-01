import django_filters
from django import forms

from .models import QuestionBank

class QuestionBankSearchFilter(django_filters.FilterSet):
    category = django_filters.AllValuesMultipleFilter(field_name='category__title')
    SUBJECT_CHOICE = [
        ('❖বাংলা ভাষা ও সাহিত্য❖', '❖বাংলা ভাষা ও সাহিত্য❖'),
        ('❖English Language and Literature❖', '❖English Language and Literature❖'),
        ('❖বাংলাদেশ ও আন্তর্জাতিক বিষয়াবলি❖', '❖বাংলাদেশ ও আন্তর্জাতিক বিষয়াবলি❖'),
        ('❖গাণিতিক যুক্তি❖', '❖গাণিতিক যুক্তি❖'),
        ('❖সাধারণ বিজ্ঞান❖', '❖সাধারণ বিজ্ঞান❖'),
    ]
    # subject = forms.CharField(label='Select Subject', widget=forms.Select(choices=SUBJECT_CHOICE))
    subject = django_filters.AllValuesMultipleFilter(field_name='subject')

    class Meta:
        model = QuestionBank
        fields = '__all__'
        fields = ['question', 'category', 'subject', 'sub_subject', 'exam_year']


class ModelTestQuestionSearchFilter(django_filters.FilterSet):
    class Meta:
        model = QuestionBank
        fields = '__all__'
        fields = ['question', 'subject', 'sub_subject', 'model_test']