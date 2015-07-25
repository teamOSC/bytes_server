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
            filler['outlet_id'] = x.outlet_id

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


def createOutlets(request):

    name = request.GET.get('name')
    service_time = request.GET.get('serve')
    outlet_id = request.GET.get('out_id')
    cft = request.GET.get('cft')    # Cost For Two

    try:
        a = Outlets(name=name, service_time=service_time, cost_for_two=cft, outlet_id=outlet_id)
        a.save()
    except:
        return HttpResponse(json.dumps({'success': 'shubhamAgain'}))

    return HttpResponse(json.dumps({'success': 'shubham'}))


def getOutletInfo(request):
    try:
        outlet_id = request.GET.get('out_id')
        final_response = {}
        final_response['results'] = []
        a = Outlets.Query.filter(outlet_id=outlet_id)
        for x in a:
            filler = {}
            filler['item_name'] = x.item_name
            filler['outlet_id'] = x.outlet_id
            filler['item_id'] = x.item_id
            filler['item_rate'] = x.item_rate

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


def createOutletInfo(request):

    outlet_id = request.GET.get('out_id')
    item_name = request.GET.get('name')
    item_id = request.GET.get('item_id')
    item_rate = request.GET.get('rate')

    try:
        a = OutletInfo(outlet_id=outlet_id, item_id=item_id, item_name=item_name, item_rate=item_rate)
        a.save()
    except:
        return HttpResponse(json.dumps({'success': 'False'}))

    return HttpResponse(json.dumps({'success': 'True'}))


def createForm(request):
    return render_to_response('create_form.html')


def createInfoForm(request):
    return render_to_response('create_info.html')