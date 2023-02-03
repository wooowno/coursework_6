from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers


from ads.models import Ad, Comment


class CommentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True, required=False)
    author_id = serializers.IntegerField(read_only=True, required=False)
    created_at = serializers.DateField(required=False)
    author_first_name = serializers.CharField(read_only=True, required=False)
    author_last_name = serializers.CharField(read_only=True, required=False)
    ad_id = serializers.IntegerField(read_only=True, required=False)
    author_image = serializers.ImageField(read_only=True, required=False)

    class Meta:
        model = Comment
        fields = ['id', 'text', 'author_id', 'created_at', 'author_first_name', 'author_last_name', 'ad_id', 'author_image']


class AdSerializer(serializers.ModelSerializer):
    pk = serializers.IntegerField(required=False)
    image = serializers.ImageField(required=False)
    description = serializers.CharField(required=False)

    class Meta:
        model = Ad
        fields = ['pk', 'image', 'title', 'price', 'description']


class AdDetailSerializer(serializers.ModelSerializer):
    pk = serializers.IntegerField(read_only=True, required=False)
    image = serializers.ImageField(required=False)
    phone = PhoneNumberField(required=False)
    description = serializers.CharField(required=False)
    author_first_name = serializers.CharField(read_only=True, required=False)
    author_last_name = serializers.CharField(read_only=True, required=False)
    author_id = serializers.IntegerField(read_only=True, required=False)

    class Meta:
        model = Ad
        fields = ["pk", "image", "title", "price", "phone", "description", "author_first_name", "author_last_name", "author_id"]
