# coding: utf-8
from django.shortcuts import render
from subscriptions.forms import SubscriptionForm


def subscribe(request):
    return render(request, 'subscriptions/subscription_form.html', {'form': SubscriptionForm()})