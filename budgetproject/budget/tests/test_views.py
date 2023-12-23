from django.test import Client, TestCase
from django.urls import reverse
from budget.models import Project, Category, Expense
import json

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.list_url = reverse('list')
        self.detail_url = reverse('detail', args = ['project1'])
        self.project1 = Project.objects.create(
            name = 'project1',
            budget = 10000
        )

    def test_project_list_GET(self):
        response = self.client.get(reverse('list'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'budget/project-list.html')

    def test_project_detail_GET(self):
        response = self.client.get(self.detail_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'budget/project-detail.html')

    def test_project_detail_POST_adds_new_expense(self):
        Category.objects.create(
            Project=self.project1,
            name='development'
        )

        response = self.client.post(self.detail_url, {
            'title'
        })
