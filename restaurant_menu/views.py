from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ReadOnlyModelViewSet

from restaurant_menu.models import RestaurantMenu
from restaurant_menu.serializers import (
    RestaurantMenuListSerializer,
    RestaurantMenuDetailSerializer,
    RestaurantMenuRatingSerializer,
)


# Create your views here.
class RestaurantMenuListViewSet(APIView):
    def get(self, request):
        res_menu = RestaurantMenu.objects.all()
        serializer = RestaurantMenuListSerializer(res_menu, many=True)
        return Response({"rest_menu": [serializer.data]})


class RestaurantMenuViewSet(ReadOnlyModelViewSet):
    queryset = RestaurantMenu.objects.all()

    def get_serializer_class(self):
        if self.action == "rate":
            return RestaurantMenuRatingSerializer
        if self.action == "retrieve":
            return RestaurantMenuListSerializer
        return RestaurantMenuDetailSerializer

    @action(detail=True, methods=["POST"])
    def rate(self, request, pk):
        res_menu = RestaurantMenu.objects.get(id=pk)
        rating = float(request.POST.get("rating"))
        serializer = self.get_serializer_class()(data={"rating": rating})
        print(serializer.is_valid())
        if res_menu.ratind is None:
            res_menu.ratind = rating
        else:
            res_menu.ratind = res_menu.ratind + rating
        res_menu.save()
        return Response({"R": "Ok"})

    @action(detail=False)
    def max_rating(self, request):
        res_menu = RestaurantMenu.objects.all()
        res = max(r.ratind for r in res_menu)
        res_with_max_rating = RestaurantMenu.objects.get(ratind=res)
        serializer = RestaurantMenuListSerializer(res_with_max_rating)
        return Response({"rest_menu": [serializer.data]})
