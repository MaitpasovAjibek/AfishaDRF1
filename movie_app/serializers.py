from rest_framework import serializers
from .models import Movie,Director,Rewiew



class MovieSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = 'id title description duration duration director reviews'.split()

class DirectorSerializers(serializers.ModelSerializer):
    movies_count = serializers.SerializerMethodField()

    def get_movies_count(self,director):
        return director.movies_count()

    class Meta:
        model = Director
        fields ='__all__'


class RewiewSerilizers(serializers.ModelSerializer):
    class Meta:
        model = Rewiew
        fields = '__all__'


class MovieReviewSerializers(serializers.ModelSerializer):
    reviews = RewiewSerilizers(many=True)
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = 'id title description duration director reviews average_rating'.split()

    def get_average_rating(self, obj):
        total_stars = sum(review.stars for review in obj.reviews.all())
        num_reviews = obj.reviews.count()
        if num_reviews > 0:
            return total_stars / num_reviews
        else:
            return 0.0