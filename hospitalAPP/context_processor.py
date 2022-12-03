from .models import Departments


def menu_link(request):
    links = Departments.objects.all()
    return dict(links=links)