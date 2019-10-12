from django.http import JsonResponse
from decouple import config

def home(request):
    data = {
        "results": {
            "message": "welcome home"
        }
    }
    return JsonResponse(data)

def health_check(request):
    data = {
        "results": {
            "status": "ok",
            "metadata": {
                "HEROKU_APP_NAME": config('HEROKU_APP_NAME', "unknown"),
                "HEROKU_RELEASE_VERSION": config("HEROKU_RELEASE_VERSION", "unknown"),
                "HEROKU_RELEASE_CREATED_AT": config("HEROKU_RELEASE_CREATED_AT", "unknown")
            }
        }
    }
    return JsonResponse(data)
