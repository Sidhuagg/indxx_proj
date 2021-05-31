from django.core.management.base import BaseCommand, CommandError
from dashboard.models import airdata as tdata
import requests
import json

class Command(BaseCommand):
    help = 'Fetches api data'

    """def add_arguments(self, parser):
        none"""


    def handle(self, *args, **options):

        #for a in range(0,1578,10):
        a = True
        offno = 0
        lst1=[]
        while a == True:
            api_key = "579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b"
            url = "https://api.data.gov.in/resource/3b01bcb8-0b14-4abf-b6f2-c1bfd384ba69?api-key={}&format=json&offset={}&limit=10".format(api_key,offno)
            response = requests.get(url)
            data = response.text
            a1=json.loads(data)
            for x in a1['records']:
                lst1.append(x)
            if a1["count"] < 10:
                a= False
            offno += 10
        airdata1 = json.loads(data)
        airdata1['records']=lst1
        ad = json.dumps(airdata1,indent=2)
        tdata.objects.bulk_create(lst1)
        return ad
   
        """with open("air.txt", "a") as file:

            file.write(airdata)"""
