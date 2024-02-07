from django.urls import path
from . import views


urlpatterns = [
    # path('director/',views.director_list_api_view),
    # path('director/<int:id>/',views.director_detail_api_view),
    # path('movie',views.movie_list_api_view),
    # path('movie/<int:id>/',views.movie_detail_api_view),
    # path('rewiew/',views.review_list_api_view),
    # path('rewiew/<int:id>/',views.review_detail_api_view),
    # path('rewiew/movies',views.movie_review_list_api_view),
    path('directors/', views.DirectorListCreateAPIView.as_view()),
    path('directors/<int:id>/', views.DirectorDetailAPIView.as_view()),
    path('movies/', views.MovieListCreateAPIView.as_view()),
    path('movies/<int:id>/', views.MovieDetailAPIView.as_view()),
    path('review/', views.ReviewListCreateAPIView.as_view()),
    path('review/<int:id>/', views.ReviewDetailAPIView.as_view()),
    path('movies/reviews', views.movie_review_list_api_view),


]