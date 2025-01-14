from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    get_object_or_404,
)
from rest_framework.views import APIView

from lms.models import Course, Lesson, Subscription
from lms.serializers import CourseSerializer, LessonSerializer, SubscriptionSerializer
from users.permissions import IsModerator, IsOwner
from .pagination import PageSize


class CourseViewSet(ModelViewSet):

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    pagination_class = PageSize

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        # course.owner = self.request.user
        # course.save()


class LessonCreateApiView(CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

    def perform_create(self, serializer):
        lesson = serializer.save()
        lesson.owner = self.request.user
        lesson.save()

    def get_permissions(self):

        self.permission_classes = (IsAuthenticated, ~IsModerator | IsOwner)

        if self.action == "create":
            self.permission_classes = (~IsModerator,)
        elif self.action in ("update", "retrieve"):
            self.permission_classes = (IsModerator | IsOwner,)
        elif self.action == "destroy":
            self.permission_classes = (IsOwner,)
        return super().get_permissions()


class LessonListApiView(ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    pagination_class = PageSize

    # def get_permissions(self):
    #     self.permission_classes = (~IsModerator,)
    #     return super().get_permissions()


class LessonRetrieveApiView(RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

    def get_permissions(self):
        self.permission_classes = (~IsModerator | IsOwner,)
        return super().get_permissions()


class LessonUpdateApiView(UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

    def get_permissions(self):
        self.permission_classes = (~IsModerator | IsOwner,)
        return super().get_permissions()


class LessonDestroyApiView(DestroyAPIView):
    # queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

    def get_permissions(self):
        self.permission_classes = (IsOwner,)
        return super().get_permissions()


class SubscriptionApiView(APIView):
    def post(self, *args, **kwargs):
        user = self.request.user
        course_id = self.request.data.get("pk")
        course_item = get_object_or_404(Course, pk=course_id)
        subs_items = Subscription.objects.filter(user=user, course=course_item)
        if subs_items.exists():
            subs_items.delete()
            message = "Подписка была удалена."
        else:
            Subscription.objects.create(user=user, course=course_item)
            message = "Подписка была создана."
        return Response({"message": message})


class SubscriptionListApiView(ListAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
