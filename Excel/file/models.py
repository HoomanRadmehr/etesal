from django.db import models
from django.contrib.auth.models import User

class File(models.Model):
    title = models.CharField(max_length=100)
    customer = models.ForeignKey(User)
    excel_file = models.FileField(upload_to="documents/%Y/%m/%d")
    appileid = models.BooleanField(default=False)
