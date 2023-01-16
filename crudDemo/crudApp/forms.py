from django import forms
from crudApp.models import Student

# Create your forms here.
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'