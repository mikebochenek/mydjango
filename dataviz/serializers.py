from django.contrib.auth.models import User
from .models import Dataset, Visualization
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'email', 'groups']

class DatasetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dataset
        fields = ['id', 'data_type', 'request_text', 'response_text', 'blob_id', 'blob_url', 'nice_filename', 'nice_path', 'local_path', 'raw_text', 'user', 'create_date']
    
class VisualizationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Visualization
        fields = ['id', 'dataset', 'votes', 'created']