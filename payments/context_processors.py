from django.conf import settings


def stripe_public_key(request):
    return {
        'stripe_public_key': settings.STRIPE_PUBLISHABLE_KEY,
    }
