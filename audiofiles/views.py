from django.http import HttpResponseServerError
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Song, Podcast, Audiobook
from .serializers import SongSerializer, PodcastSerializer
from .serializers import AudiobookSerializer

# Create your views here.

# Expected HTTP responses
OK = status.HTTP_200_OK # Request successfull
BAD_REQUEST = status.HTTP_400_BAD_REQUEST # invalid request
INTERNAL_SERVER_ERROR = status.HTTP_500_INTERNAL_SERVER_ERROR # Other errors

def post_schema(serializer, *args):
    properties = {
        'title': openapi.Schema(type=openapi.TYPE_STRING),
        'Duration in seconds': openapi.Schema(type=openapi.TYPE_INTEGER)
    }
    for arg in args:
        properties[arg] = openapi.Schema(type=openapi.TYPE_STRING)
    return openapi.Schema(
        type=openapi.TYPE_OBJECT,
        #required=['username'],
        properties=properties
    )

class AudioListAPIView(APIView):
    """
        Base list endpoint for the following audio types:
        Song, Podcast and Audiobook.
        Implements the get and post methods
        required for posting to the underlying model of the child class.
    """
    
    def get(self, request, format=None):
        queryset = self.model.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data) # with the default status (200_OK)
    
    def post(self, request, format=None):
        # Deserialize posted data
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            # Save to database
            serializer.save()
            return Response(serializer.data) # Success!
        return Response(serializer.errors, status=BAD_REQUEST) # Fail!
        
class AudioDetailAPIView(APIView):
    """
        Base detail endpoint for the following audio types:
        Song, Podcast and Audiobook.
        Implements the get and put methods
        required for modifying the underlying model of the child class.
    """
    
    @swagger_auto_schema(responses={200: 'OK'})
    def get(self, request, pk, format=None):
        try:
            # retrieve data with the given id/pk
            data = self.model.objects.get(pk=pk);
            # If found
            serializer = self.serializer_class(data)
            return Response(serializer.data)
        except: # Oops! unable to retrieve the requested data
            return Response(status=INTERNAL_SERVER_ERROR)
    
    @swagger_auto_schema(responses={200: 'OK'})
    def put(self, request, pk, format=None):
        # Let's update the record with the specified id/pk
        try:
            data = self.model.objects.get(pk=pk)
            serializer = self.serializer_class(data, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=BAD_REQUEST)
        except:
            return Response(status=INTERNAL_SERVER_ERROR)
    
    @swagger_auto_schema(responses={200: 'OK'})
    def delete(self, request, pk, format=None):
        # Let's delete the record with the specified id/pk
        try:
            data = self.model.objects.get(pk=pk)
            data.delete()
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=INTERNAL_SERVER_ERROR)

# specific audio type implementations.
# Specifies the model and serializer to be used.

class SongList(AudioListAPIView):
    model = Song
    serializer_class = SongSerializer
    @swagger_auto_schema(
        responses={200: serializer_class(many=True)},
        operation_description='Displays a list of Song record'
    )
    def get(self, request):
        return super.get(request)
    @swagger_auto_schema(
        request_body=post_schema(
            serializer_class
        ),
        operation_description='Insert new record into Song database',
        responses={200: serializer_class(many=True)}
    )
    def post(self, request):
        return super.post(request)

class SongDetail(AudioDetailAPIView):
    model = Song
    serializer_class = SongSerializer

class PodcastList(AudioListAPIView):
    model = Podcast
    serializer_class = PodcastSerializer
    @swagger_auto_schema(
        responses={200: serializer_class(many=True)},
        operation_description='Displays a list of Podcast record'
    )
    def get(self, request):
        return super.get(request)
    @swagger_auto_schema(
        request_body=post_schema(
            serializer_class,
            'host', 'participants'
        ),
        operation_description='Insert new record into Podcast database',
        responses={200: serializer_class(many=True)}
    )
    def post(self, request):
        return super.post(request)
    
class PodcastDetail(AudioDetailAPIView):
    model = Podcast
    serializer_class = PodcastSerializer

class AudiobookList(AudioListAPIView):
    model = Audiobook
    serializer_class = AudiobookSerializer
    @swagger_auto_schema(
        responses={200: serializer_class(many=True)},
        operation_description='Displays a list of Audiobook record'
    )
    def get(self, request):
        return super.get(request)
    @swagger_auto_schema(
        request_body=post_schema(
            serializer_class,
        'author', 'narrator'
        ),
        operation_description='Insert new record into Audiobook database',
        responses={200: serializer_class(many=True)}
    )
    def post(self, request):
        return super.post(request)
    
class AudiobookDetail(AudioDetailAPIView):
    model = Audiobook
    serializer_class = AudiobookSerializer