from django import forms
class ContactForm(forms.Form):
    subject = forms.CharField(max_length=20,label="Email subject",initial='hello',disabled=True)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)
