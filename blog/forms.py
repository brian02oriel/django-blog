from django import forms

class ContactForm(forms.Form):
    fullname = forms.CharField(max_length = 50, widget = forms.TextInput(attrs={"value":""}), required=True, label = "Full Name")
    email = forms.EmailField(max_length = 50, widget = forms.TextInput(attrs={"value":""}), required=True,  label = "Email")
    message = forms.CharField(max_length = 500, widget = forms.Textarea(attrs={"value":""}), required=True, label = "Message")