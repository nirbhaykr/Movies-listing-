from rest_framework import serializers
from Movies.models import Movies, Genre


class GenreSerializer(serializers.ModelSerializer):

    """
    Purpose: A serializer that deals with Details instances and
    querysets.
    """

    class Meta(object):
        model = Genre
#         fields = ('category',)
#         read_only_fields = ('entries',)
#         exclude = ('broken_url_flag',)


class MovieSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(many=True,
                                    required=False, read_only=False)
    genre = serializers.SlugRelatedField(many=True, queryset = Genre.objects.all(), read_only=False, slug_field='category')

    def create(self, validated_data):
        if validated_data.get('genre'):
            cateogry_list = validated_data.pop('genre')
        mov_obj = Movies.objects.create(**validated_data)
        mov_obj.genre.add(*cateogry_list)
        return mov_obj 

    class Meta(object):
        model = Movies
        fields = ('id','name', 'director', 'popularity', 'imdb_score','genre')


