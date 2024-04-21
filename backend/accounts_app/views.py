from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework import permissions
from django.contrib import auth
from rest_framework.response import Response
from profile_app.models import UserProfile
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
from django.utils.decorators import method_decorator


# Create your views here.

class CheckAuthenticatedView(APIView):
    def get(self, request, format=None):
        # ?  **SEE COMMENT 1 Below **
        user = self.request.user

        try:
            isAuthenticated = user.is_authenticated
            # TODO UPDATE RESPONSE MESSAGES WITH STATUS CODE AND BETTER MESSAGES
            if isAuthenticated:
                return Response({isAuthenticated: "success"})
            else:
                return Response({isAuthenticated: "error"})

        except Exception as e:
            return Response({'error': f"Something went wrong during authentication status query: {str(e)}"})

# ? **Ensures You Need a CSRF Token for the View**


@method_decorator(csrf_protect, name='dispatch')
class SignupView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        data = self.request.data

        username = data['email']
        email = data['email']
        password = data['password']
        re_password = data['re_password']

        try:
            if password == re_password:
                if User.objects.filter(email=email).exists():
                    return Response({'error': "Email is already registered to an account"})
                else:
                    #! **OPTIONAL PASSWORD VALIDATION**
                    if len(password) < 6:
                        return Response({'error': 'Password Must Be More THan 6 Characters'})
                    else:
                        user = User.objects.create_user(
                            username=username, email=email,  password=password)

                        # user = User.object.get(email=user.email)
                        # ! Can remove if we dont want it, though it might be good to be tied but blank to the auth-user
                        user = User.objects.get(id=user.id)
                        # links authentication user to user profile using the id

                        user_profile = UserProfile.objects.create(
                            user=user, first_name="", last_name="", city="", state="")
                        # ! *** ADJUST ALONG WITH USER MODEL ***

                        return Response({"user": user, "success": 'User successfully created'})
            else:
                return Response({'error': "Passwords do not match"})
        except Exception as e:
            return Response({'error': f"An error occurred during account registration: {str(e)}"})
            # This method will show the error to provide more information


# ? **Ensures You Need a CSRF Token for the View**
@method_decorator(csrf_protect, name='dispatch')
class LoginView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        data = self.request.data

        username = data['email']
        password = data["password"]

        try:
            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return Response({"success": 'User Authenticated'})
            else:
                return Response({"error": 'Unable to Authenticate User'})
        except Exception as e:
            return Response({'error': f"An error occurred during login: {str(e)}"})


class LogoutView(APIView):
    def post(self, request, format=None):
        try:
            auth.logout(request)
            return Response({"success": 'Logged Out'})
        except:
            return Response({"error": 'An Error Occurred Logging Out'})


# ? **Gives CSRF Cookie when accessed in application**
@method_decorator(ensure_csrf_cookie, name='dispatch')
class GetCSRFToken(APIView):
    permission_classes = (permissions.AllowAny, )

    def get(self, request, format=None):
        return Response({"success": 'CSRF Cookie Set'})


class DeleteAccountView(APIView):
    def delete(self, request, format=None):
        user = self.request.user

        try:
            User.objects.filter(id=user.id).delete()
            return Response({"success": 'User Successfully Deleted'})
        except:
            return Response({"error": 'An Error Occurred Deleting the User'})


# ? ***COMENT 1****
# In Django REST Framework views, the format =None parameter is often used in conjunction with the request parameter to specify the desired response format, such as JSON or HTML. When a request is made to an API endpoint, the format parameter allows the client to specify the desired format in the URL, typically using suffixes like .json or .xml. The format=None argument in the view method signature allows the view to handle requests with or without a specified format gracefully. If no format is specified in the URL, the default behavior is usually to return the response in the format specified by the DEFAULT_RENDERER_CLASSES setting in Django REST Framework.
