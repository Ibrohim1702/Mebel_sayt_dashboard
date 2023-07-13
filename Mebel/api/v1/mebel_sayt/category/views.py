from rest_framework.exceptions import NotFound
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from api.v1.mebel_sayt.category.services import ctg_format, ctg_pag, get_one_ctg
from base.helper import BearerToken
from mebel_sayt.models import Category, Product, ProductImg
from .serializer import CategorySerializer


class CategoryView(GenericAPIView):
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (BearerToken,)

    def get_object(self, pk):
        try:
            root = Category.objects.get(pk=pk)
        except:
            raise NotFound(f"{pk} id not found")
        return root

    def get(self, requests, pk=None, *args, **kwargs):
        if pk:
            result = get_one_ctg(self.get_object(pk=pk))
        else:
            result = ctg_pag(requests)

        return Response(result)

    def post(self, requests, *args, **kwargs):
        data = requests.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        data = serializer.create(serializer.data)
        return Response(ctg_format(data))

    def put(self, requests, pk, *args, **kwargs):
        root = self.get_object(pk)
        data = requests.data
        serializer = self.serializer_class(data=data, instance=root, partial=True)
        serializer.is_valid(raise_exception=True)
        data = serializer.save()
        return Response(ctg_format(data))

    def delete(self, requests, pk, *args, **kwargs):
        root = Category.objects.get(pk=pk)
        root.delete()
        return Response('success', f"{root.content} successfully deleted")
