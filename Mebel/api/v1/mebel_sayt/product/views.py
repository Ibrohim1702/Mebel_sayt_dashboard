from rest_framework.exceptions import NotFound
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.v1.mebel_sayt.product.serializer import ProductSerializer
from api.v1.mebel_sayt.product.services import prod_format, get_one_prod, prod_pag
from base.helper import BearerToken
from mebel_sayt.models import Product


class ProductView(GenericAPIView):
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (BearerToken,)

    def get_object(self, pk):
        try:
            root = Product.objects.get(pk=pk)
        except:
            raise NotFound(f"{pk} id not found")
        return root

    def get(self, requests, pk=None, *args, **kwargs):
        if requests:

            result = prod_pag(requests)
            return Response(result)

    def post(self, requests, *args, **kwargs):
        data = requests.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        data = serializer.create(serializer.data)
        return Response(prod_format(data))

    def put(self, requests, pk, *args, **kwargs):
        root = self.get_object(pk)
        data = requests.data
        serializer = self.serializer_class(data=data, instance=root, partial=True)
        serializer.is_valid(raise_exception=True)
        data = serializer.save()
        return Response(prod_format(data))

    def delete(self, requests, pk, *args, **kwargs):
        root = Product.objects.get(pk=pk)
        root.delete()
        return Response('success', f"{root.name} successfully deleted")
