from django import forms
from .models import FileModel

class MultipleFileForm(forms.ModelForm):
    class Meta:
        model = FileModel
        fields = '__all__'

        widgets = {
            "files":forms.FileInput(attrs={'multiple':True}),
        }