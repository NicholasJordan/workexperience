from django import forms

class RecordForm(forms.Form):
    work_date = forms.DateField(help_text="Enter the date of your work experience record", label='Date: ')
    work_details = forms.CharField(label='Details: ', widget=forms.Textarea)
