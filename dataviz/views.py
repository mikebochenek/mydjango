from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from .models import Dataset, User, Visualization
from .serializers import UserSerializer, DatasetSerializer, VisualizationSerializer
from rest_framework import viewsets
import logging
import json

logger = logging.getLogger(__name__)

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

def index(request):
    return render(request, 'index.html')

def upload(request):
    return render(request, 'upload.html')


class DatasetViewSet(viewsets.ModelViewSet):
    queryset = Dataset.objects.all().order_by('-create_date')
    serializer_class = DatasetSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-created')
    serializer_class = UserSerializer

class VisualizationViewSet(viewsets.ModelViewSet):
    queryset = Visualization.objects.all().order_by('-created')
    serializer_class = VisualizationSerializer

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})