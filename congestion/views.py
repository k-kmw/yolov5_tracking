from rest_framework import viewsets

import congestion
from .serializers import ItemSerializer

from congestion.models import Bus
from django.http import JsonResponse
from . import weather

'''
def congestion_new(request):
    return render(request, "create.html")


def congestion_save(request):
    if request.method == 'POST':
        Bus.objects.create(peopleNumber=request.POST.get('peopleNumber'),
                           congestion=request.POST.get('congestion'))
        return redirect('congestion:index')
    else:
        return render(request, "create.html")


def congestion_list(request):
    all_congestion = Bus.objects.order_by("-pk")
    return render(request, "list.html", {'c_list': all_congestion})
'''


# Create your views here.
class ItemViewSet(viewsets.ModelViewSet):
    queryset = Bus.objects.all()
    serializer_class = ItemSerializer


def get_weather_data(request):
    data = weather.check_weather()
    return JsonResponse(data)
