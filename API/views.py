from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.http import HttpResponseBadRequest

from .models import Song, Podcast, Audiobook
from .serializers import SongSerializer, PodcastSerializer, AudiobookSerializer

from rest_framework.views import APIView
from rest_framework.response import Response



class ListView(APIView):
	def get(self, request, file_slug, *args, **kwargs):
		if file_slug == 'song':
			song_queryset = Song.objects.all()
			song_serializer = SongSerializer(song_queryset, many=True)
			return Response(song_serializer.data)

		elif file_slug == 'podcast':
			podcast_queryset = Podcast.objects.all()
			podcast_serializer = PodcastSerializer(podcast_queryset, many=True)
			return Response(podcast_serializer.data)

		elif file_slug == 'audiobook':
			audiobook_queryset = Audiobook.objects.all()
			audiobook_serializer = AudiobookSerializer(audiobook_queryset, many=True)
			return Response(audiobook_serializer.data)

class CreateView(APIView):
	def post(self, request, file_slug, *args, **kwargs):
		if file_slug == 'song':
			name = request.POST['name']
			duration = request.POST['duration']
			uploaded_time = request.POST['uploaded_time']

			if uploaded_time < str(timezone.now()):
				return HttpResponseBadRequest('404 bad request')
			else:
				song = Song.objects.create(
					name=name,
					duration=duration,
					uploaded_time=uploaded_time)

				song_serializer = SongSerializer(song)
				return Response(song_serializer.data)

		elif file_slug == 'podcast':
			name = request.POST['name']
			duration = request.POST['duration']
			uploaded_time = request.POST['uploaded_time']
			host = request.POST['host']

			# participants = request.POST['participants']
			if uploaded_time < str(timezone.now()):
				return HttpResponseBadRequest('404 bad request')
			else:
				podcast = Podcast.objects.create(
					name=name,
					duration=duration, 
					uploaded_time=uploaded_time,
					host=host,
					#participants=participants
					)

				podcast_serializer = PodcastSerializer(podcast)
				return Response(podcast_serializer.data)

		elif file_slug == 'audiobook':
			title = request.POST['title']
			author = request.POST['author']
			narrator = request.POST['narrator']
			duration = request.POST['duration']
			uploaded_time = request.POST['uploaded_time']

			if uploaded_time < str(timezone.now()):
				return HttpResponseBadRequest('404 bad request')
			else:			

				audiobook = Audiobook.objects.create(
					title=title,
					author=author, 
					narrator=narrator,
					duration=duration,
					uploaded_time=uploaded_time)

				audiobook_serializer = AudiobookSerializer(audiobook)
				return Response(audiobook_serializer.data)

# class AllDetailView(RetrieveUpdateDestroyAPIView):
# 	serializer_class 
# 	queryset = All.objects.all()

# 	def perform_update(self, serializer):
# 		serializer.save()

class DetailView(APIView):
	def get(self, request, file_slug, pk, *args, **kwargs):
		if file_slug == 'song':
			song = get_object_or_404(Song, pk=pk)
			song_serializer = SongSerializer(song)
			return Response(song_serializer.data)

		elif file_slug == 'podcast':
			podcast= get_object_or_404(Podcast, pk=pk)
			podcast_serializer = PodcastSerializer(podcast)
			return Response(podcast_serializer.data)

		elif file_slug == 'audiobook':
			audiobook_queryset = get_object_or_404(Audiobook,pk=pk)
			audiobook_serializer = AudiobookSerializer(audiobook_queryset)
			return Response(audiobook_serializer.data)

	def delete(self, request, file_slug, pk, *args, **kwargs):
		context ={'object':'This item has been deleted.'}
		if file_slug == 'song':
			song = get_object_or_404(Song, pk=pk)
			song.delete()
			return Response(context)

		elif file_slug == 'podcast':
			podcast= get_object_or_404(Podcast, pk=pk)
			podcast.delete()
			return Response(context)

		elif file_slug == 'audiobook':
			audiobook_queryset = get_object_or_404(Audiobook,pk=pk)
			audiobook.delete()
			return Response(context)


	def put(self, request, file_slug, pk, *args, **kwargs):

		if file_slug == 'song':
			song = get_object_or_404(Song,pk=pk)
			song_serializer = SongSerializer(song, data=request.data)
			if song_serializer.is_valid():
				song_serializer.save()
				return Response(song_serializer.data)
			else:
				return Response(song_serializer.errors)

		elif file_slug == 'podcast':
			podcast = get_object_or_404(Podcast,pk=pk)
			podcast_serializer = PodcastSerializer(podcast, data=request.data)
			if podcast_serializer.is_valid():
				podcast_serializer.save()
				return Response(podcast_serializer.data)
			else:
				return Response(podcast_serializer.errors)

		elif file_slug == 'audiobook':
			audiobook = get_object_or_404(Audiobook,pk=pk)
			audiobook_serializer = AudiobookSerializer(audiobook, data=request.data)
			if audiobook_serializer.is_valid():
				audiobook_serializer.save()
				return Response(audiobook_serializer.data)
			else:
				return Response(audiobook_serializer.errors)
