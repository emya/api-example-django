# Create your views here.
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.conf import settings
import datetime, pytz, requests

def index(request):
    key = settings.SOCIAL_AUTH_DRCHRONO_KEY
    secret = settings.SOCIAL_AUTH_DRCHRONO_SECRET
    scope = settings.SOCIAL_AUTH_DRCHRONO_SCOPE
    redirect = settings.LOGIN_REDIRECT_URL
    variables = RequestContext(request, {'key':key, 'secret':secret, 'scope':scope, 'redirect':redirect})

    return render_to_response('index.html', variables, )

def token_exchange(request):
    err = request.GET.get('error', '')
    if err:
    	raise ValueError('Error authorizing application: %s' % err)

    redirectURI = settings.LOGIN_REDIRECT_URL
    key = settings.SOCIAL_AUTH_DRCHRONO_KEY
    secret = settings.SOCIAL_AUTH_DRCHRONO_SECRET
    code = request.GET.get('code', '')
    response = requests.post('https://drchrono.com/o/token/', data={
	    #'refresh_token': code,
	    'code': code, 
	    'grant_type': 'authorization_code',
	    'redirect_uri': redirectURI,
	    'client_id': key,
	    'client_secret': secret,
    })
    response.raise_for_status()
    data = response.json()

    # Save these in your database associated with the user
    access_token = data['access_token']
    refresh_token = data['refresh_token']
    expires_timestamp = datetime.datetime.now(pytz.utc) + datetime.timedelta(seconds=data['expires_in'])

    """
    # When refresh an access token

    response = requests.post('https://drchrono.com/o/token/', data={
	    #'refresh_token': code,
	    'grant_type': 'refresh_token',
	    'client_id': key,
	    'client_secret': secret,
    })

    """

    return redirect('userhome')

def userhome(request):
    variables = RequestContext(request, {})
    return render_to_response('userhome.html', variables, )

