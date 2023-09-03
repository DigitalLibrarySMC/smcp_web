# custom_middleware.py
from django.conf import settings
class SessionTimeoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if 'session_timeout_extend' in request.session:
            # If the user clicked "OK," extend the session expiration time
            request.session.modified = True  # Ensure the session is saved
            request.session['session_timeout_extend'] = False  # Reset the flag

            # Update the session cookie's expiration time (extend it)
            response.set_cookie(
                settings.SESSION_COOKIE_NAME,
                request.session.session_key,
                max_age=settings.SESSION_COOKIE_AGE,
                expires=None,  # Expire the cookie when the session ends
                samesite=None,
                secure=request.is_secure(),
            )

        return response
