# coding: utf-8
from django.shortcuts import render
from core.models import Speaker, Talk
from django.shortcuts import get_object_or_404

def home(request):
    return render(request, 'index.html')

def speaker_detail(request, slug):
    speaker = get_object_or_404(Speaker, slug=slug)
    context = {'speaker': speaker}
    return render(request, 'core/speaker_detail.html', context)

def talk_list(request):
    context = {
        'morning_talks': Talk.objects.at_morning(),
        'afternoon_talks': Talk.objects.at_afternoon()
    }
    return render(request, 'core/talk_list.html', context)