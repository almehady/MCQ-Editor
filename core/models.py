from django.db import models
from django.contrib.auth.models import AbstractUser
from tinymce.models import HTMLField
# Create your models here.

QUESTION_STATUS = (
    ('D', 'Draft'),
    ('P', 'Published'),
    ('C', 'Correct & Published'),
    ('N', 'Need to Modify')
)


class Subject(models.Model):
    title = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title


class QuestionBank(models.Model):
    question = HTMLField(blank=True, null=True)
    option_1 = HTMLField(blank=True, null=True)
    option_2 = HTMLField(blank=True, null=True)
    option_3 = HTMLField(blank=True, null=True)
    option_4 = HTMLField(blank=True, null=True)
    option_5 = HTMLField(blank=True, null=True)
    correct_answer = HTMLField(blank=True, null=True)
    explanation = HTMLField(blank=True, null=True)
    explanation_image = models.ImageField(upload_to='explanation/', null=True, blank=True)
    hints = HTMLField(blank=True, null=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, blank=True, null=True)
    sub_subject = models.CharField(max_length=450, blank=True, null=True)
    other_exam = models.CharField(max_length=500, blank=True, null=True, help_text='write the exam name here')
    status = models.CharField(choices=QUESTION_STATUS, max_length=1, default='P')
    add_model_test = models.BooleanField(default=False, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __unicode__(self):
        return self.question

    def __str__(self):
        return self.question

