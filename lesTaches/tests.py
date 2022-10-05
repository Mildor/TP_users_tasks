from django.urls import reverse
from django.test import TestCase
from django.urls.exceptions import NoReverseMatch
from lesTaches.models import Task, User


# browser = webdriver.Chrome(service=ChromeService("C:/chromedriver/chromedriver.exe"))

class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(email="test@user.fr", username="testUser")
        User.objects.create(email="test1@user.fr", username="test1User")

    def test_user_url_name(self):
        try:
            url = reverse('UserForm-edit', args=[1])
        except NoReverseMatch:
            assert False

    def test_user_url(self):
        user = User.objects.get(email='test@user.fr')
        userdeu = User.objects.get(email='test1@user.fr')
        url = reverse('UserForm-edit', args=[user.pk])
        urldeu = reverse('UserForm-edit', args=[userdeu.pk])
        response = self.client.get(url)
        responsedeu = self.client.get(urldeu)
        assert response.status_code == 200
        assert responsedeu.status_code == 200
        user.delete()
        userdeu.delete()

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
        tachedeu = Task.objects.get(name='Test Case1')
        tachetroi = Task.objects.get(name='Test Case2')
        url = reverse('details', args=[tache.pk])
        urldeu = reverse('details', args=[tachedeu.pk])
        urltroi = reverse('details', args=[tachetroi.pk])
        response = self.client.get(url)
        responsedeu = self.client.get(urldeu)
        responsetrois = self.client.get(urltroi)
        assert response.status_code == 200
        assert responsedeu.status_code == 200
        assert responsetrois.status_code == 200
        tache.delete()
        tachedeu.delete()
        tachetroi.delete()
