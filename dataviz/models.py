from django.db import models
import datetime 

class User(models.Model):
    email = models.EmailField()
    create_date = models.DateTimeField()
    last_login_date = models.DateTimeField()
    created = models.DateTimeField(default=datetime.datetime.now)

class Dataset(models.Model):
    data_type = models.IntegerField(default=0)
    request_text = models.CharField(max_length=4000)
    response_text = models.CharField(max_length=4000)
    blob_id = models.IntegerField(default=0)
    blob_url = models.CharField(max_length=200)
    nice_filename = models.CharField(max_length=200)
    nice_path = models.CharField(max_length=200)
    local_path = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(default=datetime.datetime.now)

class Visualization(models.Model):
    dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)
    created = models.DateTimeField(default=datetime.datetime.now)