from django.contrib import admin

# Register your models here.
from .models import QuestionBank, Subject, ModelTest, Category
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class QuestionBankResource(resources.ModelResource):
    class Meta:
        model = QuestionBank
        fields = ('id', 'o_id', 'category', 'c1', 'c2', 'c3', 'question', 'option_1', 'option_2', 'option_3', 'option_4', 'option_5', 'correct_answer', 'explanation', 'hints', 'subject', 'sub_subject', 'exam_year', 'other_exam',)
        # import_id_fields = ['question', ]

    def get_instance(self, instance_loader, row):
        try:
            params = {}
            for key in instance_loader.resource.get_import_id_fields():
                field = instance_loader.resource.fields[key]
                params[field.attribute] = field.clean(row)
            return self.get_queryset().get(**params)
        except Exception:
            return None


class QuestionBankAdmin(ImportExportModelAdmin):
    resource_class = QuestionBankResource
    list_display = ('question', 'option_1', 'option_2', 'option_3', 'option_4', 'subject', 'add_model_test')
    search_fields = ('question', 'subject')
    list_filter = ('subject', 'add_model_test', 'model_test')


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


class CategoryAdmin(ImportExportModelAdmin):
    list_display = ('id', 'title', )


admin.site.site_title = 'MCQ Editor'
admin.site.site_header = 'MCQ Editor'
admin.site.register(QuestionBank, QuestionBankAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(ModelTest)
admin.site.register(Category, CategoryAdmin)