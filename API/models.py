from django.db import models
from django.utils import timezone
from multiselectfield import MultiSelectField
from django.contrib.postgres.fields import ArrayField

# Create your models here.


class Song(models.Model):
# Song file fields:
	ID = models.AutoField(primary_key=True)
	name = models.CharField(max_length=100 )
	duration = models.IntegerField()
	uploaded_time = models.DateField(default=timezone.now)

class Podcast(models.Model):
# Podcast file fields:
	ID = models.AutoField(primary_key=True)
	name = models.CharField(max_length=100 )
	duration = models.IntegerField()
	uploaded_time = models.DateField(default= timezone.now)	
	host = models.CharField(max_length=100 )
	participants = models.TextField()
	# participants = ArrayField(models.CharField(max_length=100))
	
class Audiobook(models.Model):
# Audiobook file fields:
	ID = models.AutoField(primary_key=True)
	title = models.CharField(max_length=100 )
	author =models.CharField(max_length=100 )
	narrator = models.CharField(max_length=100 )
	duration = models.IntegerField()
	uploaded_time = models.DateField(default=timezone.now)

