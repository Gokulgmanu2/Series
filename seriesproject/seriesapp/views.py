from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import Series
from . forms import SeriesForm
# Create your views here.
def index(request):
    series=Series.objects.all()
    context={'series_list':series}
    return render(request,'index.html',context)
def details(request,series_id):
    series=Series.objects.get(id=series_id)
    return  render(request,"details.html",{'series':series})
def add_series(request):
    if request.method=="POST":
        name=request.POST.get('name')
        desc=request.POST.get('desc')
        year=request.POST.get('year')
        img=request.FILES['img']
        series=Series(name=name,desc=desc,year=year,img=img )
        series.save()

    return render(request,'add.html')

def update(request,id):
    series=Series.objects.get(id=id)
    form=SeriesForm(request.POST or None,request.FILES,instance=series)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'series':series})
