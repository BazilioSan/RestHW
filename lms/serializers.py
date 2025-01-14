from rest_framework.serializers import ModelSerializer, SerializerMethodField

from .validators import Only_Youtube

from lms.models import Lesson, Course, Subscription


class LessonSerializer(ModelSerializer):

    # course = CourseSerializer(read_only=True)
    course = SerializerMethodField()

    class Meta:
        model = Lesson
        # fields = '__all__'
        fields = ["id", "title", "course", "description", "preview", "video", "owner"]
        validators = (Only_Youtube(field="video"),)


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

    def get_subscription(self, course):

        user = self.context.get("request").user
        return Subscription.objects.filter(user=user, course=course).exists()

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
            "subscription",
        ]


class CourseCountSerializer(ModelSerializer):
    course_count = CourseSerializer(many=True)

    class Meta:
        model = Course
        fields = ["id", "title", "description", "course_count"]


class SubscriptionSerializer(ModelSerializer):

    class Meta:
        model = Subscription
        fields = ("user", "course")
