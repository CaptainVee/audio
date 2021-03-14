from rest_framework import fields, serializers
from .models import Song, Podcast, Audiobook
from rest_framework.serializers import ModelSerializer,SerializerMethodField



class SongSerializer(ModelSerializer):
	class Meta:
		model = Song
		fields = (
			'ID','name', 'duration', 'uploaded_time',
			)	


class PodcastSerializer(ModelSerializer):
	class Meta:
		model = Podcast
		fields = (
			'ID', 'name', 'duration', 'uploaded_time', 'host', 'participants'
			)

class AudiobookSerializer(ModelSerializer):
	class Meta:
		model = Audiobook
		fields = (
			'ID','title', 'narrator','author', 'uploaded_time',
			)	
