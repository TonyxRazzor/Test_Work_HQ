from rest_framework import viewsets
from django.shortcuts import render

from data.models import Product, Lesson, TimeInfo, Student
from .serializers import (ProductSerializer,
                          LessonSerializer,
                          TimeInfoSerializer,
                          StudentSerializer,
                          ListSerializer
                          )


def index(request):
    return render(request, 'index.html')

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CurrentProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.filter(id=self.kwargs['pk'])
        return queryset


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class TimeInfoViewSet(viewsets.ModelViewSet):
    queryset = TimeInfo.objects.all()
    serializer_class = TimeInfoSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class ListViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ListSerializer

    def get_queryset(self):
        queryset = Student.objects.filter(id=self.request.user.id)
        return queryset
