from django import forms
from posts.models import Post, Category
from django.core.validators import ValidationError


def min_length_check(val):
    if len(val) <= 10:
        raise ValidationError('Value must be greater than 10!')


class PostsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(PostsForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.errors:
                visible.field.widget.attrs['class'] = 'form-control is-invalid'
            else:
                visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Post
        fields = ['title', 'content']
        error_messages = {
            'title': {
                'required': "The title is required!",
            },
            'content': {
                'required': "The content is required!",
            },
        }


class PostCategoryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(PostCategoryForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.errors:
                visible.field.widget.attrs['class'] = 'form-control is-invalid'
            else:
                visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Category
        fields = ['title', 'slug']
        error_messages = {
            'title': {
                'required': "The title is required!",
            }
        }
