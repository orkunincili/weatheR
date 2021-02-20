from django import forms


class CityForm(forms.Form):

    city = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder': 'City'}))