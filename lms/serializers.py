from rest_framework.serializers import ModelSerializer, SerializerMethodField

from lms.models import Lesson, Course

class LessonSerializer(ModelSerializer):

    # course = CourseSerializer(read_only=True)
    course = SerializerMethodField()

    class Meta:
        model = Lesson
        # fields = '__all__'
        fields = ["id", "title", "course", "description", "preview", "video", "owner"]

class CourseSerializer(ModelSerializer):

    # lessons = SerializerMethodField()
    lessons = LessonSerializer(many=True)

    lessons_count = SerializerMethodField()

    def get_lessons(self, course):
        return [
            f"{lesson.title} - {lesson.description}"
            for lesson in course.lesson_set.all()
        ]

    def get_lessons_count(self, obj):
        return Lesson.objects.filter(course=obj).count()

    class Meta:
        model = Course
        # fields = '__all__'
        fields = [
            "id",
            "title",
            "description",
            "preview",
            "owner",
            "lessons",
            "lessons_count",
        ]

class CourseCountSerializer(ModelSerializer):
    course_count = CourseSerializer(many=True)

    class Meta:
        model = Course
        fields = ["id", "title", "description", "course_count"]
