import unittest

from rest_framework.test import APIClient
from tests.base import Base


class TestProduct(Base):
    def test_get_all(self):
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(self.token))
        response = self.client.get(self.product_url, format='json')
        assert response.status_code == 200
        print(response.data)

    @unittest.skip("TODO")
    def test_get_by_id(self):
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(self.token))
        response = self.client.get('{}1'.format(self.product_url), format='json')
        assert response.status_code == 200

    @unittest.skip("TODO")
    def test_post(self):
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(self.token))
        data = {}
        response = self.client.post(self.product_url, data=data, format='json')
        assert response.status_code == 201
