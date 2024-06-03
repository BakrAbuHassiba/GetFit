from rest_framework import serializers
from .models import Foods, User
from django.conf import settings

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=68, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = "__all__"

    def validate(self, attrs):
        email = attrs.get('email', '')
        username = attrs.get('username', '')

        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {'email': 'Email already exists'})

        if not username.isalnum():
            raise serializers.ValidationError(
                'The username should only contain alphanumeric character ')

        return attrs

    def create(self, validated_data):
        groups = validated_data.pop('groups', None)
        user_permissions = validated_data.pop('user_permissions', None)
        user = User.objects.create_user(**validated_data)

        if groups:
            user.groups.set(groups)
        if user_permissions:
            user.user_permissions.set(user_permissions)

        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ('id', 'email', 'username',
        #           'password', 'gender', 'weight', 'activity')
        fields ="__all__"
        extra_kwargs = {'password': {'write_only': True, 'required': True}}


class FoodsSerializer(serializers.ModelSerializer):
    likes = UserSerializer(many=True, read_only=True)
    # image_url = serializers.SerializerMethodField()

    class Meta:
        model = Foods
        fields='__all__'
        # fields = ["id", 'FoodName', 'TheDescription', 'YoutubeLink',
        #           'Calories', 'Protein', 'Fats', 'Carbs', 'image_url',"likes"]

    # def get_image_url(self, obj):
    #     request = self.context.get('request')
    #     if obj.LinkDrive:
    #         return request.build_absolute_uri(settings.MEDIA_URL + obj.LinkDrive)
    #     return None
