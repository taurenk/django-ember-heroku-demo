
import json
import os
import urllib

from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.template import loader

from decouple import config
from pyquery import PyQuery as pq

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
            "heroku_metadata": {
                "HEROKU_APP_NAME": config('HEROKU_APP_NAME', "unknown"),
                "HEROKU_RELEASE_VERSION": config("HEROKU_RELEASE_VERSION", "unknown"),
                "HEROKU_RELEASE_CREATED_AT": config("HEROKU_RELEASE_CREATED_AT", "unknown")
            }
        }
    }
    return JsonResponse(data)


def ember(request, **kwargs):
    # DJANGO_ROOT = os.path.dirname(os.path.abspath(__file__))
    # PROJECT_ROOT = os.path.dirname(DJANGO_ROOT)
    ember = pq(filename=os.path.join(settings.DJANGO_ROOT,
                                     'static/index.html'))
    encoded_config = ember(
            '[name="super-rentals/config/environment"]').attr['content']
    config = json.loads(urllib.parse.unquote(encoded_config))
    # config.update(settings.EMBER_CONFIG)
    context = {
            'config': urllib.parse.quote(json.dumps(config)),
            # 'lr_enabled': settings.LIVERELOAD_ENABLED,
            # 'lr_port': settings.LIVERELOAD_PORT
            }
    # import pdb; pdb.set_trace()
    
    content = loader.render_to_string('index.html', context)

    return HttpResponse(content)
