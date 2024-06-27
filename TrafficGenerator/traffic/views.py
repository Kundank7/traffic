# traffic/views.py

from django.shortcuts import render
from .forms import TrafficForm
import requests
import random
import time

# List of user agents to simulate different browsers and devices
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0"
]

def generate_traffic(request):
    if request.method == 'POST':
        form = TrafficForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            views = form.cleaned_data['views']

            for _ in range(views):
                user_agent = random.choice(user_agents)
                headers = {'User-Agent': user_agent}
                try:
                    response = requests.get(url, headers=headers)
                    print(f"Request to {url} sent with user agent: {user_agent}, Response code: {response.status_code}")
                except Exception as e:
                    print(f"Error sending request: {e}")

                # Sleep for a random amount of time between 1 and 5 seconds
                time.sleep(random.uniform(1, 5))
        else:
            print(f"Form errors: {form.errors}")
    else:
        form = TrafficForm()

    return render(request, 'traffic/generate_traffic.html', {'form': form})
