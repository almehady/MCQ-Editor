import django_filters

from .models import QuestionBank

class QuestionBankSearchFilter(django_filters.FilterSet):
    class Meta:
        model = QuestionBank
        fields = '__all__'
        fields = ['question', 'subject', 'sub_subject', 'status']


class ModelTestQuestionSearchFilter(django_filters.FilterSet):
    class Meta:
        model = QuestionBank
        fields = '__all__'
        fields = ['question', 'subject', 'sub_subject', 'model_test']