from django.shortcuts import render
from django.http import HttpResponse
import operator

# Create your views here.
def homepage(request):
    #return HttpResponse("My  home page")
    return render(request,'wcount/home.html')
def about(request):
    #return HttpResponse("<h1>Nuvvu  evanivo naku thelvadhu</h2>")
    return render(request,'wcount/about.html')
def count(request):
    #return HttpResponse("Count  endhi sheyy")
    fulltext=request.GET['text']
    word_count=len(fulltext.split())
    word_dict={}
    for w in fulltext.split():
        if w in word_dict:
            word_dict[w]+=1
        else:
            word_dict[w]=1
    wl=[(x,word_dict[x]) for x in list(word_dict.keys())]
    return render(request,'wcount/count.html',{ 'fulltext':fulltext, 'word_count':word_count,'wd':word_dict, 'wl':wl })