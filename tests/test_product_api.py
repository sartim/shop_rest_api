from rest_framework.test import APIClient
from tests.base import Base


class TestProduct(Base):
    def test_get_all(self):
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(self.token))
        response = self.client.get(self.product_url, format='json')
        assert response.status_code == 200

    def test_get_by_id(self):
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(self.token))
        response = self.client.get('{}1'.format(self.product_url), format='json')
        assert response.status_code == 200

    def test_post(self):
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(self.token))
        data = {
            "category": 1,
            "name": "Sanus VLF410B2 10-Inch Mount for 84 Inches TV's",
            "slug": "sanus-vlf410b1-10-inch-mount-for-84-inches-tvs",
            "description": "",
            "price": "105.99",
            "stock": 10,
            "available": True
        }
        response = self.client.post(self.product_url, data=data, format='json')
        assert response.status_code == 201

    def test_put(self):
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(self.token))
        data = {
            "description": "some description for product"
        }
        response = self.client.get(
            '{}1'.format(self.product_url), data=data, format='json')
        assert response.status_code == 200

    def test_delete(self):
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(self.token))
        response = self.client.delete(
            '{}1'.format(self.product_url))
        assert response.status_code == 200
