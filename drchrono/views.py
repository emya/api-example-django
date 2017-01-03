# Create your views here.
from django.shortcuts import render_to_response
from django.conf import settings

def index(request):
    key = settings.SOCIAL_AUTH_DRCHRONO_KEY
    secret = settings.SOCIAL_AUTH_DRCHRONO_SECRET
    scope = settings.SOCIAL_AUTH_DRCHRONO_SCOPE
    redirect = settings.LOGIN_REDIRECT_URL
    variables = RequestContext(request, {'key':key, 'secret':secret, 'scope':scope, 'redirect':redirect})

    return render_to_response('index.html', variables, )
