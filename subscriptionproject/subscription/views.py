from django.shortcuts import render, redirect
from .forms import SubscriptionForm
from .models import Subscription

def home(request):
    allSubscription = Subscription.objects.all()
    subscriptionForm = SubscriptionForm()
    if request.method == "POST":
        subscriptionForm = SubscriptionForm(request.POST or None)
        if subscriptionForm.is_valid():
            subscriptionForm.save()
            return redirect("home")

    return render(request, template_name="dashboard.html", context={"subscriptionForm" : subscriptionForm, "allSubscription" : allSubscription})