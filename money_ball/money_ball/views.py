from django.http import JsonResponse

def home(request):
    return JsonResponse({"message": "Welcome to Money Ball API"})
