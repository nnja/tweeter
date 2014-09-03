from django.core.urlresolvers import reverse
from rest_framework.test import APITestCase, APIClient


class TweetTests(APITestCase):
    def test_create_invalid_tweet(self):
        self.client = APIClient()
        self.client.login(username='bob', password='bob')
        url = reverse('tweet-list')
        data = {'text': "x" * 4}
        response = self.client.post(url, data, format='json')
        error_msg = response.data['text'][0]

        self.assertEquals(response.status_code, 400)
        self.assertEquals(error_msg, 'Text is too short!')
