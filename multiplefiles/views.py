from django.http import FileResponse
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
import os
from django.shortcuts import render, HttpResponse
from .forms import MultipleFileForm
from . models import FileModel
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
# Create your views here.

def loginView(request):
     if request.method=="POST":
          username = request.POST['username']
          password = request.POST['password']
          user = authenticate(username=username, password=password)
          if user:
               login(request, user)
               messages.success(request, 'Login successfully.')
          messages.error(request,'Invalid username or password')
     return render(request, 'login.html')

def FileUploadView(request):
    if request.method == "POST":
        form = MultipleFileForm(request.POST, request.FILES)
        name = request.POST.get('name')
        files = request.FILES.getlist('files')
        if form.is_valid:
            for file in files:
                obj = FileModel(
                    name=name,
                    files=file
                )
                obj.save()
            return HttpResponse("submitted successfully")
        return HttpResponse(str(form.errors))
    form = MultipleFileForm()
    context = {
        'form': form
    }
    return render(request, 'multiple.html', context)


def filesDetailView(request):
    files = FileModel.objects.all()
    context = {
        'files': files
    }
    return render(request, 'files.html', context)


@login_required
def secureView(request, file):
        document = get_object_or_404(FileModel, files='files__/'+file)
        files, file_name = os.path.split(file)
        response = FileResponse(document.files)
        return response
