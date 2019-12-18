from django.http import HttpResponse, JsonResponse
from django.views import View
from .form import Product
from django.shortcuts import render
from .models import Item, Review
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .serializers import ItemSerializer, ReviewSerializer
import json
from django.shortcuts import get_object_or_404


@method_decorator(csrf_exempt, name='dispatch')
class AddItemView(View):
    """View for create product"""

    def post(self, request):
        document = json.loads(request.body)
        if ItemSerializer(data=document).is_valid():
            product = Item(title=document["title"], description=document["description"], price=document["price"])
            product.save()
            return JsonResponse({"id": product.pk}, status=201)
        else:
            return JsonResponse({"error": "Incorrect data"}, status=400)
        # this code might use when user will be input data

        # def get(self, request):
        #     data = Product(request.POST)
        #     return render(request, "form.html", {"data": data})
        # def post(self, request):ite,
        #     form = Product(request.POST)
        #     if form.is_valid():
        #         data = list(form.cleaned_data.items())
        #         Item(title=data[0][1], description=data[1][1], price=data[2][1]).save()
        #         return JsonResponse(form.cleaned_data, status=201)
        #     else:
        #         return JsonResponse({}, status=404)


@method_decorator(csrf_exempt, name='dispatch')
class PostReviewView(View):
    """View for create review about product."""

    def post(self, request, item_id):
        document = json.loads(request.body)
        if ReviewSerializer(data=document).is_valid():
            if Item.objects.filter(id=item_id):
                Review(text=document["text"], grade=document["grade"], item=Item.objects.get(id=item_id)).save()
                return JsonResponse({"id": item_id}, status=201)
            else:
                return JsonResponse({"error": "User with id=" + str(item_id) + " doesn't exist"}, status=401)

        else:
            return JsonResponse({"error": "Incorrect data"}, status=400)


@method_decorator(csrf_exempt, name='dispatch')
class GetItemView(View):
    """View for receiving information about product."""

    def get(self, request, item_id):
        if Item.objects.filter(id=item_id):
            product = Item.objects.get(id=item_id)
            info_product = {"id": item_id, "title": product.title, "description": product.description,
                            "review": [{"id": x.id, "text": x.text, "grade": x.grade} for x in
                                       Review.objects.filter(item__id=item_id)[:5]]}
            return JsonResponse(info_product, status=200)
        else:
            return JsonResponse({"error": "User with id=" + str(item_id) + " doesn't exist"}, status=404)
