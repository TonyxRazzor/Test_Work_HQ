from rest_framework import serializers
from data.models import Product, Lesson, TimeInfo, Student


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class TimeInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeInfo
        fields = '__all__'


class Lesson1Serializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = ('title', 'url', 'viewing', 'student_time')


class ProductSerializer(serializers.ModelSerializer):
    lessons = Lesson1Serializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ("id", "owner", "title", 'lessons')


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class ListSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Student
        fields = ('products',)


class StatisticSerializer(serializers.ModelSerializer):
    sum_viewing = serializers.SerializerMethodField(
        source='Суммарное просмотренное время')

    class Meta:
        model = Product
        fields = ('sum_viewing',)
