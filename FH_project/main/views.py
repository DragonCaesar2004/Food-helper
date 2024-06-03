from django.shortcuts import render
from django.shortcuts import render, redirect
import g4f
from g4f.client import Client
from g4f.Provider import RetryProvider, Phind, FreeChatgpt, Liaobots,Cnote, DuckDuckGo, Ecosia, Blackbox

def index(request):
    return render(request, 'index.html')

def profile(request):
    client = Client(
        provider=RetryProvider([Blackbox], shuffle=False)
    )
    try:
        if 'messages' not in request.session:
            request.session['messages'] = [
                {"role": "assistant",
                 "content": "Привет! Я ИИ-помощник по питанию, чем я могу быть вам полезен?"},
            ]
        if request.method == 'POST':
            prompt = request.POST.get('prompt')
            additional_text = request.POST.get('additional_text', '')
            full_prompt = f"{additional_text}\n{prompt}"
            temperature = float(request.POST.get('temperature', 0.1))
            request.session['messages'].append({"role": "user", "content": prompt})
            request.session.modified = True
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": full_prompt}],
            )
            formatted_response = response.choices[0].message.content
            request.session['messages'].append({"role": "assistant", "content": formatted_response[13:]})
            request.session.modified = True
            context = {
                'messages': request.session['messages'],
                'prompt': '',
                'temperature': temperature,
            }
            return render(request, 'main.html', context)
        else:
            context = {
                'messages': request.session['messages'],
                'prompt': '',
                'temperature': 0.1,
            }
            return render(request, 'main.html', context)
    except Exception as e:
        print(e)
        return redirect('main:error_handler')

def new_chat(request):
    request.session.pop('messages', None)
    return redirect('main:profile')

def error_handler(request):
    return render(request, '404.html')
