from django.http import HttpResponse
from django.shortcuts import render
from photos.models import Photo

def home(request):

    context = {
        'photo_list': Photo.objects.all().order_by('-creation_date')[:10]
    }
    return render(request, 'photos/home.html', context)

