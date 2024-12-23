# users/views.py
from decouple import config
from google.oauth2 import id_token
from google.auth.transport.requests import Request

from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.exceptions import AuthenticationFailed

from rest_framework_simplejwt.tokens import RefreshToken


class GoogleLoginAPIView(APIView):
    permission_classes = [AllowAny]  # Leave it as it is

    """
    Please do modify the codes but not the logic.
    """

    def post(self, request):
        """
        Returns tokens for new or existing google users.
        NB: use it as templates for other social auth apps as well.

        :param request:(HttpRequest)
            - body:
                - access_token: (str)
        :return Response:(JsonResponse)
        """

        # Fetch the token from body data
        google_token = request.data.get('access_token')

        print(google_token, "----------Google Token Type-----------")

        if not google_token:
            raise AuthenticationFailed('Token is missing')

        try:
            # Verify the token with Google
            idinfo = id_token.verify_oauth2_token(
                google_token,
                Request(),
                config('GOOGLE_CLIENT_ID'),
                clock_skew_in_seconds=30,
            )

            # idinfo = request.get("https://www.googleapis.com/oauth2/v3/userinfo", headers={"Authorization": f"Bearer {google_token}"})

            print(idinfo, "----------IDInfo Get From Google-----------")  # if you need for info what google returns us back

            # Check if the user already exists
            user, created = User.objects.get_or_create(
                username=idinfo['email'],
                defaults={
                    'email': idinfo['email'],
                    'first_name': idinfo['name']
                }
            )

            # If the user is new, we set up the user (fields such as username, email, etc. could be modified)
            if created:
                user.set_unusable_password()  # Since the user is logging in via Google, no password is set
                user.save()

            # Generate a JWT token
            refresh = RefreshToken.for_user(user)

            # Do your magic here, I've done it for only testing.
            return Response({
                'access_token': str(refresh.access_token),
                'refresh_token': str(refresh),
            })

        except ValueError as error:
            raise AuthenticationFailed(f'Error verifying Google token: {str(error)}')


class UserInfoAPIView(APIView):

    """
    Test endpoint to see the token we return works after google sign in.
    Hit post man to see it in action
    """

    # Authentication class
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        Return basic user data for verifying purpose only.
        :param request:(HttpRequest)
        :return Response:(JsonResponse)
        """

        return Response(
            {
                "user_id": request.user.id,
                "user_email": request.user.email,
                "user_name": request.user.first_name,
            }, status=status.HTTP_200_OK
        )
