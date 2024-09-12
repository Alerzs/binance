from celery import shared_task
from .models import Shart
import requests
import json


@shared_task
def my_task(self):
    for item in Shart.objects.all():
        ramzarz = item.arz
        url = "https://api.nobitex.ir/market/stats?srcCurrency="+ ramzarz +"&dstCurrency=rls"
        response = requests.get(url)
        cur_price = json.loads(response.content)["stats"][f"{ramzarz}-rls"]["latest"]
        if cur_price >= item.price:
            print("warningggggggg")

    