from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.

class SnickersTest(SimpleTestCase):
  def test_home_page_status(self):
      url = reverse('home')
      response = self.client.get(url)
      expected = 200
      self.assertEqual(response.status_code, expected)

  def test_home_page_template_two(self):
      self.helper_status_code_200('home')
  
  def test_home_page_template(self):
      url = reverse('home')
      response = self.client.get(url)
      self.assertTemplateUsed(response, 'home.html')
      self.assertTemplateUsed(response, 'base.html')
  
  def test_about_page_status(self):
      url = reverse('about')
      response = self.client.get(url)
      expected = 200
      self.assertEqual(response.status_code, expected)


  def helper_status_code_200(self, url_name):
      url = reverse(url_name)
      response = self.client.get(url)
      self.assertTemplateUsed(response, 'home.html')
      self.assertTemplateUsed(response, 'base.html')