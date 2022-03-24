from django import forms
from django.forms import inlineformset_factory
from posts.models import Post, Category, PostSeo
from tinymce.widgets import TinyMCE


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
        fields = ['title', 'content', 'image', 'category']
        error_messages = {
            'title': {
                'required': "The title is required!",
            },
            'content': {
                'required': "The content is required!",
            },
            'image': {
                'required': "The image is required!",
            },
            'category': {
                'required': "The category is required!",
            },
        }
        widgets = {
            'content': TinyMCE(attrs={'class': 'form-control'})
        }


class PostSeoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(PostSeoForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.errors:
                visible.field.widget.attrs['class'] = 'form-control is-invalid'
            else:
                visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = PostSeo
        fields = ['title', 'description']
        error_messages = {
            'title': {
                'required': "The title is required!",
            },
            'description': {
                'required': "The description is required!",
            },
        }


PostSeoInlineFormset = inlineformset_factory(
    Post,
    PostSeo,
    form=PostSeoForm,
    extra=0,
    min_num=1
    # max_num=5,
    # fk_name=None,
    # fields=None, exclude=None, can_order=False,
    # can_delete=True, max_num=None, formfield_callback=None,
    # widgets=None, validate_max=False, localized_fields=None,
    # labels=None, help_texts=None, error_messages=None,
    # min_num=None, validate_min=False, field_classes=None
)
