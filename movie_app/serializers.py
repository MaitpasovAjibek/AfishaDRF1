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

class DirectorValidatorSerializer(serializers.Serializer):
    name = serializers.CharField()

class MovieValidatorSerializer(serializers.Serializer):
    title = serializers.CharField(min_length=1, max_length=25)
    description = serializers.CharField(min_length=5, max_length=1500)
    duration = serializers.FloatField(min_value=1, max_value=5)
    director_id = serializers.IntegerField()

class ReviewValidatorSerializer(serializers.Serializer):
    text = serializers.CharField(min_length=5, max_length=1500)
    movie_id = serializers.IntegerField()

class DirectorDetailValidatorSerializer(serializers.Serializer):
    name = serializers.CharField()

class MovieDetailValidatorSerializer(serializers.Serializer):
    title = serializers.CharField(min_length=1, max_length=25)
    description = serializers.CharField(min_length=5, max_length=1500)
    duration = serializers.FloatField(min_value=1, max_value=5)
    director_id = serializers.IntegerField()

class ReviewDetailValidatorSerializer(serializers.Serializer):
    text = serializers.CharField(min_length=5, max_length=1500)
    movie = serializers.CharField()
    movie_id = serializers.IntegerField()