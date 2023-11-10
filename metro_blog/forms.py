from django import forms
from django.forms import ModelForm, CheckboxSelectMultiple
from .models import *


class AddPostForm(ModelForm):

    class Meta:
        model = Blog
        exclude = ['time_created', 'time_update', 'is_public', 'owner']
        widgets = {
            'line': CheckboxSelectMultiple(),
            'content': forms.TextInput(attrs={'cols': 60, 'rows': 10}),
                   }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-input'})

        self.fields['content'].widget.attrs.update({'class': 'form-control django_ckeditor_5'})
        self.fields['content'].required = False


class CommentForm(ModelForm):
    text = forms.CharField(label='Введите комментарий',
                           widget=forms.TextInput(attrs={'class': 'form-input', 'cols': 60, 'rows': 10}))

    class Meta:
        model = Blog
        fields = ('text',)
