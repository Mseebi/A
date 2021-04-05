from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework import viewsets
from . import models
from . import serializers
from .models import Movies

from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.decorators import api_view


def all_movies(request):
    Movie = Movies.objects.all()
    if request.method == 'GET': 
        movie_serializer = serializers.MovieSerializer(Movie, many=True)
        return JsonResponse(movie_serializer.data, safe=False)
    
    
def movie_details(request, movie):
    
    movie_name = Movies.objects.get(movie=movie)
    if request.method == 'GET': 
        movie_serializer = serializers.MovieSerializer(movie_name)
        return JsonResponse(movie_serializer.data)