import re
import time

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
from django.test import TestCase
from django.urls.exceptions import NoReverseMatch
from lesTaches.models import Task, User
from django.urls import resolve
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from lesTaches.views import task_nav, task_listing, user_choice, task_details, task_form, task_edit, task_delete, \
    user_form, user_edit, user_delete


class FunctionalTest(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.options = Options()
        cls.options.add_argument("--headless")
        cls.browser = Chrome(executable_path='C:/chrome_driver/chromedriver.exe', options=cls.options)
        cls.browser.implicitly_wait(3)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super().tearDownClass()

    def test_can_show_task_list(self):
        self.browser.get("http://127.0.0.1:8000/lesTaches/")
        self.assertIn("Que souhaitez vous faire ?", self.browser.title)
        #self.fail()

    def test_add_delete_task(self):
        browser = Chrome(executable_path='C:/chrome_driver/chromedriver.exe')
        browser.get("http://127.0.0.1:8000/lesTaches/addTask/")
        time.sleep(1)
        name = browser.find_element_by_id("id_name")
        desc = browser.find_element_by_id("id_description")
        closed = browser.find_element_by_id("id_closed")
        due_date = browser.find_element_by_id("id_due_date")
        schedule_date = browser.find_element_by_id("id_schedule_date")
        owner = browser.find_element_by_xpath("//select[@name='owner']/option[@value='1']")

        name.send_keys("Quizz a rendre")
        time.sleep(1)
        desc.send_keys("c'est un test pour voir si ajouter avec un test ca fonctionne")
        time.sleep(1)
        closed.click()
        time.sleep(1)
        due_date.send_keys("05-10-2022")
        time.sleep(1)
        schedule_date.send_keys("05-11-2022")
        time.sleep(1)
        owner.click()
        time.sleep(1)

        browser.find_element_by_id("submit").click()
        time.sleep(1)

        titre_tache = browser.find_element_by_css_selector(".card-header>h2")
        tache_found = False
        elem = None

        if "Quizz a rendre" == titre_tache.text:
            tache_found = True
            elem = titre_tache

        self.assertEqual(True, tache_found)

        browser.find_element_by_id("delete").click()
        time.sleep(10)

        titles = browser.find_elements_by_class_name("widget-heading")
        tache_found = True

        for title in titles:
            if 'Quizz a rendre' == title.text:
                tache_found = False

        self.assertEqual(True, tache_found)
        browser.quit()

    #def test_add_delete_user(self):



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
