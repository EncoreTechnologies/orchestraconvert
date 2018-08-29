from base_test_case import BaseActionTestCase

from orquestaconvert.client import Client


class TestClient(BaseActionTestCase):
    __test__ = True

    def test_parse_args

    def e2e_from_file(self, wf_filename):
        fixture_path = self.get_fixture_path('mistral/' + wf_filename)
        result = Client().convert_file(fixture_path)
        expected = self.get_fixture_content('orquesta/' + wf_filename)
        self.assertEquals(result, expected)

    def test_e2e_nasa_apod_twitter_post(self):
        self.e2e_from_file('nasa_apod_twitter_post.yaml')

    def test_e2e_nasa_apod_twitter_post(self):
        self.e2e_from_file('emptywee_test.yaml')
