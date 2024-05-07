import json
import smtplib
from email.mime.text import MIMEText

from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.utils import timezone
import web3
from django.core.files.storage import FileSystemStorage
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect
# Create your views here.
from Charity_Scheme.models import *
import datetime
import json
from web3 import Web3, HTTPProvider
from .printpdf import printpdffn
# truffle development blockchain address
blockchain_address = 'http://127.0.0.1:7545'
# Client instance to interact with the blockchain
web3 = Web3(HTTPProvider(blockchain_address))
# Set the default account (so we don't need to set the "from" for every transaction call)
web3.eth.defaultAccount = web3.eth.accounts[0]
compiled_contract_path = r"C:\Users\THINKPAD\PycharmProjects\Charity_Scheme_and_Fund_Tracker_Using_Blockchain\node_modules\.bin\build\contracts\Structfund.json"
# Deployed contract address (see `migrate` command output: `contract address`)
deployed_contract_address = '0xeA9Bcb0f7A8391cC1116Fa0d78519Cd6D9CFD33f'

def first(request):
    return  render(request,"firstindex.html")

def login(request):
    auth.logout(request)
    return  render(request,"loginindex.html")


def check_email(request):
    cd = request.GET['code']
    print(cd)
    try:
        ob = user_table.objects.filter(email=cd)
        r = {"key": False}
        if len(ob) > 0:
            r['key'] = True
        print(r)
        return JsonResponse(r)
    except:
        r = {"key": False}

        print(r,"hiuh")
        return JsonResponse(r)


def check_email1(request):
    cd = request.GET['code']
    print(cd)
    try:
        ob = volunteers_table.objects.filter(email=cd)
        r = {"key": False}
        if len(ob) > 0:
            r['key'] = True
        print(r)
        return JsonResponse(r)
    except:
        r = {"key": False}

        print(r,"hiuh")
        return JsonResponse(r)


def logincode(request):
    print(request.POST)
    username=request.POST['textfield']
    password=request.POST['textfield2']
    try:
        ob=login_table.objects.get(username=username ,password=password)
        if ob.username!=username or ob.password!=password:
            return HttpResponse('''<Script>window.location="/"</Script>''')
        if ob.type == 'admin1':
            obb=auth.authenticate(username="admin",password="admin")
            if obb is not None:
                auth.login(request,obb)
            request.session['lid']=ob.id
            return HttpResponse('''<Script>window.location="/adminhomepage"</Script>''')
        elif ob.type=='department':
            obb = auth.authenticate(username="admin", password="admin")
            if obb is not None:
                auth.login(request, obb)
            request.session['lid']=ob.id
            # return redirect("/department_homepage")
            return HttpResponse('''<Script>window.location="/department_homepage_sub"</Script>''')

        elif ob.type == 'volunteer':
            obb = auth.authenticate(username="admin", password="admin")
            if obb is not None:
                auth.login(request, obb)
            request.session['lid'] = ob.id
            return HttpResponse('''<Script>window.location="/volunteer_homepage"</Script>''')

            # return redirect("/user_homepage")
        elif ob.type == 'user':
            obb = auth.authenticate(username="admin", password="admin")
            if obb is not None:
                auth.login(request, obb)
            request.session['lid'] = ob.id
            return HttpResponse('''<Script>window.location="/user_homepage"</Script>''')
        else:
            return HttpResponse('''<Script>alert("Invalid user and password!");window.location="/"</Script>''')
    except:
        return HttpResponse('''<Script>alert("Invalid user and password!");window.location="/"</Script>''')

def Registration(request):
    return  render(request,"regindex.html")





def registration(request):
    try:
        Fname=request.POST['Name']
        Lname=request.POST['lName']
        address= request.POST['Message']
        gender = request.POST['gender']
        phone = request.POST['Phone no']
        email_id = request.POST['Email']
        uname = request.POST['username']
        passwd = request.POST['password']
        lob = login_table()
        lob.username = uname
        lob.password =passwd
        lob.type = 'user'
        lob.save()
        userob = user_table()
        userob.fname = Fname
        userob.lname = Lname
        userob.gender = gender
        userob.address = address
        userob.phone = phone
        userob. email  = email_id
        userob.LOGIN=lob
        userob.save()
        try:
            gmail = smtplib.SMTP('smtp.gmail.com', 587)
            gmail.ehlo()
            gmail.starttls()
            gmail.login('ayshashana656@gmail.com', 'bzfl rvqx odup wixd')
            print("login=======")
        except Exception as e:
            print("Couldn't setup email!!" + str(e))
        msg = MIMEText("Succesfuly registered,Welcome to Athani Pain and Palliative Care")


        print(msg)
        msg['Subject'] = 'Athani pain and paliative care'
        msg['To'] = email_id
        msg['From'] = 'ayshashana656@gmail.com'

        print("ok====")
        try:
            gmail.send_message(msg)
        except Exception as e:
            return HttpResponse('''<Script>alert("invalid");window.location="/"</Script>''')

        return HttpResponse('''<Script>window.location="/"</Script>''')
        # return HttpResponse('''<Script>window.location="/"</Script>''')
    except:
        return HttpResponse('''<Script>alert("Duplicate Entry!!!!!!!1");window.location="/"</Script>''')

def reg(request):
    username  = request.GET['username']
    print(username)
    data = {
        'is_taken': login_table.objects.filter(username__iexact=username).exists()
    }
    if data['is_taken']:
        data['error_message']="A user with this username already exists."

        # return HttpResponse("A user with this username already exists.")
    print(data)
    return JsonResponse(data)

@login_required(login_url='/')
def adminhomepage(request):
    return  render(request,"admin1/adminindex.html")
@login_required(login_url='/')

def mngdepartment(request):
    ob=department_table.objects.all().order_by('-id')
    return  render(request,"admin1/manage department.html",{"val":ob})

def searchdep(request):
    dep=request.POST['textfield']
    ob=department_table.objects.filter(d_name__istartswith=dep)
    return  render(request,"admin1/manage department.html",{"val":ob})

def adddepatment(request):
    return  render(request,"admin1/add department.html")

def editdep(request,id):
    request.session['ed']=id
    ob=department_table.objects.get(id=id)
    return render(request,"admin1/edit department.html",{"val":ob})

def deletedep(request,id):
    ob=department_table.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<Script>alert("Delete Department!!!!!!!1");window.location="/mngdepartment"</Script>''')

def editdepcode(request):
    depart=request.POST['textfield']
    details=request.POST['textfield2']
    ob=department_table.objects.get(id=request.session['ed'])
    ob.d_name=depart
    ob.Details=details
    ob.save()
    return HttpResponse('''<Script>window.location="/mngdepartment#about"</Script>''')

def adddepcode(request):
    depart=request.POST['textfield']
    details=request.POST['textfield2']
    username=request.POST['textfield3']
    password=request.POST['textfield4']
    obj=login_table()
    obj.username=username
    obj.password=password
    obj.type='department'
    obj.save()
    ob=department_table()
    ob.LOGIN=obj
    ob.d_name=depart
    ob.Details=details
    ob.save()
    return HttpResponse('''<Script>window.location="/mngdepartment"</Script>''')
def accept_need(request,id):
    ob=need_table.objects.get(id=id)
    ob.status='verified'
    ob.save()
    return HttpResponse('''<Script>window.location="/verify_need"</Script>''')
@login_required(login_url='/')

def mngfoodchart(request):
    ob = foodchart_table.objects.all().order_by('-id')
    return  render(request,"admin1/manage food chart.html", {'val': ob})


def addfoodchart_code(request):
    daytime=request.POST['select2']
    daytype=request.POST['select3']
    amount=request.POST['textfield']


    ob=foodchart_table()

    ob.daytime=daytime
    ob.daytype=daytype
    ob.amount=amount

    ob.save()
    return redirect('/mngfoodchart')

def editfoodchart(request,id):
    request.session['ed']=id
    ob=foodchart_table.objects.get(id=id)
    return render(request,"admin1/edit_foodchart.html",{"val":ob})



def editcode_foodchart(request):
    # day = request.POST['textfield']
    daytime = request.POST['select2']
    daytype = request.POST['select3']
    amount = request.POST['textfield']

    ob = foodchart_table.objects.get(id=request.session['ed'])

    ob.daytime = daytime
    ob.daytype = daytype
    ob.amount = amount

    ob.save()
    return redirect('/mngfoodchart')



def deletefoodchart(request,id):
    ob=foodchart_table.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<Script>alert("Delete foodchart!!!!!!!1");window.location="/mngfoodchart"</Script>''')









def searchfood(request):
    day=request.POST['textfield']
    ob=foodchart_table.objects.filter(day=day)
    return  render(request,"admin1/manage food chart.html",{"val":ob})


def addfoodchart(request):
    return  render(request,"admin1/add foodchart.html")

@login_required(login_url='/')

def mngproduct(request):
    ob=product_table.objects.all()
    return  render(request,"admin1/manage product.html",{'val':ob})

def add_product(request):
    return  render(request,"admin1/add product.html")

def addproductcode(request):
    productname=request.POST['textfield']
    Description=request.POST['textfield3']

    price=request.POST['textfield4']
    image=request.FILES['file']
    fs=FileSystemStorage()
    fsave=fs.save(image.name,image)

    ob = product_table()
    ob.productname = productname
    ob.Description = Description
    ob.stock = 0
    ob.price = price
    ob.image = image
    ob.image = fsave
    ob.save()
    return HttpResponse('''<Script>window.location="/mngproduct"</Script>''')




def editproduct(request, id):
    request.session['ed']=id
    ob=product_table.objects.get(id=id)
    return render(request,"admin1/editproduct.html",{"val":ob})

def editproductcode(request):
    try:
        productname=request.POST['textfield']
        Description=request.POST['textfield3']
        stock=request.POST['textfield5']
        price=request.POST['textfield4']
        image=request.FILES['file']
        fs=FileSystemStorage()
        fsave=fs.save(image.name,image)

        ob = product_table.objects.get(id=request.session['ed'])
        ob.productname = productname
        ob.Description = Description
        ob.stock = stock
        ob.price = price
        ob.image = image
        ob.image = fsave
        ob.save()
        return HttpResponse('''<Script>window.location="/mngproduct"</Script>''')
    except:
        productname = request.POST['textfield']
        Description = request.POST['textfield3']
        stock = request.POST['textfield5']
        price = request.POST['textfield4']
        ob = product_table.objects.get(id=request.session['ed'])
        ob.productname = productname
        ob.Description = Description
        ob.stock = stock
        ob.price = price
        ob.save()
        return HttpResponse('''<Script>window.location="/mngproduct"</Script>''')

def delete_product(request,id):
    ob=product_table.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<Script>alert("Delete Product!!!!!!!1");window.location="/mngproduct"</Script>''')

def search_product(request):
    pro=request.POST['textfield']
    ob=product_table.objects.filter(productname__istartswith=pro)
    return  render(request,"admin1/manage product.html",{"val":ob})



@login_required(login_url='/')

def verify_need(request):
    oo=department_table.objects.all().order_by('-id')
    on=need_table.objects.all().order_by('-id')
    return  render(request,"admin1/verified need.html",{'val':on,'vall':oo})

def verify_needsearch(request):
    oo = department_table.objects.all()
    date = request.POST['date']
    dep = request.POST['select']
    if dep!="0":
        try:
            on=need_table.objects.filter(department=dep,date=date)
        except Exception as e:
            print(e)
            on = need_table.objects.filter(Q(department=dep) )
        return  render(request,"admin1/verified need.html",{'val':on,'vall':oo,"d":date,"de":int(dep)})
    else:
        try:

            on = need_table.objects.filter(Q(date=date))
        except:
            on = need_table.objects.all().order_by('-id')
        return render(request, "admin1/verified need.html", {'val': on, 'vall': oo,"d":date,"de":int(dep)})

def view_foodchart_donation_details(request):
    obb=fooddonation.objects.all().order_by('-id')
    return  render(request,"user/view foodchart donate details.html",{'val':obb})



@login_required(login_url='/')

def view_foodchart_and_donation_details(request):
    obb=fooddonation.objects.all()
    return  render(request,"admin1/view foodchart and donate details.html",{'val':obb})


def search_donation_date(request):
    d=request.POST['date']
    # ob=needresponse.objects.filter(date__exact=d)
    ob = fooddonation.objects.filter(date__exact=d)
    return  render(request,"admin1/view foodchart and donate details.html",{'val':ob,"date":d})
@login_required(login_url='/')

def view_food_details(request,id):
    obb=foodchart_table.objects.filter(id=id)
    return  render(request,"admin1/view details.html",{'val':obb})
@login_required(login_url='/')

def view_need_and_donate_details(request):
    data = []
    with open(
            r'C:\Users\THINKPAD\PycharmProjects\Charity_Scheme_and_Fund_Tracker_Using_Blockchain\node_modules\.bin\build\contracts\Structfund.json') as file:
        contract_json = json.load(file)  # load contract info as JSON
        contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
    contract = web3.eth.contract(address='0x64A02Cdde8ADC7aB0D5BC40D40F97E4f6DD45Ba7', abi=contract_abi)
    blocknumber = web3.eth.get_block_number()
    for i in range(blocknumber, 25, -1):
        try:
            a = web3.eth.get_transaction_by_block(i, 0)
            decoded_input = contract.decode_function_input(a['input'])
            if decoded_input[1]['needid']:
                data.append(decoded_input[1])
        except Exception as e:
            print(e)
            pass
    print(data, "==============================")
    res=[]
    for k in data:
        print(k['userid'],"============")
        ob1=user_table.objects.get(LOGIN__id=k['userid'])
        ob2=need_table.objects.get(id=k['needid'])
        row={'date':k['date'],'amount':k['amount'],'needid':ob2.needs,'userid':ob1.fname+" "+ob1.lname}
        res.append(row)
        # row={'needs':i.needs,'d_name':i.department.d_name,'amount':i.amount,'details':i.details,'date':i.date,'id':i.id,'amt':amnt}
    return  render(request,"admin1/view need and donate details.html",{'val':res})



def search_need_and_donate_details(request):
    date=request.POST['date']
    data = []
    with open(
            r'C:\Users\THINKPAD\PycharmProjects\Charity_Scheme_and_Fund_Tracker_Using_Blockchain\node_modules\.bin\build\contracts\Structfund.json') as file:
        contract_json = json.load(file)  # load contract info as JSON
        contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
    contract = web3.eth.contract(address='0x64A02Cdde8ADC7aB0D5BC40D40F97E4f6DD45Ba7', abi=contract_abi)
    blocknumber = web3.eth.get_block_number()
    for i in range(blocknumber, 26, -1):
        try:
            a = web3.eth.get_transaction_by_block(i, 0)
            decoded_input = contract.decode_function_input(a['input'])
            if decoded_input[1]['date'] in date:
                data.append(decoded_input[1])
        except Exception as e:
            print(e)
            pass
    print(data, "==============================")
    res=[]
    for k in data:
        pp=k['userid']
        print(pp,"ggggggggggggggggggg")
        ob1=user_table.objects.get(LOGIN__id=k['userid'])
        ob2=need_table.objects.get(id=k['needid'],date=date)
        if k['date']==date:
            row={'date':k['date'],'amount':k['amount'],'needid':ob2.needs,'userid':ob1.fname+" "+ob1.lname}
            res.append(row)
        # row={'needs':i.needs,'d_name':i.department.d_name,'amount':i.amount,'details':i.details,'date':i.date,'id':i.id,'amt':amnt}
    return  render(request,"admin1/view need and donate details.html",{'val':res,'date':date})
def view_order_history(request):
    ob = order_table.objects.all()
    return  render(request,"admin1/view order history.html",{'val':ob})

def search_order_history(request):
    d=request.POST['d']
    ob=order_table.objects.filter(date=d)
    return  render(request,"admin1/view order history.html",{'val':ob,"d":d})

@login_required(login_url='/')

def view_patient_information(request):
    ob=patientinfo_table.objects.all()
    return  render(request,"admin1/view patient information.html",{'val':ob})

@login_required(login_url='/')

def view_patient_information_search(request):
    name=request.POST['textfield']
    ob=patientinfo_table.objects.filter(Q(fname__startswith=name)|Q(gender__startswith=name))
    return render(request,"admin1/view patient information.html",{'val':ob})

@login_required(login_url='/')

def view_volunteer(request):
    ob=volunteers_table.objects.exclude(status="disabled")
    return render(request,"admin1/view volunteers.html",{'val':ob})
def view_volunteersearch(request):
    name=request.POST['textfield']
    ob=volunteers_table.objects.filter(Q(fname__istartswith=name)|Q(gender=name)|Q(place__istartswith=name))
    return render(request,"admin1/view volunteers.html",{'val':ob})



@login_required(login_url='/')

def generate_report(request):
    # data = []
    # with open(
    #         r'C:\Users\THINKPAD\PycharmProjects\Charity_Scheme_and_Fund_Tracker_Using_Blockchain\node_modules\.bin\build\contracts\Structfund.json') as file:
    #     contract_json = json.load(file)  # load contract info as JSON
    #     contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
    # contract = web3.eth.contract(address='0x64A02Cdde8ADC7aB0D5BC40D40F97E4f6DD45Ba7', abi=contract_abi)
    # blocknumber = web3.eth.get_block_number()
    # for i in range(blocknumber, 25, -1):
    #     try:
    #         a = web3.eth.get_transaction_by_block(i, 0)
    #         decoded_input = contract.decode_function_input(a['input'])
    #         if decoded_input[1]['needid']:
    #             data.append(decoded_input[1])
    #     except Exception as e:
    #         print(e)
    #         pass
    # print(data, "==============================")
    # res = []
    # for k in data:
    #     print(k['userid'], "============")
    #     ob1 = user_table.objects.get(LOGIN__id=k['userid'])
    #     ob2 = need_table.objects.get(id=k['needid'])
    #     row = {'date': k['date'], 'amount': k['amount'], 'needid': ob2.needs, 'userid': ob1.fname + " " + ob1.lname}
    #     res.append(row)
        # row={'needs':i.needs,'d_name':i.department.d_name,'amount':i.amount,'details':i.details,'date':i.date,'id':i.id,'amt':amnt}
    return  render(request,"admin1/genarate monthly report.html",{"report":"no"})


def search_generate_report(request):
    startingdate =  datetime.datetime.strptime(request.POST['date'], '%Y-%m-%d')
    endingdate = datetime.datetime.strptime(request.POST['date1'], '%Y-%m-%d')
    data = []
    with open(
            r'C:\Users\THINKPAD\PycharmProjects\Charity_Scheme_and_Fund_Tracker_Using_Blockchain\node_modules\.bin\build\contracts\Structfund.json') as file:
        contract_json = json.load(file)  # load contract info as JSON
        contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
    contract = web3.eth.contract(address='0x64A02Cdde8ADC7aB0D5BC40D40F97E4f6DD45Ba7', abi=contract_abi)
    blocknumber = web3.eth.get_block_number()
    for i in range(blocknumber, 25, -1):
        try:
            a = web3.eth.get_transaction_by_block(i, 0)
            decoded_input = contract.decode_function_input(a['input'])
            if decoded_input[1]['needid']:
                data.append(decoded_input[1])
        except Exception as e:
            print(e)
            pass
    print(data, "==============================")
    res = []
    s=0
    for k in data:
        print(k,"================")
        print(k['userid'], "============")
        ob1 = user_table.objects.get(LOGIN__id=k['userid'])
        try:
            ob2 = need_table.objects.get(id=k['needid'])

            tday = datetime.datetime.strptime(k['date'], '%Y-%m-%d')
            if tday<=endingdate and tday>=startingdate:
                row = {'date': k['date'], 'amount': k['amount'], 'needid': ob2.needs, 'userid': ob1.fname + " " + ob1.lname}
                res.append(row)
                s=float(s)+float(k['amount'])

                print(s, "kkkkkkkkkkkkkkkkkkkk")
        except:
            pass
        # row={'needs':i.needs,'d_name':i.department.d_name,'amount':i.amount,'details':i.details,'date':i.date,'id':i.id,'amt':amnt}


    data=[['Date',"Username","Need","Amount"]]
    for i in res:
        r=[i['date'],i['userid'],i['needid'],str(i["amount"]).split(".")[0]+".00"]
        data.append(r)
    r=["","","Total",str(s).split(".")[0]+".00"]
    data.append(r)
    printpdffn(data,str(startingdate).split(" ")[0],str(endingdate).split(" ")[0])

    return render(request, "admin1/genarate monthly report.html", {'val': res,'fdate':startingdate,'tdate':endingdate,"s":s,"report":"yes"})









def  department_homepage(request):
    return  render(request,"department/depindex.html")


def  department_homepage_sub(request):
    return  render(request,"department/depindex_sub.html")
@login_required(login_url='/')

def add_and_manage_inventory(request):
    ob = inventory_table.objects.filter(department__LOGIN__id=request.session['lid']).order_by('-id')
    return  render(request,"department/add and manage inventory.html",{'val':ob})
@login_required(login_url='/')
def add_and_manage_inventory_search(request):
    name=request.POST['textfield']
    ob=inventory_table.objects.filter(inventory__istartswith=name,department__LOGIN__id=request.session['lid'])
    return render(request,"department/add and manage inventory.html",{'val':ob})



def add_inventory(request):
    ob=department_table.objects.filter(LOGIN__id=request.session['lid'])
    return  render(request,"department/add inventory.html",{"val":ob})



def addinvcode(request):
    department=request.POST['textfield2']
    inventory=request.POST['select']
    description=request.POST['textfield3']
    stock=request.POST['textfield4']


    ob=inventory_table()
    ob.department=department_table.objects.get(id=department)
    ob.inventory=inventory
    ob.description=description
    ob.stock=stock

    ob.save()
    return HttpResponse('''<Script>window.location="/add_and_manage_inventory"</Script>''')





def editinvcode(request):
    department=request.POST['textfield2']
    inventory=request.POST['select']
    description=request.POST['textfield3']
    stock=request.POST['textfield4']


    ob=inventory_table.objects.get(id=request.session['iid'])
    ob.department=department_table.objects.get(id=department)
    ob.inventory=inventory
    ob.description=description
    ob.stock=stock

    ob.save()
    return HttpResponse('''<Script>window.location="/add_and_manage_inventory"</Script>''')


def edit_inv1(request,id):
    obb=inventory_table.objects.get(id=id)
    request.session['iid']=id
    ob=department_table.objects.filter(LOGIN__id=request.session['lid'])

    return  render(request,"department/edit_inventory.html",{"val":ob,"val1":obb})

def delete_inv(request,id):
    ob=inventory_table.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<Script>alert("Delete inventory!!!!!!!1");window.location="/add_and_manage_inventory"</Script>''')



# def add_and_manage_needs(request):
#     return  render(request,"department/add and manage needs.html")

@login_required(login_url='/')

def add_and_manage_needs(request):

    ob=need_table.objects.filter(department__LOGIN__id=request.session['lid']).order_by('-id')
    return  render(request,"department/add and manage needs.html",{'val':ob})



def search_add_and_manage_needs(request):
    d=request.POST['d']
    ob=need_table.objects.filter(department__LOGIN__id=request.session['lid'],date=d)
    return  render(request,"department/add and manage needs.html",{'val':ob,"d":d})

def add_needs(request):
    return  render(request,"department/add needs.html")

def addneedcode(request):
    needs=request.POST['textfield']
    details=request.POST['textfield2']
    amount=request.POST['textfield3']
    status="pending"
    ob=need_table()
    ob.needs = needs
    ob.details = details
    ob.amount = amount
    ob.status = status
    ob.department =department_table.objects.get(LOGIN__id=request.session['lid'])
    ob.date=datetime.datetime.now()
    ob.save()
    return HttpResponse('''<script>window.location="/add_and_manage_needs"</script>''')




def editneeds(request,id):
    request.session['ed']=id
    ob=need_table.objects.get(id=id)
    return render(request,"department/edit needs.html",{"val":ob})



def editcode1(request):
    # try:
        needs = request.POST['textfield']
        details = request.POST['textfield2']
        amount = request.POST['textfield3']


        ob = need_table.objects.get(id=request.session['ed'])
        ob.needs = needs
        ob.details = details
        ob.amount = amount
        # ob.status = status
        ob.department = department_table.objects.get(LOGIN__id=request.session['lid'])
        ob.date = datetime.datetime.now()
        ob.save()

        return HttpResponse('''<Script>window.location="/add_and_manage_needs"</Script>''')


def deleteneeds(request,id):
    ob=need_table.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<Script>alert("Delete needs!!!!!!!1");window.location="/add_and_manage_needs"</Script>''')











def add_and_manage_volunteer(request):
    ob = volunteers_table.objects.all().order_by('-id')
    return  render(request,"department/add and manage volunteer.html",{'val':ob})

def add_volunteer(request):
    return  render(request,"department/add volunteer.html")


def addvolcode(request):
    fname=request.POST['textfield']
    lname=request.POST['textfield2']
    gender=request.POST['radiobutton']
    place=request.POST['textfield3']
    post=request.POST['textfield5']
    pin=request.POST['textfield4']
    phone=request.POST['textfield6']
    photo=request.FILES['file']
    fs=FileSystemStorage()
    fsave=fs.save(photo.name,photo)
    email = request.POST['textfield10']

    aadharno=request.POST['textfield8']
    Username=request.POST['textfield7']
    Password=request.POST['textfield82']

    lob = login_table()
    lob.username = Username
    lob.password = Password
    lob.type = 'volunteer'
    lob.save()

    ob=volunteers_table()
    ob.fname=fname
    ob.lname=lname
    ob.gender=gender
    ob.place=place
    ob.post=post
    ob.pin=pin
    ob.phone=phone
    ob.photo=fsave
    ob.email=email
    ob.aadharno=aadharno
    ob.LOGIN=lob
    ob.save()
    return HttpResponse('''<Script>window.location="/add_and_manage_volunteer"</Script>''')


def editvol(request,id):
    request.session['ed']=id
    return redirect("/editvol1")

def editvol1(request):
    id=request.session['ed']
    ob=volunteers_table.objects.get(id=id)
    return render(request,"department/edit_volunteer.html",{"val":ob})




def editcode(request):
    try:
        fname=request.POST['textfield']
        lname=request.POST['textfield2']
        gender=request.POST['radiobutton']
        place=request.POST['textfield3']
        post=request.POST['textfield5']
        pin=request.POST['textfield4']
        phone=request.POST['textfield6']
        email=request.POST['textfield10']
        photo=request.FILES['file']
        fs=FileSystemStorage()
        fsave=fs.save(photo.name,photo)
        aadharno=request.POST['textfield8']


        ob=volunteers_table.objects.get(id= request.session['ed'])
        ob.fname=fname
        ob.lname=lname
        ob.gender=gender
        ob.place=place
        ob.post=post
        ob.pin=pin
        ob.phone=phone
        ob.email=email
        ob.photo=fsave
        ob.aadharno=aadharno
        ob.save()
    except:
        fname = request.POST['textfield']
        lname = request.POST['textfield2']
        gender = request.POST['radiobutton']
        place = request.POST['textfield3']
        post = request.POST['textfield5']
        pin = request.POST['textfield4']
        phone = request.POST['textfield6']
        email=request.POST['textfield10']


        aadharno = request.POST['textfield8']

        ob = volunteers_table.objects.get(id=request.session['ed'])
        ob.fname = fname
        ob.lname = lname
        ob.gender = gender
        ob.place = place
        ob.post = post
        ob.pin = pin
        ob.phone = phone
        ob.email = email
        ob.aadharno = aadharno
        ob.save()

    return HttpResponse('''<Script>window.location="/add_and_manage_volunteer"</Script>''')




def deletepai(request,id):
    request.session['pid'] = id
    ob=patientinfo_table.objects.get(id=id)
    ob.status='disabled'
    ob.save()
    return render(request, "volunteers/reson_page.html")


def add_reson(request):
    reson = request.POST['textfield']
    ob = patient_enable()
    ob.reson = reson
    ob.status = 'disabled'
    ob.patient_id = patientinfo_table.objects.get(id=request.session['pid'])
    ob.save()

    return HttpResponse('''<Script>window.location="/add_and_manage_patientinfo"</Script>''')



def enabelepai(request,id):
    ob=patientinfo_table.objects.get(id=id)
    ob.status='enabled'
    ob.save()
    ob = patient_enable.objects.get(patient_id__id=id)
    ob.delete()
    return HttpResponse('''<Script>window.location="/add_and_manage_patientinfo"</Script>''')




def deletevol(request,id):
    ob=volunteers_table.objects.get(id=id)
    ob.status='disabled'
    ob.save()
    onn=login_table.objects.get(id=ob.LOGIN.id)
    onn.type='disabled'
    onn.save()

    return HttpResponse('''<Script>window.location="/add_and_manage_volunteer"</Script>''')



def enabelevol(request,id):
    ob=volunteers_table.objects.get(id=id)
    ob.status='enabled'
    ob.save()
    onn = login_table.objects.get(id=ob.LOGIN.id)
    onn.type = 'volunteer'
    onn.save()
    return HttpResponse('''<Script>window.location="/add_and_manage_volunteer"</Script>''')


def searchvol(request):
    name=request.POST['textfield']
    ob=volunteers_table.objects.filter(Q(fname__istartswith=name)|Q(gender=name)|Q(place__istartswith=name))
    return  render(request,"department/add and manage volunteer.html",{"val":ob})
@login_required(login_url='/')

def verify_user_request(request):
    print(request.session['lid'])
    ob=inventoryrequest_table.objects.filter(inventory__department__LOGIN__id=request.session['lid']).order_by('-id')

    return  render(request,"department/verify user request.html",{'val':ob})

def search_verify_user_request(request):
    d=request.POST['d']
    name=request.POST['name']
    ob=inventoryrequest_table.objects.filter(Q(userid__fname__startswith=name) |Q(inventory__inventory__startswith=name) | Q(date=d),inventory__department__LOGIN__id=request.session['lid'])
    return  render(request,"department/verify user request.html",{'val':ob,"d":d})


def accept(request,id):
    ob=inventoryrequest_table.objects.get(id=id)
    ob.status='accept'
    ob.save()
    return HttpResponse('''<Script>alert("Accepted");window.location="/verify_user_request"</Script>''')

def reject(request,id):
    ob=inventoryrequest_table.objects.get(id=id)
    oo=ob.stock
    kk=ob.inventory.id
    ob.status='reject'
    ob.save()
    obb = inventory_table.objects.get(id=kk)
    o=obb.stock
    h=int(oo)+int(o)
    obb.stock=h
    obb.save()
    return HttpResponse('''<Script>alert("Rejected");window.location="/verify_user_request"</Script>''')

def user_homepage(request):
    # return  render(request,"user/userindex.html")
    return  render(request,"user/usersubindex.html")

def request_for_inventory(request):
    obb=inventory_table.objects.all()
    return  render(request,"user/request for inventory.html",{'val':obb})

# def request_for_inventory_search(request):
#     dept=request.POST['textfield']
#     ob=inventoryrequest_table.objects.filter(inventory__department__d_name_istarstwith=dept)
#     return render(request,"user/request for inventory.html",{'val':ob})


def search_inv(request):
    dep=request.POST['textfield']
    print(request.POST,"hhhhhhhhhhhhhhhhh")
    ob=inventory_table.objects.filter(Q(department__d_name__startswith=dep)|Q(inventory__startswith=dep))
    return  render(request,"user/request for inventory.html",{'val':ob})

@login_required(login_url='/')

def myreq(request):
    ob=inventoryrequest_table.objects.filter(userid__LOGIN__id=request.session['lid']).order_by('-id')
    return  render(request,"user/my_request .html",{'val':ob})


def req_inv(request,id):
    request.session['kidf']=id
    ob=inventory_table.objects.get(id=id)
    return render(request,"user/req_inv.html",{"val":ob})

def request_inv(request):
    print(request.POST)
    a=request.POST['textfield']
    b=request.POST['textfield2']
    oo=inventory_table.objects.get(id=request.session['kidf'])
    st=int(oo.stock)
    if(int(a)<st):
        oo.stock=int(oo.stock)-int(a)
        oo.save()
        ob=inventoryrequest_table()
        ob.inventory=inventory_table.objects.get(id=request.session['kidf'])
        ob.stock=a
        ob.reason=b
        ob.status='pending'
        ob.date=datetime.datetime.now()
        ob.userid=user_table.objects.get(LOGIN__id=request.session['lid'])
        ob.save()
        return HttpResponse('''<Script>window.location="/request_for_inventory"</Script>''')
    else:
        return HttpResponse('''<Script>alert("out of stock");window.location="/request_for_inventory"</Script>''')

@login_required(login_url='/')

def view_foodchart_and_donate(request):
    current_date = datetime.datetime.now()

    # Define the number of days you want to add
    days_to_add = 1

    # Calculate the date after the current date
    future_date = current_date + datetime.timedelta(days=days_to_add)

    # Format the date as desired (YYYY-MM-DD)
    formatted_date = future_date.strftime("%Y-%m-%d")

    # Print or use the formatted future date
    print(formatted_date)
    ob=foodchart_table.objects.all()
    return render(request,"user/view foodchart and donate.html",{'val':ob,'min':formatted_date})
def view_foodchart_add(request):
    date=request.POST['textfield']
    fid=request.POST.getlist('check')
    print(request.POST)
    tot=0
    lids=[]
    for i in fid:
        ob = fooddonation()
        obb=foodchart_table.objects.get(id=i)
        ob.foodchart = foodchart_table.objects.get(id=i)
        ob.amount = obb.amount
        tot=int(tot)+int(obb.amount)
        print(tot,"==============")
        request.session['tot']=tot
        o=fooddonation.objects.filter(foodchart_id=i,date=date,status='paid')
        print(o,"ugfghjklkjhvn")
        if len(o) == 0:
            ob.userid=user_table.objects.get(LOGIN__id=request.session['lid'])
            ob.foodchart=foodchart_table.objects.get(id=i)
            ob.date=date
            ob.status="pending"
            # ob.amount=tot
            ob.save()
            lids.append(str(ob.id))
            # return HttpResponse('''<script>alert("Success! Thank you for your Contribution");window.location="/food_userpay"</script>''')
        else:
            request.session['fid'] = ','.join(lids)
            return HttpResponse('''<script>alert("Already Contributed");window.location="/view_foodchart_and_donate"</script>''')
    request.session['fid']=','.join(lids)
    return HttpResponse('''<script>window.location="/food_userpay"</script>''')
@login_required(login_url='/')

def view_need_and_donate(request):
    ob1 = department_table.objects.all()
    ob = need_table.objects.filter(status="verified").order_by('-id')
    data=[]
    for i in ob:
        from django.db.models import Sum
        obb=needresponse.objects.filter(needid__id=i.id).aggregate(Sum('amount'))
        print(obb)
        if obb['amount__sum'] is None:
            amt=0
        else:
            amt=obb['amount__sum']
        print(i.amount,amt,"===============================")
        if float(i.amount)>=float(amt):
            amnt=0
        else:
            amnt=1
        print(amnt,"*************************")
        row={'needs':i.needs,'d_name':i.department.d_name,'amount':i.amount,'details':i.details,'date':i.date,'id':i.id,'amt':amnt}
        data.append(row)
    return render(request, "user/view need and donate.html", {"val": data, 'val1': ob1})
def search1(request):
    ob1 = department_table.objects.all()
    dep=request.POST['select']
    try:
        date=request.POST['date']
    except:
        date='0000-00-00'
    if dep == "0":
        try:
            ob = need_table.objects.filter(status="verified",date=date).order_by('-id')
        except:
            ob = need_table.objects.filter(status="verified").order_by('-id')
    else:
        try:
             ob = need_table.objects.filter(status="verified",department__id=dep,date=date).order_by('-id')
        except:
            ob = need_table.objects.filter(status="verified", department__id=dep).order_by('-id')

    data=[]
    for i in ob:
        from django.db.models import Sum
        obb=needresponse.objects.filter(needid__id=i.id).aggregate(Sum('amount'))
        print(obb)
        if obb['amount__sum'] is None:
            amt=0
        else:
            amt=obb['amount__sum']
        print(i.amount,amt,"===============================")
        if float(i.amount)>=float(amt):
            amnt=0
        else:
            amnt=1
        print(amnt,"*************************")
        row={'needs':i.needs,'d_name':i.department.d_name,'amount':i.amount,'details':i.details,'date':i.date,'id':i.id,'amt':amnt}
        data.append(row)
    return render(request, "user/view need and donate.html", {"val": data, 'val1': ob1,'dt':int(dep),'date':date})


import razorpay
def send_need_response(request,id):
    ob = need_table.objects.get(id=id)
    request.session['needid'] = id
    return render(request,'user/donate_amount.html',{"val":ob})
    # return render(request,'user/UserPayProceed.html',{"val":ob})
def getAmount(request):
    request.session['pay_amount'] = request.POST['textfield3']
    request.session['charityid'] = request.POST['did']
    return redirect('/user_pay_proceed')
def user_pay_proceed(request):
    import razorpay
    amount=request.session['pay_amount']
    # did=request.session['charityid']
    client = razorpay.Client(auth=("rzp_test_edrzdb8Gbx5U5M","XgwjnFvJQNG6cS7Q13aHKDJj"))
    print(client)
    payment = client.order.create({'amount': str(int(amount)*100)+"", 'currency': "INR", 'payment_capture': '1'})
    return render(request,'user/UserPayProceed.html', {'p':payment,'nid':request.session['needid'],'uid':request.session['lid']})

def food_userpay(request):
    return render(request, 'user/pymt.html',
                  {'amt':request.session['tot']})

def food_userpayy(request):
    amount = request.session['tot']
    # did=request.session['charityid']
    client = razorpay.Client(auth=("rzp_test_edrzdb8Gbx5U5M", "XgwjnFvJQNG6cS7Q13aHKDJj"))
    print(client)
    payment = client.order.create({'amount': str(amount) + "", 'currency': "INR", 'payment_capture': '1'})
    return render(request, 'user/food_UserPayProceed.html',
                  {'p': payment,'fid':request.session['fid']})
def on_payment_success1(request,id,amt):
    try:
        ids=id.split(',')
        for id in ids:

            ob=fooddonation.objects.get(id=id)
            ob.status='paid'

            ob.save()
        return HttpResponse('''<script>alert("Success! Thank you for your Contribution");window.location="/user_homepage"</script>''')
    except:
        return HttpResponse(
            '''<script>alert("Success! Thank you for Ordering");window.location="/user_homepage"</script>''')


def on_payment_success(request,id,id2,id3):
    import datetime
    print(request.POST,"===================================================")
    # p=request.POST['amount']
    amt = str(id)
    needid=id2
    uid=id3
    print(amt,needid,uid,"============================")
    # charity = request.session['charityid']
    # qry = "INSERT INTO `donation` VALUES(NULL,%s,%s,%s,CURDATE())"
    # iud(qry, (charity, session['lid'], amt))
    # q="select * from user where lid=%s"
    q=user_table.objects.get(LOGIN__id=uid)
    # v=selectone(q,session['lid'])
    ob=needresponse()
    ob.userid = user_table.objects.get(LOGIN__id=uid)
    ob.needid_id = needid
    ob.date = datetime.datetime.now()
    ob.status = "paid"
    amt1 = amt[:-2]
    ob.amount = amt1
    ob.save()
    ob1=need_table.objects.get(id=needid)
    print(amt1,"88888888888888888888")
    ob1.amount=int(ob1.amount)-int(amt1)
    ob1.save()
    with open(
            r'C:\Users\THINKPAD\PycharmProjects\Charity_Scheme_and_Fund_Tracker_Using_Blockchain\node_modules\.bin\build\contracts\Structfund.json') as file:
        contract_json = json.load(file)  # load contract info as JSON
        contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
    contract = web3.eth.contract(address='0x52FC83A873Fe71b145B930b1D02dD69B04243d81', abi=contract_abi)
    blocknumber = web3.eth.get_block_number()
    message2 = contract.functions.addfund(blocknumber + 1, str(needid), str(uid),
                                          str(datetime.datetime.now().strftime("%Y-%m-%d")),str(amt1)).transact({'from': web3.eth.accounts[0]})
    return HttpResponse('''<script>alert("Success! Thank you for your Contribution");window.location="/view_need_and_donate"</script>''')

def search_dep(request):
    dep=request.POST['select']
    ob1=department_table.objects.all()
    # ob= need_table.objects.filter(department_id=dep).order_by('-id')
    if dep!="0":
        try:
            on=need_table.objects.filter(department=dep)
        except Exception as e:
            print(e)
            on = need_table.objects.filter(Q(department=dep) )
        return  render(request,"user/view need and donate.html",{'val':on,'val1':ob1,"de":int(dep)})
    else:
        on = need_table.objects.all()
        return render(request, "user/view need and donate.html", {'val': on, 'val1': ob1})
    # return  render(request,"user/view need and donate.html",{"val":ob, 'val1': ob1, 'dep': int(dep)})


# def search_dep(request):
#     dep=request.POST['textfield']
#     ob=department_table.objects.filter(d_name__istartswith=dep)
#     return  render(request,"user/view need and donate.html",{"val":ob})
#
@login_required(login_url='/')

def view_Product_and_purchase(request):
    ob=product_table.objects.all()
    return  render(request,"user/view product and purchase.html",{'val':ob})


def view_more_product(request,id):
    ob=product_table.objects.get(id=id)
    request.session['prid']=id
    return  render(request,"user/view more.html",{'val':ob})


def addtocart(request):
    qty=request.POST['textfield4']
    ok=order_table()
    ok.userid=user_table.objects.get(LOGIN__id=request.session['lid'])
    ok.date=datetime.datetime.now()
    pro=product_table.objects.get(id=request.session['prid'])
    price=pro.price
    ok.amount=int(qty)*int(price)
    ok.status="cart"
    ok.save()

    ob=orderdetail_table()
    ob.product=product_table.objects.get(id=request.session['prid'])
    ob.stock=qty
    ob.order=ok
    ob.save()
    return HttpResponse('''<Script>window.location="/view_Product_and_purchase"</Script>''')





def viewmore(request):
    productname=request.POST['textfield']
    price=request.POST['textfield2']
    stock=request.POST['textfield3']
    # qty=request.POST['textfield4']



    ob=product_table()
    ob.productname=productname
    ob.price=price
    ob.stock=stock
    ob.save()
    return HttpResponse('''<Script>window.location="/view_Product_and_purchase"</Script>''')





@login_required(login_url='/')

def view_my_order(request):
    return  render(request,"user/view my order.html")

@login_required(login_url='/')

def view_my_cart(request):
    try:
        OB1 = order_table.objects.get(userid__LOGIN__id=request.session['lid'], status='CART')
        ob = orderdetail_table.objects.filter(order__userid__LOGIN__id=request.session['lid'], order__status='CART')
        print( OB1.amount,"hhhhhhhhhhhhhh")
        return render(request, 'user/view my cart.html', {'val': ob, 'total': OB1.amount,"oid":OB1.id})

    except:
        ob = orderdetail_table.objects.filter(order__userid__LOGIN__id=request.session['lid'], order__status='CART')
        return render(request, 'user/view my cart.html', {'val': ob, 'total': 0})

def deleteviewproduct(request,id,qid):
    print(request.POST, "uuuuuuuuuuuuuuuu")


    obd = orderdetail_table.objects.get(id=id)
    j=obd.price
    obp = product_table.objects.get(id=obd.product.id)
    obp.stock = float(obp.stock) + int(qid)
    obp.save()
    ob11 = order_table.objects.get(id=obd.order.id)
    o=int(ob11.amount)-int(j)
    ob11.amount=o
    ob11.save()
    id=obd.order.id
    obd.delete()
    ob2 = orderdetail_table.objects.filter(order__id=id)
    if len(ob2) == 0:
        ob1 = order_table.objects.get(id=id)
        ob1.delete()
    return HttpResponse('''<Script>alert("Delete product...........");window.location="/view_my_cart"</Script>''')

def view_item_product(request,id):
    ob=orderdetail_table.objects.filter(order__id=id)
    return  render(request,"admin1/view items_product.html",{'val':ob})








@login_required(login_url='/')

def view_more(request):
    return  render(request,"user/view more.html")
@login_required(login_url='/')

def view_item(request):
    return  render(request,"user/view items.html")

@login_required(login_url='/')


def volunteer_homepage(request):
    return  render(request,"volunteers/volindex1.html")
def add_and_manage_patientinfo(request):
    ob = patientinfo_table.objects.filter(status='enabled').order_by('-id')
    return  render(request,"volunteers/ass and manage patient information.html",{'val':ob})

def disable_patientinfo(request):
    ob = patient_enable.objects.filter(status='disabled').order_by('-id')
    return  render(request,"volunteers/disable_patients.html",{'val':ob})


def view_reson(request):
    ob = patient_enable.objects.filter(status='disabled').order_by('-id')
    return  render(request,"volunteers/disable_patients.html",{'val':ob})


def add_patients(request):
    return  render(request,"volunteers/add patient info.html")



def addpatientinfo(request):
    fname=request.POST['textfield']
    lname=request.POST['textfield1']
    gender=request.POST['radiobutton']
    dob=request.POST['date']
    date=request.POST['date1']
    img=request.FILES['file']
    fs = FileSystemStorage()
    fsave = fs.save(img.name, img)
    img1 = request.FILES['file1']
    fs1 = FileSystemStorage()
    fsave1 = fs1.save(img1.name, img1)
    phone=request.POST['textfield6']
    disease=request.POST['textarea']
    ob=patientinfo_table()
    ob.fname=fname
    ob.lname=lname
    ob.gender=gender
    ob.dob=dob
    ob.Image=fsave
    ob.idproof=fsave1
    ob.sdate=date

    ob.phone=phone
    ob.disease=disease
    ob.volunteer=volunteers_table.objects.get(LOGIN__id=request.session['lid'])
    ob.save()
    return HttpResponse('''<Script>window.location="/add_and_manage_patientinfo"</Script>''')

def editpatient1(request,id):
    request.session['ed']=id
    ob=patientinfo_table.objects.get(id=id)
    print(ob.dob,"jjjjjjj")
    return render(request,"volunteers/edit_patient info.html",{"val":ob,"date":str(ob.sdate),"dob":str(ob.dob)})


def editpatientcode(request):
    if 'file' in request.FILES and 'file1' in request.FILES:
        fname = request.POST['textfield']
        lname = request.POST['textfield1']
        gender = request.POST['radiobutton']
        dob = request.POST['date']
        date = request.POST['date1']
        img = request.FILES['file']
        fs = FileSystemStorage()
        fsave = fs.save(img.name, img)
        img1 = request.FILES['file1']
        fs1 = FileSystemStorage()
        fsave1 = fs1.save(img1.name, img1)
        phone = request.POST['textfield6']
        disease = request.POST['textarea']
        ob = patientinfo_table.objects.get(id=request.session['ed'])
        ob.fname = fname
        ob.lname = lname
        ob.gender = gender
        ob.dob = dob
        ob.Image = fsave
        ob.idproof = fsave1
        ob.sdate = date

        ob.phone = phone
        ob.disease = disease
        ob.volunteer = volunteers_table.objects.get(LOGIN__id=request.session['lid'])
        ob.save()

    elif 'file1' in request.FILES and 'file' not in request.FILES:
        fname = request.POST['textfield']
        lname = request.POST['textfield1']
        gender = request.POST['radiobutton']
        dob = request.POST['date']
        date = request.POST['date1']
        img1 = request.FILES['file1']
        fs1 = FileSystemStorage()
        fsave1 = fs1.save(img1.name, img1)
        phone = request.POST['textfield6']
        disease = request.POST['textarea']
        ob = patientinfo_table.objects.get(id=request.session['ed'])
        ob.fname = fname
        ob.lname = lname
        ob.gender = gender
        ob.dob = dob
        ob.idproof = fsave1
        ob.sdate = date
        ob.phone = phone
        ob.disease = disease
        ob.volunteer = volunteers_table.objects.get(LOGIN__id=request.session['lid'])
        ob.save()
    elif 'file' in request.FILES and 'file1' not in request.FILES:
        fname = request.POST['textfield']
        lname = request.POST['textfield1']
        gender = request.POST['radiobutton']
        dob = request.POST['date']
        date = request.POST['date1']
        img = request.FILES['file']
        fs = FileSystemStorage()
        fsave = fs.save(img.name, img)
        phone = request.POST['textfield6']
        disease = request.POST['textarea']
        ob = patientinfo_table.objects.get(id=request.session['ed'])
        ob.fname = fname
        ob.lname = lname
        ob.gender = gender
        ob.dob = dob
        ob.Image = fsave
        ob.sdate = date

        ob.phone = phone
        ob.disease = disease
        ob.volunteer = volunteers_table.objects.get(LOGIN__id=request.session['lid'])
        ob.save()
    else:
        fname = request.POST['textfield']
        lname = request.POST['textfield1']
        gender = request.POST['radiobutton']
        dob = request.POST['date']
        date = request.POST['date1']
        phone = request.POST['textfield6']
        disease = request.POST['textarea']
        ob = patientinfo_table.objects.get(id=request.session['ed'])
        ob.fname = fname
        ob.lname = lname
        ob.gender = gender
        ob.dob = dob
        ob.sdate = date

        ob.phone = phone
        ob.disease = disease
        ob.volunteer = volunteers_table.objects.get(LOGIN__id=request.session['lid'])
        ob.save()
    return HttpResponse('''<Script>window.location="/add_and_manage_patientinfo"</Script>''')


def deletepatient(request,id):
    ob=patientinfo_table.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<Script>alert("Delete patient........");window.location="/add_and_manage_patientinfo"</Script>''')


def searchpatient(request):
    patient=request.POST['textfield']
    ob=patientinfo_table.objects.filter(fname__istartswith=patient)
    return  render(request,"volunteers/ass and manage patient information.html",{"val":ob})



@login_required(login_url='/')

def product_stock_update(request):
    ob=product_table.objects.all()
    return  render(request,"volunteers/product stock update.html",{'val':ob})

def updatepro(request,id):
    ob=product_table.objects.get(id=id)
    request.session['proid']=id
    return  render(request,"volunteers/update stock.html",{'val':ob})

def updateprocode(request):
    stock = request.POST['textfield']
    ob=product_table.objects.get(id=request.session['proid'])
    kk=ob.stock
    st=int(stock)+int(kk)
    ob.stock=st
    ob.save()
    return HttpResponse('''<Script>alert("Updated");window.location="/product_stock_update"</Script>''')





def update_stock(request):
    return  render(request,"volunteers/update stock.html")



def view_assigned_department(request):
    return  render(request,"volunteers/view assigned department.html")
@login_required(login_url='/')

def view_department(request):
    ob=department_table.objects.all()
    return  render(request,"volunteers/view department.html",{"val":ob})
@login_required(login_url='/')

def transaction_history(request):
    ob=needresponse.objects.all().order_by('-id')
    return  render(request,"user/transaction history.html",{"val":ob})


########################## cart#######################

def ordrprdctcode(request):
    btn=request.POST['Submit']
    if btn=='ORDER NOW':
        print(request.session['prid'],"kiiiiiiiiiiiiiiiiiii")
        qty=request.POST['textfield4']
        qq=product_table.objects.get(id=request.session['prid'])
        tt = int(qq.price)* int(qty)
        request.session['amt']=tt
        stock = int(qq.stock)
        print(stock,qty,"jjjjjjjjjjjjjjjjjjjjjj")
        nstk = int(stock) - int(qty)
        if stock >= int(qty):
            up=product_table.objects.get(id=request.session['prid'])
            up.stock=nstk
            up.save()
            qt=order_table()
            qt.date=datetime.datetime.today()
            qt.userid=user_table.objects.get(LOGIN=request.session['lid'])
            qt.status='ORDER'
            qt.amount=tt
            qt.save()
            qty1=orderdetail_table()
            qty1.quantity=qty
            qty1.product=product_table.objects.get(id=request.session['prid'])
            qty1.order=qt
            qty1.price=tt
            qty1.save()
            request.session['fid']=qt.id
            return HttpResponse('''<script>alert('placed order successfuly');window.location='/product_userpayy'</script>''')
        else:
            return HttpResponse('''<script>alert('out of stock');window.location='/view_Product_and_purchase'</script>''')
    else:
        print(request.session['prid'], "kiiiiiiiiiiiiiiiiiii")
        qty = request.POST['textfield4']
        qq = product_table.objects.get(id=request.session['prid'])
        tt = int(qq.price) * int(qty)
        request.session['amt']=tt
        stock = int(qq.stock)
        print(stock, qty, "jjjjjjjjjjjjjjjjjjjjjj")
        nstk = int(stock) - int(qty)
        if stock >= int(qty):
            q = order_table.objects.filter(userid=user_table.objects.get(LOGIN__id=request.session['lid']),
                                           status='CART')
            if len(q) == 0:
                qt = order_table()
                qt.date = datetime.datetime.today()
                qt.userid = user_table.objects.get(LOGIN=request.session['lid'])
                qt.status = 'CART'
                qt.amount = tt
                qt.save()
                qty1 = orderdetail_table()
                qty1.quantity = qty
                qty1.product = product_table.objects.get(id=request.session['prid'])
                qty1.order = qt
                qty1.price = tt
                qty1.save()
                return HttpResponse(
                    '''<script>alert('placed in to cart');window.location='/view_Product_and_purchase'</script>''')
            else:
                total = int(q[0].amount) + int(tt)
                print(q[0].amount,"ordertotalamount")
                print(tt,"perpriceamount")
                qt = order_table.objects.get(id=q[0].id)
                qt.amount = total
                qt.date = datetime.datetime.today()
                qt.save()
                qty1 = orderdetail_table.objects.filter(product__id=request.session['prid'], order__id=q[0].id)
                if len(qty1) == 0:
                    qqt = orderdetail_table()
                    qqt.order = q[0]
                    qqt.price = tt
                    qqt.product = product_table.objects.get(id=request.session['prid'])
                    qqt.quantity = qty
                    qqt.save()
                else:
                    qry1 = orderdetail_table.objects.get(id=qty1[0].id)
                    quty = int(qty1[0].quantity) + int(qty)
                    print(quty,"hhhhhhhhhhhhhhhhh")
                    m = int(quty) * int(qq.price)
                    print(m,"lllllllllllllllll")
                    qry1.quantity = quty
                    # qty1.price = int(m)
                    qry1.save()
                    m1 = int(quty) * int(qq.price)
                    qry1.price=m1
                    qry1.save()
                return HttpResponse('''<script>alert(' success');window.location='/view_Product_and_purchase'</script>''')
        else:
            return HttpResponse('''<script>alert('out of stock');window.location='/view_Product_and_purchase'</script>''')


"===========================================orderfromcart====================="
def oredercartproduct(request):
    print(request.POST)
    oid = request.POST['textfield2']
    amount = request.POST['textfield']
    request.session['amtt']=amount
    ob =order_table.objects.get(id=oid)
    obb=orderdetail_table.objects.filter(order__id=oid)
    for i in obb:
        o=product_table.objects.get(id=i.product.id)
        o.stock=o.stock-int(i.quantity)
        o.save()
    ob.status = 'PAID'
    ob.save()
    return HttpResponse('''<script>alert('placed order successfuly');window.location='/product_userpayy1'</script>''')












def product_userpayy(request):
    amount=request.session['amt']

    # did=request.session['charityid']
    client = razorpay.Client(auth=(""
                                   "rzp_test_edrzdb8Gbx5U5M", "XgwjnFvJQNG6cS7Q13aHKDJj"))
    print(client)
    payment = client.order.create({'amount': str(amount) + "", 'currency': "INR", 'payment_capture': '1'})
    return render(request, 'user/product_UserPayProceed.html',
                  {'p': payment,'fid':request.session['fid'],'amt':amount})


def product_userpayy1(request):
    amt = request.session['amtt']

    amount = int(float(amt))
    print(amount, "hjjjjjjj")
    # did=request.session['charityid']
    client = razorpay.Client(auth=(""
                                   "rzp_test_edrzdb8Gbx5U5M", "XgwjnFvJQNG6cS7Q13aHKDJj"))
    print(client)
    payment = client.order.create({'amount': str(amount) + "", 'currency': "INR", 'payment_capture': '1'})
    return render(request, 'user/product_UserPayProceed.html',
                  {'p': payment,'fid':request.session['fid'],'amt':amount})



def on_payment_success4(request,id,amt):

    ids=id.split(',')
    for id in ids:

        ob=fooddonation.objects.get(id=id)
        ob.status='paid'

        ob.save()
    return HttpResponse('''<script>alert("Success! Thank you for your Contribution");window.location="/user_homepage"</script>''')

























