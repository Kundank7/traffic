# traffic/forms.py

from django import forms

class TrafficForm(forms.Form):
    url = forms.URLField(label='Website URL', max_length=200)
    views = forms.IntegerField(label='Number of Views', min_value=1)
