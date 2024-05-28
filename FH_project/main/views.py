from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def index(request):
    return render(request, 'index.html')




from django.shortcuts import render, redirect
from django.http import HttpResponse
import g4f
from g4f.client import Client
from g4f.Provider import RetryProvider, Aichatos, Cnote, DuckDuckGo, Ecosia, Feedough


def profile(request):
    client = Client(
        provider=RetryProvider([Aichatos, Cnote, DuckDuckGo, Ecosia, Feedough], shuffle=False)
    )
    try:
        # if the session does not have a messages key, create one
        if 'messages' not in request.session:
            request.session['messages'] = [
                {"role": "assistant",
                 "content": "Привет! Я ИИ-помощник по питанию, чем я могу быть вам полезен?"},
            ]
        if request.method == 'POST':
            # get the prompt from the form
            prompt = request.POST.get('prompt')
            # get the temperature from the form
            temperature = float(request.POST.get('temperature', 0.1))
            # append the prompt to the messages list
            request.session['messages'].append({"role": "user", "content": prompt})
            # set the session as modified
            request.session.modified = True
            # call the openai API
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
            )
            # format the response
            formatted_response = response.choices[0].message.content
            # append the response to the messages list
            request.session['messages'].append({"role": "assistant", "content": formatted_response})
            request.session.modified = True
            # redirect to the home page
            context = {
                'messages': request.session['messages'],
                'prompt': '',
                'temperature': temperature,
            }
            return render(request, 'main.html', context)
        else:
            # if the request is not a POST request, render the home page
            context = {
                'messages': request.session['messages'],
                'prompt': '',
                'temperature': 0.1,
            }
            return render(request, 'main.html', context)
    except Exception as e:
        print(e)
        # if there is an error, redirect to the error handler
        return redirect('error_handler')


def new_chat(request):
    # clear the messages list
    request.session.pop('messages', None)
    return redirect('main:profile')




def foo():
    client = Client(
        provider=RetryProvider([Aichatos], shuffle=False)
    )
    messages = []
    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Exiting chat...")
            break  # Exit the loop to end the conversation
        messages.append({"role": "user", "content": user_input})

        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": "Hello"}],
            )
            gpt_response = response.choices[0].message.content
            print(f"Bot: {gpt_response}")
            messages.append({"role": "assistant", "content": gpt_response})
        except Exception as e:
            print(f"An error occurred: {e}")


# views.py
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.views import APIView
# from rest_framework.permissions import AllowAny
# from rest_framework.response import Response
# from rest_framework import status
# from django.contrib.auth.models import User
# import random
# import string
# from django.core.mail import send_mail

# @csrf_exempt  # Это отключает CSRF защиту для данного эндпоинта
# class PasswordResetAPIView(APIView):
#     permission_classes = [AllowAny]

#     def post(self, request):
#         serializer = PasswordResetSerializer(data=request.data)
#         if serializer.is_valid():
#             email = serializer.validated_data['mail_for_recovery']
#             try:
#                 user = User.objects.get(email=email)
#                 new_password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
#                 user.set_password(new_password)
#                 user.save()
                
#                 # Отправка письма с новым паролем
#                 send_mail(
#                     'Password Reset',
#                     f'Your new password is: {new_password}',
#                     'from@example.com',
#                     [email],
#                     fail_silently=False,
#                 )
                
#                 return Response({'message': 'A new password has been sent to your email.'}, status=status.HTTP_200_OK)
#             except User.DoesNotExist:
#                 return Response({'error': 'Email not registered in the system.'}, status=status.HTTP_404_NOT_FOUND)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# from django.contrib.auth import get_user_model
# from django.shortcuts import render
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.views import APIView
# from rest_framework.permissions import AllowAny
# from rest_framework.response import Response
# from rest_framework import status
# from django.core.mail import send_mail
# import random
# import string

# # Импорт вашего сериализатора
# from .serializers import PasswordResetSerializer

# # Представление для главной страницы
# def index(request):
#     return render(request, 'index.html')

