import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','crudfbv.settings')
import django
django.setup()

from testapp.models import Student
from faker import Faker
from random import randint

faker = Faker()

def populate(n):
    for _ in range(n):
        fsid = randint(1, 99)
        fsname = faker.name()
        fsage = randint(1, 50)
        fslocation = faker.city()
        Student.objects.create(sid=fsid, sname=fsname, sage=fsage, slocation=fslocation)

populate(20)
