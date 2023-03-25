from shopapp.models import Shop


def shop(request):
    return {'shops': Shop.objects.all()}