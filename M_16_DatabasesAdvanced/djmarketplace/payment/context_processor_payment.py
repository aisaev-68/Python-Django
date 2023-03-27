from payment.models import Billing


def billing(request):
    return {'billing': Billing.objects.all().first()}