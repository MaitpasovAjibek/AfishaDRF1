from django.urls import path
from . import views


urlpatterns = [
    path('director/',views.director_list_api_view),
    path('director/<int:id>/',views.director_detail_api_view),
    path('movie',views.movie_list_api_view),
    path('movie/<int:id>/',views.movie_detail_api_view),
    path('rewiew/',views.review_list_api_view),
    path('rewiew/<int:id>/',views.review_detail_api_view),
    path('rewiew/movies',views.movie_review_list_api_view),

]