from django.http import FileResponse
import os
from django.shortcuts import render, HttpResponse
from .forms import MultipleFileForm
from . models import FileModel
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
# Create your views here.

def FileUploadView(request):
    if request.method=="POST":
        form = MultipleFileForm(request.POST, request.FILES)
        name = request.POST.get('name')
        files = request.FILES.getlist('files')
        if form.is_valid:
            for file in files:
                obj=FileModel(
                    name = name,
                    files=file
                )
                obj.save()
            return HttpResponse("submitted successfully")
        return HttpResponse(str(form.errors))
    form = MultipleFileForm()
    context = {
        'form':form
    }
    return render(request, 'multiple.html', context)

def filesDetailView(request):
    files = FileModel.objects.all()
    context = {
        'files':files
    }
    return render(request, 'files.html', context)

@login_required
def secureView(request, file):
    document = get_object_or_404(FileModel, pdf='files__/'+file)
    path, file_name = os.path.split(file)
    response = FileResponse(document.pdf)
    return response
