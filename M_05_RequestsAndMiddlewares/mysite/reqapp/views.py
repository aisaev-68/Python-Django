from django.core.exceptions import ValidationError
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.http import JsonResponse

from . import models


def upload_file(request: HttpRequest) -> HttpResponse:
    limit = 1 * 1024 * 1024

    if request.method == "POST" and request.FILES.get('file', ''):
        image_file = request.FILES.get('file', '')
        file_title = request.POST.get("fileTitle", '')
        if image_file.size > limit:
            return render(request, "reqapp/req_form.html", {"context": "Ошибка! 'Размер файла не должен превышать 1 Mb.'"})
            # raise ValidationError('Размер файла не должен превышать 1 Mb.')

        fs = FileSystemStorage()
        filename = fs.save(image_file.name, image_file)
        image_url = fs.url(filename)
        document = models.Files(
            title=file_title,
            uploadedFile=image_url
        )
        document.save()
        documents = models.Files.objects.all()
        return render(request, "reqapp/req_form.html", {'files': documents})

    return render(request, "reqapp/req_form.html")

