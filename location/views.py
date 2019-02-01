from disccourse.location.models import *
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render_to_response

@login_required
def create(request):
    if request.method == "GET":
        return render_to_response("location/create.html", context_instance = RequestContext(request, {}))
    else:

        # redirect to read

@login_required
def read(request, location_id):
    pass

@login_required
def update(request, location_id):
    pass

@login_required
def delete(request, location_id):
    pass
