from tests.base import Base


class TestProduct(Base):
    def test_get_all(self):
        r = self.client.get('/api/v1/product/')
        assert r.status_code == 200
