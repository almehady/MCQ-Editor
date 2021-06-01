import django_filters

from .models import QuestionBank

class QuestionBankSearchFilter(django_filters.FilterSet):
    category = django_filters.AllValuesMultipleFilter(field_name='category__title')
    class Meta:
        model = QuestionBank
        fields = '__all__'
        fields = ['question', 'category', 'subject', 'sub_subject', 'exam_year']


class ModelTestQuestionSearchFilter(django_filters.FilterSet):
    class Meta:
        model = QuestionBank
        fields = '__all__'
        fields = ['question', 'subject', 'sub_subject', 'model_test']