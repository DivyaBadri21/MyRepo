import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crudDemo.settings')

import django
django.setup()

from crudApp.models import *
from faker import Faker
from random import *
faker = Faker()

def generate(n):
    for i in range(n):
        fsno = randint(1,1001)
        fsname = faker.name()
        fsclass = randint(1,10)
        fsaddress = faker.city()
        stud_record = Student.objects.get_or_create(sno = fsno,sname = fsname,sclass = fsclass,saddress = fsaddress)
        

generate(10)