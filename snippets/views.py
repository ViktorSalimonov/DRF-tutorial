# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer, UserSerializer
from rest_framework import permissions
from snippets.permissions import IsOwnerOrReadOnly
from rest_framework.response import Response
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.decorators import action


class SnippetViewSet(viewsets.ModelViewSet):
    """This viewset automatically provides list, CRUD actions."""
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlight)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """The viewset automatically provides list and delete actions."""
    queryset = User.objects.all()
    serializer_class = UserSerializer
