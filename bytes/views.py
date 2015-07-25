from django.shortcuts import render, HttpResponse, render_to_response
from models import *
import json, requests, copy

# Create your views here.


def mainPage(request):
    return HttpResponse("Shubham")


def getOutlets(request):

    try:
        final_response = {}
        final_response['results'] = []
        a = Outlets.Query.all()
        for x in a:
            filler = {}
            filler['name'] = x.name
            filler['min_service_time'] = x.service_time
            filler['cost_for_two'] = x.cost_for_two

            final_response['results'].append(copy.deepcopy(filler))

        final_response['success'] = True

        resp = {
            'success': 'True',
            'result': [
                {
                    'name': '',
                    'min_service_time': '',
                    'cost_for_two': ''
                },
            ]
        }

        return HttpResponse(json.dumps(final_response))
    except:
        return HttpResponse(json.dumps({'success': 'False'}))

    return HttpResponse(json.dumps({'success': 'partly True'}))


def createOutlets(request):

    name = request.GET.get('name')
    service_time = request.GET.get('serve')
    cft = request.GET.get('cft')    # Cost For Two

    try:
        a = Outlets(name=name, service_time=service_time, cost_for_two=cft)
        a.save()
    except:
        return HttpResponse(json.dumps({'success': 'False'}))

    return HttpResponse(json.dumps({'success': 'True'}))