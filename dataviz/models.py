from django.db import models

class User(models.Model):
    email = models.EmailField()
    create_date = models.DateTimeField()
    last_login_date = models.DateTimeField()

class Dataset(models.Model):
    data_type = models.IntegerField(default=0)
    raw_text = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateTimeField()

class Visualization(models.Model):
    dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)