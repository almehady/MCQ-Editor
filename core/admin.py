from django.contrib import admin

# Register your models here.
from .models import QuestionBank, Subject
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class QuestionBankResource(resources.ModelResource):
    class Meta:
        model = QuestionBank


class QuestionBankAdmin(ImportExportModelAdmin):
    resource_class = QuestionBankResource
    list_display = ('question', 'option_1', 'option_2', 'option_3', 'option_4', 'subject')
    search_fields = ('question', 'subject')
    list_filter = ('subject',)


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


admin.site.site_title = 'MCQ Editor'
admin.site.site_header = 'MCQ Editor'
admin.site.register(QuestionBank, QuestionBankAdmin)
admin.site.register(Subject, SubjectAdmin)