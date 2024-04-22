from django.forms import Form, ChoiceField, CharField, IntegerField, ModelForm
from django.contrib.auth.models import User

choices = (
    ('book', 'book'),
    ('magazine', 'magazine'),
)

class TestForm(Form):
    choice = ChoiceField(choices=choices)
    text = CharField(max_length=50)
    number = IntegerField()

class RegistrationForm(ModelForm):
    first_name = CharField(max_length=80, required=True)
    last_name = CharField(max_length=100, required=True)
    email = CharField(max_length=100, required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']