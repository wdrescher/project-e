from django import forms

class ContractorCreationForm(forms.Form):

    cont_name = forms.CharField()
    cont_email = forms.CharField()
    address = forms.CharField()
    fname = forms.CharField()
    lname = forms.CharField()
    phone = forms.CharField()
    notes = forms.CharField()
