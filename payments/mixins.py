from django.http import JsonResponse


class StripeCheckoutMixin:
    """Общая логика создания Stripe session для DetailView."""

    stripe_method = None

    def get_stripe_object(self):
        return self.get_object()

    def get_stripe_session(self, obj, request):
        raise NotImplementedError

    def get(self, request, *args, **kwargs):
        obj = self.get_stripe_object()
        try:
            session = self.get_stripe_session(obj, request)
            return JsonResponse({'session_id': session.id})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)