import os
import re
from django.core.management import BaseCommand
from config.settings import BASE_URL
from testbase.models import RealEstateObject

class Command(BaseCommand):

    def handle(self, *args, **options):
        # filter_lst = []
        my_query  = 'cad_num=23&shirota=23&dolgota=23'
        # clear_query=re.compile("cad_num \(ts\/tv\) =")
        # clear_query = re.compile("cad_num=(.*)&")
        clear_query = re.compile("cad_num=(\d+)&")
        clear_query = clear_query.findall(my_query)[0]
        # filter_lst =RealEstateObject.objects.all().values_list('cad_num', 'shirota', 'dolgota') 
        print(clear_query)
    

        # token = Token.objects.create(user=request.user)
        # print(token.key)
        # print(os.path.join(BASE_URL,'/emulate_server'))
        # print(f'{BASE_URL}/emulate_server')

        
        # response = requests.get(f"{BASE_URL}?cad_num=23&shirota=25&dolgota=55")
        # print(response.json())
        # print(BASE_URL)
     