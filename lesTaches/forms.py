from django import forms
from django.forms import ModelForm
from lesTaches.models import Task, User


class TaskForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields["name"].label = "Nom"
        self.fields["description"].label = "Description"
        self.fields["due_date"].label = "Dernière date de rendu"
        self.fields["schedule_date"].label = "Date de rendu"
        self.fields["closed"].label = "Fermé"
        self.fields["owner"].label = "Utilisateur"

    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
            'schedule_date': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        }


class UserForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = "Nom d'utilisateur"
        self.fields['username'].required = False
        self.fields['email'].label = "Adresse email"
        self.fields['email'].required = True

    class Meta:
        model = User
        fields = '__all__'
