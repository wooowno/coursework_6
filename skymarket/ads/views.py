from rest_framework import pagination, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from ads.models import Ad, Comment
from ads.permissions import IsOwner
from ads.serializers import AdSerializer, AdDetailSerializer, CommentSerializer


class AdPagination(pagination.PageNumberPagination):
    page_size = 4
    page_query_param = 'page_size'


class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    pagination_class = AdPagination

    def get_serializer_class(self):
        if self.action in ['retrieve', 'create', 'partial_update']:
            return AdDetailSerializer

        return super().serializer_class

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_permissions(self):
        if self.action in ['retrieve', 'create']:
            return IsAuthenticated
        elif self.action in ['partial_update', 'destroy']:
            return (IsOwner | IsAdminUser)
        return AllowAny


    @action(detail=False)
    def me(self, request):
        user_id = self.request.user.pk
        user_ads = Ad.objects.all().filter(author_id=user_id)

        page = self.paginate_queryset(user_ads)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(user_ads, many=True)
        return Response(serializer.data)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        ad_id = self.kwargs.get('ad_id')
        return Comment.objects.all().filter(ad_id=ad_id)

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            ad_id=self.kwargs.get('ad_id')
        )

    def get_permissions(self):
        if self.action in ['retrieve', 'create', 'list']:
            return IsAuthenticated
        elif self.action in ['partial_update', 'destroy']:
            return (IsOwner | IsAdminUser)
        return AllowAny
