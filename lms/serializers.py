from rest_framework.serializers import ModelSerializer, SerializerMethodField
from rest_framework import serializers

from lms.models import Lesson, Course


class LessonSerializer(ModelSerializer):

    class Meta:
        model = Lesson
        # fields = '__all__'
        fields = ["id", "title", "description", "preview", "video"]


class CourseSerializer(ModelSerializer):

    lessons = SerializerMethodField()
    lessons_count = serializers.SerializerMethodField()

    def get_lessons_count(self, obj):
        return Lesson.objects.filter(course=obj).count()

    def get_lessons(self, course):

        return [
            f"{lesson.title} - {lesson.description}"
            for lesson in course.lesson_set.all()
        ]

    class Meta:
        model = Course
        # fields = '__all__'
        fields = ["id", "title", "description", "preview", "lessons","lessons_count"]


class CourseCountSerializer(ModelSerializer):
    course_count = CourseSerializer(many=True)

    class Meta:
        model = Course
        fields = ["id", "title", "description", "course_count"]
