import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chandrayan.settings")

import django
django.setup()

from faker import Faker
from rover.userdetails import accdata

fakeobj = Faker()
def fillit(N=5):
    for entry in range(N):
        namef = fakeobj.name()
        emailf = fakeobj.email()

        accdataf = accdata.objects.get_or_create(username=namef,emailid=emailf)[0]

if __name__ == '__main__':
    print("populating the userdata!")
    fillit(20)
    print("populating complete!")
