from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(AuthenticationForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.errors:
                visible.field.widget.attrs['class'] = 'form-control is-invalid'
            else:
                visible.field.widget.attrs['class'] = 'form-control'


class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(UserCreationForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.errors:
                visible.field.widget.attrs['class'] = 'form-control is-invalid'
            else:
                visible.field.widget.attrs['class'] = 'form-control'
