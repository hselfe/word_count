from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
    
def about(request):
    return render(request, 'about.html')
    
def count(request):
    full_text = request.GET['full_text']
    return render(request, 'count.html', {'original_text': full_text, 'full_text': word_count(full_text)})
    
def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts