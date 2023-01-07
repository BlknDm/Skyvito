import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from ads.models import Categories


def get_main(request):
    return JsonResponse({"status": "ok"})


class CategoriesDetailView(DetailView):
    model = Categories

    def get(self, request, *args, **kwargs):
        categories = self.get_object()

        return JsonResponse({
            "id": categories.pk,
            "name": categories.name
        })


@method_decorator(csrf_exempt, name="dispatch")
class CatListCreateView(View):
    def get(self, request):
        cat_list = Categories.objects.all()
        return JsonResponse([{
            "id": cat.pk,
            "name": cat.name} for cat in cat_list], safe=False, json_dumps_params={'ensure_ascii': False})

    def post(self, request):
        ad_data = json.loads(request.body)
        new_cat = Categories.objects.create(**ad_data)
        return JsonResponse({
            "id": new_cat.pk,
            "name": new_cat.name
        })