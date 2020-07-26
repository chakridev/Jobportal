from django.shortcuts import render 
import requests
from bs4 import BeautifulSoup
 
from .jb import job_data
 
 
def jobs(request):
 
 
    if request.method == 'POST':
        job = request.POST['title']
        location = request.POST['location']
 
     
        job = job.strip()
        j = job.title().strip()
        items = j.split(' ')
        location = location.strip()
        job = job.replace(' ', '+')
 
        url ='https://www.indeed.co.in/jobs?q='+job+'&amp;l='+location+'&amp;sort=date'
 
        x,y,z,a,b = job_data(url,items)
        
 
        data = zip(x,y,z,a,b)
 
        if len(x)>0:
 
            context ={
                'data':data,
                 
            }
        else:
            context ={
                'message':'No Jobs Found..!',
                 
            }
 
 
        return render(request,'index.html',context)
     
    return render(request,'index.html')