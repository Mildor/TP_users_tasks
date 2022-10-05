from django.urls import reverse
from django.test import TestCase
from django.urls.exceptions import NoReverseMatch
from lesTaches.models import Task, User


# browser = webdriver.Chrome(service=ChromeService("C:/chromedriver/chromedriver.exe"))

class TacheTestCase(TestCase):
    def setUp(self):
        firstUser = User.objects.create(email="test@test.fr", username="test")
        secondUser = User.objects.create(email="test1@test.fr", username="test1")
        Task.objects.create(name="Test Case", description="Description de test case", closed=False,
                            due_date="2022-10-05", schedule_date="2022-10-15", owner=firstUser)
        Task.objects.create(name="Test Case1", description="Description de test case1", closed=False,
                            due_date="2022-10-05", schedule_date="2022-10-15", owner=secondUser)
        Task.objects.create(name="Test Case2", description="Description de test case2", closed=False,
                            due_date="2022-10-05", schedule_date="2022-10-15", owner=firstUser)

    def test_tache_url_name(self):
        try:
            url = reverse('details', args=[1])
        except NoReverseMatch:
            assert False

    def test_tache_url(self):
        tache = Task.objects.get(name='Test Case')
        url = reverse('details', args=[tache.pk])
        response = self.client.get(url)
        assert response.status_code == 200
