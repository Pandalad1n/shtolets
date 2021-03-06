from django.views import generic
from django.shortcuts import render
from gallery.models import Picture


class Gallery(generic.View):
    def get(self, request):
        pics = Picture.objects.all().order_by('id')
        return render(request, 'home/gallery.html', {'pics': pics})
