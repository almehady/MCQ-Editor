from django.forms import Widget
from django import forms
from django.forms.widgets import Textarea


class MyTextarea(Textarea):
    template_name = 'core/textarea.html'

    def __init__(self, attrs=None):
        # Use slightly better defaults than HTML's 20x2 box
        default_attrs = {'cols': '100', 'rows': '10', 'class': 'vLargeTextField ascii-tinymce'}
        if attrs:
            default_attrs.update(attrs)
        super().__init__(default_attrs)


class CustomTextArea(forms.Textarea):
    template_name = 'core/textarea.html'