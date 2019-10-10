from django.http import JsonResponse


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
            "status": "ok"
        }
    }
    return JsonResponse(data)
