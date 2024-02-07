from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Movie,Rewiew,Director
from .serializers import MovieSerializers,DirectorSerializers,RewiewSerilizers,MovieReviewSerializers,\
MovieValidatorSerializer,DirectorValidatorSerializer,ReviewValidatorSerializer,DirectorDetailValidatorSerializer,\
MovieDetailValidatorSerializer,ReviewDetailValidatorSerializer
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
#
# @api_view(['GET','PUT','DELETE'])
# def movie_detail_api_view(request,id):
#     movies = Movie.objects.get(id=id)
#     if request.method == 'GET':
#         data = MovieSerializers(movies).data
#         return Response(data=data)
#     elif request.method == 'DELETE':
#         movies.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     elif request.method == 'PUT':
#         serializer = MovieDetailValidatorSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         movies.title = request.data.get('title')
#         movies.description = request.data.get('description')
#         movies.duration = request.data.get('duration')
#         movies.director_id = request.data.get('director_id')
#         movies.save()
#         return Response(data={'movie_id': movies.id}, status=status.HTTP_201_CREATED)
#
#
# @api_view(['GET','POST'])
# def movie_list_api_view(request):
#     if request.method == 'GET':
#         movie = Movie.objects.all()
#         data = MovieSerializers(movie,many=True).data
#         return Response(data=data)
#     elif request.method == 'POST':
#         serializer = MovieValidatorSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(status=status.HTTP_400_BAD_REQUEST,
#                             data={'errors': serializer.errors})
#         title = request.data.get('title')
#         description = request.data.get('description')
#         duration = request.data.get('duration')
#         director_id = request.data.get('director_id')
#         movie = Movie.objects.create(title=title,description=description,duration=duration,director_id=director_id)
#         return Response(data={'movie_id':movie.id},status=status.HTTP_201_CREATED)
#
#
#
#
# @api_view(['GET','PUT','POST'])
# def director_detail_api_view(request,id):
#     directors = Director.objects.get(id=id)
#     if request.method == 'GET':
#         data = DirectorSerializers(directors).data
#         return Response(data=data)
#     elif request.method == 'DELETE':
#         directors.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     elif request.method == 'PUT':
#         serializer = DirectorDetailValidatorSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         text = request.data.get('text')
#         movie_id = request.data.get('movie_id')
#         directors = Director.objects.create(text=text,movie_id=movie_id)
#         directors.name = request.data.get('name')
#         directors.save()
#         return Response(data={'directors_id': directors.id}, status=status.HTTP_201_CREATED)
#
#
# @api_view(['GET','POST'])
# def director_list_api_view(request):
#     if request.method == "GET":
#         director = Director.objects.all()
#         data = DirectorSerializers(director,many=True).data
#         return Response(data=data)
#     elif request.method == 'POST':
#         serializer = DirectorValidatorSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(status=status.HTTP_400_BAD_REQUEST,
#                             data={'errors': serializer.errors})
#         name = request.data.get('name')
#         director = Director.objects.create(name=name)
#         return Response(data={'director_id': director.id}, status=status.HTTP_201_CREATED)
#
#
# @api_view(['GET','POST'])
# def review_detail_api_view(request,id):
#     reviews = Rewiew.objects.get(id=id)
#     if request.method == 'GET':
#         data = RewiewSerilizers(reviews).data
#         return Response(data=data)
#     elif request.method == 'DELETE':
#         reviews.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     elif request.method == 'PUT':
#         serializer = ReviewDetailValidatorSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         reviews.text = request.data.get('text')
#         reviews.movie = request.data.get('movie')
#         reviews.movie_id = request.data.get('movie_id')
#         reviews.save()
#         return Response(data={'movie_id': reviews.id}, status=status.HTTP_201_CREATED)
#
#
# @api_view(['GET','POST'])
# def review_list_api_view(request):
#     if request.method == 'GET':
#         review = Rewiew.objects.all()
#         data = RewiewSerilizers(review,many=True).data
#         return Response(data=data)
#     elif request.method == 'POST':
#         serializer = ReviewValidatorSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(status=status.HTTP_400_BAD_REQUEST,
#                             data={'errors': serializer.errors})
#         text = request.data.get('text')
#         movie_id = request.data.get('movie_id')
#         review = Rewiew.objects.create(text=text, movie_id=movie_id)
#         return Response(data={'review_id': review.id}, status=status.HTTP_201_CREATED)
#


class DirectorListCreateAPIView(ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializers
    pagination_class = PageNumberPagination

class DirectorDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializers
    lookup_field = 'id'


class MovieListCreateAPIView(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializers
    pagination_class = PageNumberPagination

class MovieDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializers
    lookup_field = 'id'


class ReviewListCreateAPIView(ListCreateAPIView):
    queryset = Rewiew.objects.all()
    serializer_class = RewiewSerilizers
    pagination_class = PageNumberPagination

class ReviewDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Rewiew.objects.all()
    serializer_class = RewiewSerilizers
    lookup_field = 'id'

















@api_view(['GET','POST'])
def movie_review_list_api_view(request):
    print(request.data)
    if request.method =="GET":
        movies = Movie.objects.all()
        data = MovieReviewSerializers(movies, many=True).data
        return Response(data=data)