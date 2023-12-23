from django.test import SimpleTestCase
from django.urls import reverse, resolve
from budget.views import project_list, project_detail, ProjectCreateView

class TestUrls(SimpleTestCase):

    def test_list_url_is_resolved(self):
        url = reverse('list')
        # print(f'your url {url}')
        print(resolve(url))
        self.assertEquals(resolve(url).func, project_list)

    def test_add_url_is_resolved(self):
        url = reverse('add')
        # print(f'your url {url}')
        print(resolve(url))
        # resolve_url = resolve(url)
        self.assertEquals(resolve(url).func.view_class, ProjectCreateView)

    def test_detail_url_is_resolved(self):
        url = reverse('detail', kwargs={'project_slug': 'your_project_slug'})
        # print(f'your url {url}')
        # print(f'project_details {project_detail}')
        self.assertEquals(resolve(url).func, project_detail)
