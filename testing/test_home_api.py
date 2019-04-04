from django.test import Client
from django.urls import reverse
from testing.base import Base


class TestHomeApi(Base):
    def test_home_api(self):
        client = Client()
        r = client.get(reverse('home', kwargs={}))
        assert r.status_code == 200
        assert r.data == "Welcome!"
