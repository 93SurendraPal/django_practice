from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        #fields = ["document_id", "proof_type", "file_url"]
        fields = "__all__"
