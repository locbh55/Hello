from django.shortcuts import render_to_response
from django.template import RequestContext

counter = [0]

def index(request):
    counter[0] = counter[0] + 1
    if request.is_ajax():
        template = "index_ajax.html"
    else:
        template = "index.html"
    return render_to_response(template,
                              {'counter': str(counter[0])},
                        context_instance=RequestContext(request))