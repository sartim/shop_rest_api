from tests.base import Base


class TestHomeApi(Base):
    def test_home_api(self):
        r = self.client.get('/')
        assert r.status_code == 200
        assert r.data == "Welcome!"
