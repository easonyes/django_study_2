from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, QueryDict
from django.urls import reverse
from django.core import serializers
from django.forms.models import model_to_dict
import json
from warehouse.models import *

# Create your views here.

"""

def index(request):
    # 查看所有礼品信息
    #lists = warehouse.objects.all()
    # 返回主页，并将信息在主页显示
    #return render(request, 'index.html', {'presents':lists})


def login(request):
    if request.method == 'POST':
        name = request.POST['empname']
        psd = request.POST['emppassword']
        emploee = Emploee.objects.filter(empname=name, emppassword=psd )
        context = {
            'log_status': 0,
            'order': 0
        }
        request.session['IS_LOGIN'] = False
        if emploee:
            context['log_status'] = 1
            context['order'] = emploee.emporder
            request.session['IS_LOGIN'] = True
            return render(request, request.path, context)
        else:
            return render(request, request.path, context)
    else:
        return render(request, request.path, context='')

def add_page(request):
    return render(request, 'adddata.html', {'title': '添加', 'urlname': 'add_data', 'warehouse': ''})


def add_data(request):
    iname = request.POST['name']
    iintroduction = request.POST['introduction']
    iondate = request.POST['ondate']
    istorenum = request.POST['storenum']
    ioff = request.POST['off']
    offcost = request.POST['offcost']
    if offcost:
        ioffcost = float(offcost)
    else:
        ioffcost = 0
    hot = request.POST['hot']
    if hot:
        ihot = int(hot)
    else:
        ihot = 0
    iprice = request.POST['price']
    obj = warehouse(name=iname, introduction=iintroduction, ondate=iondate, storenum=int(istorenum), status=2, off=int(ioff),
                    offcost=ioffcost, hot=ihot, price=int(iprice))
    obj.save()
    return redirect(reverse('index'))
"""

def index(request):
    # 查看所有礼品信息
    #lists = warehouse.objects.all()
    # 返回主页，并将信息在主页显示
    #return render(request, 'index.html', {'presents':lists})
    return

# done
# tested
def login(request):
    context = {
        'log_status': 0
    }
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        employee = Employee.objects.filter(empname=name, emppassword=password)

        if employee:
            request.session['IS_LOGIN'] = True
            request.session['EMPLOYEE_ID'] = employee[0].id
            request.session['ORDER'] = employee[0].emporder
            conx = serializers.serialize("json", employee)
            conx2 = '{"log_status":1, "employee": ' + conx + '}'
            return HttpResponse(conx2, content_type="application/json")
        else:
            return HttpResponse(json.dumps(context), content_type="application/json")


# done
# tested
def logout(request):
    context={
        'IS_LOGOUT': 0
    }
    if('IS_LOGIN' in request.session and 'EMPLOYEE_ID' in request.session):
        del request.session['IS_LOGIN']
        del request.session['EMPLOYEE_ID']
        context['IS_LOGOUT'] = 1
        return HttpResponse(json.dumps(context), content_type="application/json")
    else:
        return HttpResponse(json.dumps(context), content_type="application/json")

# undone
# not test
def register(request):
    return

# done
# tested
"""
gifts
返回仓库中的礼品信息，如果是仓库管理员，就返回自己仓库的信息，如果是普通员工，就返回所有礼品信息
method: GET
"""
def gifts(request, employee_id):
    employee = Employee.objects.get(pk=employee_id)
    context = {
        'error': 0
    }
    if(not employee) or ('EMPLOYEE_ID' not in request.session) or ('IS_LOGIN' not in request.session) \
        or (request.session['EMPLOYEE_ID'] != employee_id):
        context['error'] = 1
        return HttpResponse(json.dumps(context), content_type="application/json")
    if request.method == 'GET':
        if employee.emporder == 1:
            presents = Present.objects.all()
            '''
            presents = []
            for p in present:
                presents.append(p)
            '''
            conx = serializers.serialize("json", presents)
            return HttpResponse(conx, content_type="application/json")
        elif employee.emporder == 2:
            depots = Depot.objects.get(manager=employee.id)
            presents = Present.objects.filter(pdepot=depots)
            conx = serializers.serialize("json", presents)
            return HttpResponse(conx, content_type="application/json")
            # present = Present.objects.filter(pdepot=)
        else:
            context['error'] = 2
            return HttpResponse(json.dumps(context), content_type="application")
    return

# done
# tested
"""
add
添加一个礼品，仓库管理员可操作，但添加时其默认状态值为0，即待审核状态
method：POST
"""
def add(request, employee_id):
    employee = Employee.objects.get(pk=employee_id)
    context = {
        'error': 0
    }
    if (not employee) or ('EMPLOYEE_ID' not in request.session) or ('IS_LOGIN' not in request.session) \
        or (request.session['EMPLOYEE_ID'] != employee_id):
        context['error'] = 1
        return HttpResponse(json.dumps(context), content_type="application/json")
    if request.method == 'POST':
        pname = request.POST['name']
        introduction = request.POST['introduction']
        on_date = request.POST['on_date']
        store_num = request.POST['store_num']
        status = 0
        cost = request.POST['cost']
        hot = 0
        off = 0
        off_cost = 0
        url = request.POST['url']
        depot = Depot.objects.get(manager=employee)

        #pdepot = Depot.objects.get(id=depot)
        # pdepot = request.POST['pdepot']
        # depots = Depot.objects.all()
        # pdepots = []
        # for depot in depots:
        #    did = depot.id
        #    pdepots.append(did)
        # if pdepot not in pdepots:
        #    context['error'] = 3
        #    return HttpResponse(json.dumps(context), content_type="application/json")
        # else:
        obj = Present(name=pname, introduction=introduction, on_date=on_date, store_num=int(store_num),
                      status=status, cost=float(cost), hot=int(hot), off=int(off),
                      off_cost=off_cost, url=url, pdepot=depot)
        obj.save()
        present = Present.objects.filter(id=obj.id)
        conx = serializers.serialize("json", present)
        return HttpResponse(conx, content_type="application/json")
    return


# done
# tested
"""
modify
修改一个礼品的信息，仓库管理员可操作，但不可修改其状态值以及打折、热度情况
method：PUT
"""
def modify(request, employee_id):
    employee = Employee.objects.get(pk=employee_id)
    context = {
        'error': 0
    }
    if (not employee) or ('EMPLOYEE_ID' not in request.session) or ('IS_LOGIN' not in request.session) \
            or (request.session['EMPLOYEE_ID'] != employee_id):
        context['error'] = 1
        return HttpResponse(json.dumps(context), content_type="application/json")
    if request.method == 'PUT':
        modify = QueryDict(request.body)
        id = modify.get('id')
        present = Present.objects.filter(id=id)
        if not present:
            context['error'] = 2
            return HttpResponse(json.dumps(context), content_type="application/json")
        status = present[0].status
        name = modify.get('name')
        introduction = modify.get('introduction')
        on_date = modify.get('on_date')
        store_num = modify.get('store_num')
        cost = modify.get('cost')
        hot = present[0].hot
        off = present[0].off
        off_cost = present[0].off_cost
        url = modify.get('url')
        pdepot = present[0].pdepot
        present.update(name=name, introduction=introduction, status=status, on_date=on_date,
                       store_num=store_num, cost=cost, hot=hot, off=off, off_cost=off_cost,
                       url=url, pdepot=pdepot)
        conx = serializers.serialize("json", present)
        return HttpResponse(conx, content_type="application/json")

# done
# tested
"""
delete
删除一个礼品，仅仓库管理员可操作
method：DELETE
"""
def delete(request, employee_id):
    employee = Employee.objects.get(pk=employee_id)
    context = {
        'error': 0
    }
    if (not employee) or ('EMPLOYEE_ID' not in request.session) or ('IS_LOGIN' not in request.session) \
            or (request.session['EMPLOYEE_ID'] != employee_id):
        context['error'] = 1
        return HttpResponse(json.dumps(context), content_type="application/json")
    if request.method == 'DELETE':
        delete = QueryDict(request.body)
        key = delete.get('id')
        present = Present.objects.filter(id=key)
        if not present:
            context['error'] = 2
            return HttpResponse(json.dumps(context), content_type="application/json")
        conx = serializers.serialize("json", present)
        present.delete()
        return HttpResponse(conx, content_type="application/json")

# done
# tested
"""
sell
修改一个礼品的状态值，即上架或下架该礼品，以及修改其打折、热度情况，仅普通员工可操作
method：PUT
"""
def sell(request, employee_id):
    employee = Employee.objects.get(pk=employee_id)
    context = {
        'error': 0
    }
    if (not employee) or ('EMPLOYEE_ID' not in request.session) or ('IS_LOGIN' not in request.session) \
            or (request.session['EMPLOYEE_ID'] != employee_id):
        context['error'] = 1
        return HttpResponse(json.dumps(context), content_type="application/json")
    if request.method == 'PUT':
        sell = QueryDict(request.body)
        key = sell.get('id')
        present = Present.objects.filter(id=key)
        if not present:
            context['error'] = 2
            return HttpResponse(json.dumps(context), content_type="application/json")
        name = present[0].name
        introduction = present[0].introduction
        on_date = present[0].on_date
        store_num = present[0].store_num
        status = sell.get('status')
        cost = present[0].cost
        hot = sell.get('hot')
        off = sell.get('off')
        off_cost = sell.get('off_cost')
        url = present[0].url
        pdepot = present[0].pdepot
        present.update(name=name, introduction=introduction, status=status, on_date=on_date,
                       store_num=store_num, cost=cost, hot=hot, off=off, off_cost=off_cost,
                       url=url, pdepot=pdepot)
        conx = serializers.serialize("json", present)
        return HttpResponse(conx, content_type="application/json")
    if request.method == 'GET':
        depots = QueryDict(request.body)
        key1 = depots.get('depot_id')
        key2 = depots.get('present_status')
        if key1:
            depot = Depot.objects.get(id=key1)
            presents = Present.objects.filter(pdepot=depot)
            conx = serializers.serialize("json", presents)
            return HttpResponse(conx, content_type="application/json")
        if key2:
            if key2 == '1':
                presents = Present.objects.filter(status=key2)
                conx = serializers.serialize("json", presents)
                return HttpResponse(conx, content_type="application/json")
            elif key2 == '0':
                presents = Present.objects.filter(status=key2)
                conx = serializers.serialize("json", presents)
                return HttpResponse(conx, content_type="application/json")
            elif key2 == '2':
                presents = Present.objects.filter(status=key2)
                conx = serializers.serialize("json", presents)
                return HttpResponse(conx, content_type="application/json")



