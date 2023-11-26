from django.http import HttpResponse
import requests
import io
from PIL import Image
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import os
import json

def home(request):
    return render(request, 'home.html')


API_URL = "https://xdwvg9no7pefghrn.us-east-1.aws.endpoints.huggingface.cloud"
headers = {
	"Accept": "image/png",
	"Authorization": "Bearer VknySbLLTUjbxXAXCjyfaFIPwUTCeRXbFSOjwRiCxsxFyhbnGjSFalPKrpvvDAaPVzWEevPljilLVDBiTzfIbWFdxOkYJxnOPoHhkkVGzAknaOulWggusSFewzpqsNWM",
	"Content-Type": "application/json"
}

@csrf_exempt
def query(request):
    if request.method == 'POST':
        try:
            # Extract input text from the request payload
            payload = json.loads(request.body)
            input_text = payload.get('inputs', '')

            # Make the API call
            response = requests.post(API_URL, headers=headers, json={"inputs": "cat"})
            print("hello")

            if response.ok:
                # If the response is successful, return the image content
				
                return JsonResponse({'image': response.content.decode('utf-8')})
            else:
                # If the response is not successful, return an error message
                return JsonResponse({'error': 'Failed to fetch image'}, status=500)
        except json.JSONDecodeError:
            # Handle JSON decoding error
            return JsonResponse({'error': 'Invalid JSON payload'}, status=400)
    else:
        # Return an error for unsupported HTTP methods
        return JsonResponse({'error': 'Invalid request method'}, status=400)

