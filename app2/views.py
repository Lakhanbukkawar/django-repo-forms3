from django.shortcuts import render
from app2.form import studentform

# Create your views here.
def index(request):
    form=studentform(request.POST)
    if form.is_valid():
        form.save()
        print(form.cleaned_data)
    return render(request,'main.html',{'forms':form})
