from django.utils import timezone
from Visitor_App.models import *

class UserTrackingMiddleware:

    def __init__(self, get_response):
        # Runs once when server starts
        self.get_response = get_response
        print("UserTrackingMiddleware Initialized")

    def __call__(self, request):
        # Runs for every request

        # Get username from URL query
        username = request.GET.get('user')


        # -------------------------------
        # LOGIN LOGIC
        # -------------------------------
        if request.path == '/home/'  and username:
            try:
                # Get user from database
                user = UserProfile.objects.get(username = username)

                # Create a new login record
                active_login = UserLoginActivity.objects.filter(
                    user=user,
                    logout_time__isnull=True
                ).exists()

                # If NOT logged in → create new login record
                if not active_login:
                    UserLoginActivity.objects.create(
                        user=user,
                        login_time=timezone.now()
                    )
            except UserProfile.DoesNotExist:
                pass

        # -------------------------------
        # LOGOUT LOGIC
        # -------------------------------
        if request.path == '/logout/' and username:
            try:
                # Get user
                user = UserProfile.objects.get(username = username)

                # Get last login activity with no logout time
                activity = UserLoginActivity.objects.filter(
                    user=user,
                    logout_time__isnull=True
                ).last()

                if activity:
                    # Set logout time
                    activity.logout_time = timezone.now()

                    # Calculate total time in seconds
                    activity.total_seconds = int(
                        (activity.logout_time - activity.login_time).total_seconds()
                    )

                    activity.save()

            except UserProfile.DoesNotExist:
                pass


        # Continue request-response cycle
        response = self.get_response(request)
        return response