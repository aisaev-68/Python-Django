from .models import Catalog


def catalogs(request):
    return {'catalogs': Catalog.objects.all()}
