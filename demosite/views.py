from django.http import JsonResponse

def health_check(request):
    data = {
        "results": {
            "status": "ok"
        }
    }
    return JsonResponse(data)
