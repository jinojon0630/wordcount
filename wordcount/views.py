from django.http import HttpResponse
from django.shortcuts import render
from collections import Counter
from operator import itemgetter

def home(request):
    return render(request, 'home.html')

def count(request):
    text = request.GET['text']
    word_per_text = dict(Counter(text.split(' ')))

    return render(request, 'actions.html', 
        {
            'text': text,
            'length': len(text),
            'words': word_per_text
        })

def about(request):
    return render(request, 'about.html')