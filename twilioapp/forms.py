from django import forms


class TwiliioSmsForm(forms.Form):
    send_to = forms.CharField(max_length=13, required=True,initial="+91",
                               widget=forms.NumberInput(attrs={'class': 'form-control'}))
    sms_text = forms.CharField(max_length=150, required=True,initial="This is a demo text",
                               widget=forms.Textarea(attrs={'class': 'form-control'}))