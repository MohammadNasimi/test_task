from django.contrib.auth.models import User
from django.test import TestCase

# Create your tests here.
from django.urls import reverse


class RegisterViewTest(TestCase):

    def test1_list_receipt_get_form(self):
        url = reverse('list_view')  # auth/register
        response = self.client.get(url)
        # print('A:',response.content)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'orders')
        self.assertContains(response, 'discount_all')

    # def test2_register_post_success(self):
    #     url = reverse('register_view')
    #     user_info = {
    #         'username': 'akbar',
    #         'password': 'akbar',
    #         'first_name': 'akbar',
    #         'last_name': 'babaii',
    #     }
    #     response = self.client.post(url, data=user_info)
    #
    #     self.assertEqual(response.status_code, 200)
    #     self.assertContains(response, "User registered by ID:")
    #
    #     self.assertIn(
    #             user_info['username'],
    #             list(User.objects.values_list('username', flat=True))
    #             )
