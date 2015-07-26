from django.shortcuts import render, HttpResponse, render_to_response
from models import *
import json, requests, copy
import random
from parse_rest.installation import Push

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
        a = OutletInfo.Query.filter(outlet_id=outlet_id)
        #print a
        for x in a:
            #print x
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
        return HttpResponse(json.dumps({'success': 'something went wrong'}))


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


def billing(request):

    query = request.GET.get('q')
    user_id = int(request.GET.get('user_id'))
    username = request.GET.get('username')

    data = query.split('|')

    final_data = {}
    for x in data:
        filler = {}
        requested_data = x.split(',')
        a = OutletInfo.Query.get(outlet_id=requested_data[0], item_id=requested_data[1])
        print a
        b = Outlets.Query.get(outlet_id=requested_data[0])


        try:
            final_data[a.outlet_id]['cost'] += int(int(a.item_rate) * int(requested_data[2]))
            final_data[a.outlet_id]['time'] += int(float(float(b.service_time)/5.0) * float(requested_data[2]))
        except:
            final_data[a.outlet_id] = {}
            final_data[a.outlet_id]['name'] = b.name
            final_data[a.outlet_id]['outlet_id'] = a.outlet_id
            final_data[a.outlet_id]['cost'] = int(int(a.item_rate) * int(requested_data[2]))
            final_data[a.outlet_id]['time'] = int(float(float(b.service_time)/5.0) * float(requested_data[2]))

        filler['cost'] = str(int(a.item_rate) * int(requested_data[2]))
        filler['time'] = str(int(float(b.service_time)/5.0) * int(requested_data[2]))
        c = Order(item_name=a.item_name, outlet_id = a.outlet_id, outlet_name=b.name, item_id=a.item_id,
                  cost=filler['cost'], time=filler['time'], qty=int(requested_data[2]), name=username, user_id=user_id,
                  order_number='GREPLR'+str(a.outlet_id)+str(a.outlet_id)+str(a.outlet_id)+str(username)+'2718'+str(user_id)+'x005F')
        c.save()
        print c.qty

    response_data = []

    for key in final_data:
        response_data.append(copy.deepcopy(final_data[key]))


    return HttpResponse(json.dumps(response_data))


def dashboardAPI(request, outlet_id):

    # fetch data from parse it it exists for every user
    x = Order.Query.filter(outlet_id=outlet_id)
    final_data = {}

    for data in x:
        try:
            final_data[data.user_id]['amount'] += int(data.cost)
            filler = {}
            filler['item'] = data.item_name
            filler['quantity'] = data.qty
            final_data[data.user_id]['order'].append(filler)
        except:
            final_data[data.user_id] = {}
            final_data[data.user_id]['user_id'] = data.user_id
            final_data[data.user_id]['username'] = data.name
            final_data[data.user_id]['outlet_name'] = data.outlet_name
            final_data[data.user_id]['order_id'] = data.order_number
            final_data[data.user_id]['amount'] = int(data.cost)
            final_data[data.user_id]['order'] = []
            filler = {}
            filler['item'] = data.item_name
            filler['quantity'] = data.qty
            final_data[data.user_id]['order'].append(copy.deepcopy(filler))

    response_final = []

    for key in final_data:
        response_final.append(copy.deepcopy(final_data[key]))

    return HttpResponse(json.dumps(response_final))


def notify(request):
    restaurant = request.GET.get('restaurant')
    msg = "True"
    d = {}
    d['alert'] = msg
    d['type'] = 'push'
    Push.message("Your order from "+ str(restaurant) + " is complete.", channels=[""])
    return HttpResponse(json.dumps({'status': True}))