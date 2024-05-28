from django.shortcuts import render, redirect
from django.http import HttpResponse
import g4f
from g4f.client import Client
from g4f.Provider import RetryProvider, Aichatos, Cnote, DuckDuckGo, Ecosia, Feedough


def home(request):
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
            return render(request, 'askgpt/home.html', context)
        else:
            # if the request is not a POST request, render the home page
            context = {
                'messages': request.session['messages'],
                'prompt': '',
                'temperature': 0.1,
            }
            return render(request, 'askgpt/home.html', context)
    except Exception as e:
        print(e)
        # if there is an error, redirect to the error handler
        return redirect('error_handler')


def new_chat(request):
    # clear the messages list
    request.session.pop('messages', None)
    return redirect('home')


def error_handler(request):
    return render(request, 'askgpt/404.html')


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