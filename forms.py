from django import forms
from personal.models import Entry

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ('text',)
 