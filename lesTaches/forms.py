from django.forms import ModelForm, DateInput
from lesTaches.models import Task, User
from django import forms


class TaskForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields["name"].label = "Nom"
        self.fields["description"].label = "description"
        self.fields["due_date"].label = "due_date"
        self.fields["schedule_date"].label = "schedule_date"
        self.fields["closed"].label = "closed"
        owner = forms.MultipleChoiceField(widget=forms.SelectMultiple, choices=User.objects.all(), required=False)

    class Meta:
        model = Task
        fields = ("name", "description", "due_date", "schedule_date", "owner", "closed")
        widgets = {
            "due_date": DateInput(),
            "schedule_date": DateInput()
        }


class UserForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = "Username"
        self.fields['username'].required = False
        self.fields['email'].label = "Email"
        self.fields['email'].required = True

    class Meta:
        model = User
        fields = ("username", "email")
