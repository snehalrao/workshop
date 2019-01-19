from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,"home.html")
def point(request):
    return render(request,"point.html")
def about(request):
    fulltext=request.GET['text']
    word_count=len(fulltext.split())
    word_dict={}
    for w in fulltext.split():
        if w in word_dict:
            word_dict[w]+=1
        else:
            word_dict[w]=1
    l=[(i,word_dict[i]) for i in word_dict]
    h=[1,2,3,4]
    return render(request,"about.html",{'fulltext':fulltext,'word_count':word_count,'word_dict':word_dict,'l':l,'h':h})