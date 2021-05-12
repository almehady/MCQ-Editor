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


class QuestionBank(models.Model):
    category = models.CharField(max_length=200, blank=True, null=True)
    sub_category = models.CharField(max_length=200, blank=True, null=True)
    o_id = models.CharField(max_length=100, blank=True, null=True)
    c1 = models.CharField(max_length=100, blank=True, null=True)
    c2 = models.CharField(max_length=100, blank=True, null=True)
    c3 = models.CharField(max_length=100, blank=True, null=True)
    question = HTMLField(blank=True, null=True)
    option_1 = HTMLField(blank=True, null=True)
    option_2 = HTMLField(blank=True, null=True)
    option_3 = HTMLField(blank=True, null=True)
    option_4 = HTMLField(blank=True, null=True)
    option_5 = HTMLField(blank=True, null=True)
    correct_answer = HTMLField(blank=True, null=True)
    explanation = HTMLField(blank=True, null=True)
    hints = HTMLField(blank=True, null=True)
    issue = models.CharField(max_length=100, blank=True, null=True)
    subject = models.CharField(max_length=150, blank=True, null=True)
    sub_subject = models.CharField(max_length=450, blank=True, null=True)
    exam_year = models.CharField(max_length=350, blank=True, null=True)
    other_exam = models.CharField(max_length=500, blank=True, null=True)
    media = models.ImageField(upload_to='quiz/', null=True, blank=True)
    status = models.CharField(choices=QUESTION_STATUS, max_length=1, default='P')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __unicode__(self):
        return self.question

    def __str__(self):
        return self.question

