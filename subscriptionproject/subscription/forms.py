from django import forms
from .models import Subscription

class SubscriptionForm(forms.ModelForm):

    class Meta:
        model = Subscription
        fields = ("email",)

    def __init__(self, *args, **kwargs):
        super(SubscriptionForm, self).__init__(*args, **kwargs)
        self.fields["email"].widget.attrs.update({"autocomplete":"off"})