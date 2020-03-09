from rest_framework.decorators import action
from rest_framework.response import Response
from . import utils, models

from apps.accounts.api.serializers import UserModelSerializer


class LikedMixin:

    @action(detail=True, methods=['POST'])
    def like(self, request, **kwargs):
        obj = self.get_object()
        utils.add(obj, request.user)
        return Response()

    @action(detail=True, methods=['POST'])
    def unlike(self, request, **kwargs):
        obj = self.get_object()
        utils.remove(obj, request.user)
        return Response()
