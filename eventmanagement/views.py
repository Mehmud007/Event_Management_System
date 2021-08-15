from django.shortcuts import render,redirect
from . models import Cateror,Customer,Decorator,Hall,Event,Event_Type,Package,Wedding_Package,Corporate_Package
from django.contrib import messages
from django.contrib.sessions.models import Session
from django.views.decorators.cache import cache_control
from django.conf import settings
from django.http import HttpResponse
from datetime import date
# Create your views here.
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def index(request):
    if request.session.has_key('is_hall_booked'):
        halls = Hall.objects.filter(id=request.session['hall_id']).update(is_booked=True)
        del request.session['is_hall_booked']
    if request.session.has_key('persons'): 
        del request.session['persons']
    if request.session.has_key('strating_date'): 
        del request.session['strating_date']
    if request.session.has_key('ending_date'): 
        del request.session['ending_date']
    if request.session.has_key('event_time'): 
        del request.session['event_time']
    if request.session.has_key('hall_name'):
        del request.session['hall_name']
    if request.session.has_key('Price_per_person'):
        del request.session['Price_per_person']
    if request.session.has_key('c_book'):
        del request.session['c_book']
    if request.session.has_key('hall_address'):
        del request.session['hall_address']
    if request.session.has_key('package_name'):
        del request.session['package_name']
    if request.session.has_key('person_capacity'):
        del request.session['person_capacity']
    if request.session.has_key('Price_per_extra_day'):
        del request.session['Price_per_extra_day']
    if request.session.has_key('Price_per_extra_fifty_person'):
        del request.session['Price_per_extra_fifty_person']
    if request.session.has_key('No_of_days'):
        del request.session['No_of_days']
    if request.session.has_key('package_price'):
        del request.session['package_price']
    if request.session.has_key('hall_rent'):
        del request.session['hall_rent']
    if request.session.has_key('hall_image'):
        del request.session['hall_image']
    if request.session.has_key('event_date'):
        del request.session['event_date']
    if request.session.has_key('hall_id'):
        del request.session['hall_id']  
    if request.session.has_key('event_type'):
        del request.session['event_type']  
    if request.session.has_key('username'):
        return render(request,"index.html",{'username':request.session['username']})
    else:
        return render(request,"index.html")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def signin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        category = request.POST['category']
        customer = Customer.objects.all()
        cateror = Cateror.objects.all()
        decorartor = Decorator.objects.all()
        if category == 'Customer':
            if customer:
                for i in customer:
                    if(i.email == email and i.password == password):
                        request.session['username'] = i.firstname
                        request.session['lname'] = i.lastname 
                        request.session['phonno'] = i.phnno 
                        request.session['email'] = i.email  
                        return redirect('home')
                else:
                    messages.success(request,"Login Failed!")
                    return redirect("signin")
        if category == 'Cateror':
            if cateror:
                for i in cateror:
                    if(i.email == email and i.password == password):
                        request.session['username'] = i.firstname
                        request.session['lname'] = i.lastname 
                        request.session['phonno'] = i.phnno 
                        request.session['email'] = i.email      
                        return redirect('home')
                else:
                    messages.success(request,"Login Failed!")
                    return redirect("signin")
        if category == 'Decorator':
            if decorartor:
                for i in decorartor:
                    if(i.email == email and i.password == password):
                        request.session['username'] = i.firstname
                        request.session['lname'] = i.lastname 
                        request.session['phonno'] = i.phnno 
                        request.session['email'] = i.email      
                        return redirect('home')
                else:
                    messages.success(request,"Login Failed!")
                    return redirect("signin")
    elif request.session.has_key('username'):
        return redirect('home')
    else:
        return render(request,"login.html")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def signup(request):
    if request.method == 'POST':
        firstname = request.POST['fname']
        lastname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        phoneno = request.POST['phno']
        category = request.POST['category']
        if category == 'Customer':
            if Customer.objects.filter(email=email).exists():
                return render(request,'signup.html',{'error':"Email already exists"})
            else:
                data = Customer(firstname=firstname, lastname=lastname,email=email, password=password,phnno=phoneno)
                data.save()
                return redirect('signin')
        if category == 'Cateror':
            if Cateror.objects.filter(email=email).exists():
                return render(request,'signup.html',{'error':"Email already exists"})
            else:
                data = Cateror(firstname=firstname, lastname=lastname,email=email, password=password,phnno=phoneno)
                data.save()
                return redirect('signin')
        if category == 'Decorator':
            if Decorator.objects.filter(email=email).exists():
                return render(request,'signup.html',{'error':"Email already exists"})
            else:
                data = Decorator(firstname=firstname, lastname=lastname,email=email, password=password,phnno=phoneno)
                data.save()
                return redirect('signin')
    elif request.session.has_key('username'):
        return redirect('home')
    else:
        return render(request,"signup.html")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def u_logout(request):
    if request.session.has_key('username'):
        del request.session['username']
    if request.session.has_key('phonno'):
        del request.session['phonno']
    if request.session.has_key('email'):
        del request.session['email']        
    if request.session.has_key('lname'):
        del request.session['lname']        
    return redirect('home')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)  
def book_event(request):
    if not request.session.has_key('username'):
        return redirect('signin')
    # if request.method == "POST":
    #     event_type = request.POST['event_type']
    #     starting_date = request.POST['strating_date']
    #     ending_date = request.POST['ending_date']
    #     event_time = request.POST['event_time']
    #     data = Event(customer_name=request.session['username'],email=request.session['email'],phnno=request.session['phonno'],starting_date=starting_date,ending_date=ending_date,event_time=event_time,event_type=event_type)
    #     data.save()
    #     messages.success(request,"Event booked Successfully")
    #     return redirect("home")
    else:
        data = Event_Type.objects.all()
        year= date.today().year+10
        month = date.today().month+1
        day = date.today().day
        if len(str(month)) != 2:
            month = "0{}".format(month)
        return render(request,'book_event.html',{'username':request.session['username'],'email':request.session['email'],'phonno':request.session['phonno'],'data':data,'date':date.today().strftime("%Y-%m-%d"),'mdate':"{}-{}-{}".format(year,month,day)})

def show_data(request):
    if not request.session.has_key('username'):
        return redirect('signin')
    else:
        halls = Hall.objects.all()
        return render(request,"show_hall.html",{'halls':halls, 'media_url':settings.MEDIA_URL})

def view_hall(request):
    if not request.session.has_key('username'):
        return redirect('home')
    else:
        request.session['persons'] = request.POST['nop']
        request.session['event_time'] = request.POST['event_time']
        request.session['event_type'] = request.POST['event_type']
        if request.POST['event_type'] == 'Birthday':
            request.session['event_date'] = request.POST['event_date']
        else:
            request.session['strating_date'] = request.POST['strating_date']
            request.session['ending_date'] = request.POST['ending_date']
        halls = Hall.objects.all()
        return render(request,"show_hall.html",{'halls':halls, 'media_url':settings.MEDIA_URL})

def select_hall(request,id):
    if not request.session.has_key('username'):
        return redirect('home')
    else:
        halls = Hall.objects.all()
        hall = Hall.objects.values_list('name','address','hall_rent').get(id=id)
        request.session['hall_id'] = id
        request.session['hall_name']=hall[0]
        request.session['hall_address']= hall[1]
        request.session['hall_rent']= hall[2]
        # print(request.session['hall_image'])
        return render(request,"show_hall.html",{'halls':halls,'id':id,'media_url':settings.MEDIA_URL})
def read_more(request,id):
    if not request.session.has_key('username'):
        return redirect('home')
    # if not request.session.has_key('hall_id'):
    #     return redirect(show_data)
    else:
        hall = Hall.objects.get(pk=id)
        return render(request,'read_more.html',{'hall':hall,'media_url':settings.MEDIA_URL,})

def view_packages(request):
    if request.session['event_type'] == 'Birthday':
        packages = Package.objects.all()
    elif request.session['event_type'] == 'Wedding':
        packages = Wedding_Package.objects.all()
    else:
        packages = Corporate_Package.objects.all()
    return render(request,'packages.html',{'packages':packages,'nop':request.session['persons'],'event_type':request.session['event_type']})
    

def birthday_event(request):
    if request.session.has_key('username'):
        return render(request, 'Birthday.html',{'username':request.session['username']})
    else:
        return render(request, 'Birthday.html')

def corporate_event(request):
    if request.session.has_key('username'):
        return render(request, 'corporate.html',{'username':request.session['username']})
    else:
        return render(request, 'corporate.html')

def wedding_event(request):
    if request.session.has_key('username'):
        return render(request, 'wedding.html',{'username':request.session['username']})
    else:
        return render(request, 'wedding.html')

def services(request):
    if request.session.has_key('username'):
        return render(request, 'services.html',{'username':request.session['username']})
    else:
        return render(request, 'services.html')

def select_packages(request,id):
    if request.session['event_type'] == 'Birthday':
        packages = Package.objects.all()
        package = Package.objects.values_list('Package_name','Price_per_person').get(id=id)
        request.session['package_name'] = package[0]
        request.session['Price_per_person'] = package[1]
        # print(request.session['Price_per_person'])
        selected = id
    elif request.session['event_type'] == 'Wedding':
        packages = Wedding_Package.objects.all()
        package = Wedding_Package.objects.values_list('Package_name','person_capacity','Price_per_extra_day','Price_per_extra_fifty_person','No_of_days','package_price').get(id=id)
        request.session['package_name'] = package[0]
        request.session['person_capacity'] = package[1]
        request.session['Price_per_extra_day'] = package[2]
        request.session['Price_per_extra_fifty_person'] = package[3]
        request.session['No_of_days'] = package[4]
        request.session['package_price'] = package[5]
        # print(request.session['Price_per_person'])
        selected = id
    else:
        packages = Corporate_Package.objects.all()
        package = Corporate_Package.objects.values_list('Package_name','person_capacity','Price_per_extra_day','Price_per_extra_fifty_person','No_of_days','package_price').get(id=id)
        request.session['package_name'] = package[0]
        request.session['person_capacity'] = package[1]
        request.session['Price_per_extra_day'] = package[2]
        request.session['Price_per_extra_fifty_person'] = package[3]
        request.session['No_of_days'] = package[4]
        request.session['package_price'] = package[5]
        # print(request.session['Price_per_person'])
        selected = id
    return render(request,'packages.html',{'packages':packages,'selected':selected,'nop':request.session['persons'],'event_type':request.session['event_type']})

def confirm_booking(request):
    # halls = Hall.objects.filter(id=request.session['hall_id']).update(is_booked=True)
    context = {
        'name': request.session['username'],
        'email':  request.session['email'],
        'phonno': request.session['phonno'],
        'nop': request.session['persons'],
        'package_name': request.session['package_name'],
        'event_type' :  request.session['event_type'],
        'event_time':request.session['event_time'],
        'hall_name' : request.session['hall_name'],
        'hall_rent' : request.session['hall_rent'],
        'hall_address': request.session['hall_address'],
    }
    if request.session['event_type'] == "Birthday":
        context['event_date'] = request.session['event_date']
        total = (request.session['Price_per_person'] * float(request.session['persons'])) + request.session['hall_rent']
        context['total'] = total
        context['price_per_person'] = request.session['Price_per_person']
    elif request.session['event_type'] == 'Wedding':
        context['strating_date'] = request.session['strating_date']
        context['ending_date'] = request.session['ending_date']
        context['No_of_days'] = request.session['No_of_days']
        context['Price_per_extra_fifty_person'] = request.session['Price_per_extra_fifty_person']
        context['Price_per_extra_day'] = request.session['Price_per_extra_day']
        d0 = context['strating_date'].split('-')
        d1 = context['ending_date'].split('-')
        diff = int(d1[2]) - int(d0[2]) + 1
        extra_days = diff - context['No_of_days']
        extra_person = (int(context['nop']) - request.session['person_capacity'])/50
        if(request.session['package_name'] == 'Silver Package'):
            if ((diff > 2)  and (int(context['nop']) > 100)):
                total = request.session['package_price']+(extra_days*int(context['Price_per_extra_day']))+(extra_person*int(context['Price_per_extra_fifty_person']))+request.session['hall_rent']
            elif ((diff > 2) and (int(context['nop']) <= 100)):
                total = request.session['package_price']+(extra_days*int(context['Price_per_extra_day']))+request.session['hall_rent']
            elif ((diff <= 2) and (int(context['nop']) > 100)):
                total = request.session['package_price']+(extra_person*int(context['Price_per_extra_fifty_person']))+request.session['hall_rent']
            else:
                total = request.session['package_price'] + request.session['hall_rent']
        elif(request.session['package_name'] == 'Gold Package'):
            if ((diff > 4)  and (int(context['nop']) > 300)):
                total = request.session['package_price']+(extra_days*int(context['Price_per_extra_day']))+(extra_person*int(context['Price_per_extra_fifty_person']))+request.session['hall_rent']
               
            elif ((diff > 4) and (int(context['nop']) <= 300)):
                total = request.session['package_price']+(extra_days*int(context['Price_per_extra_day']))+request.session['hall_rent']
            elif ((diff <= 4) and (int(context['nop']) > 300)):
                total = request.session['package_price']+(extra_person*int(context['Price_per_extra_fifty_person']))+request.session['hall_rent']
            else:
                total = request.session['package_price'] + request.session['hall_rent']
        else:
            if ((diff > 6)  and (int(context['nop']) > 500)):
                total = request.session['package_price']+(extra_days*int(context['Price_per_extra_day']))+(extra_person*int(context['Price_per_extra_fifty_person']))+request.session['hall_rent']
            
            elif ((diff > 6) and (int(context['nop']) <= 500)):
                total = request.session['package_price']+(extra_days*int(context['Price_per_extra_day']))+request.session['hall_rent']
            elif ((diff <= 6) and (int(context['nop']) > 500)):
                total = request.session['package_price']+(extra_person*int(context['Price_per_extra_fifty_person']))+request.session['hall_rent']
            else:
                total = request.session['package_price'] + request.session['hall_rent']
            context['total'] = total
            request.session['total'] = total
    else:
        context['strating_date'] = request.session['strating_date']
        context['ending_date'] = request.session['ending_date']
        context['No_of_days'] = request.session['No_of_days']
        context['Price_per_extra_fifty_person'] = request.session['Price_per_extra_fifty_person']
        context['Price_per_extra_day'] = request.session['Price_per_extra_day']
        d0 = context['strating_date'].split('-')
        d1 = context['ending_date'].split('-')
        diff = int(d1[2]) - int(d0[2]) + 1
        extra_days = diff - context['No_of_days']
        extra_person = (int(context['nop']) - request.session['person_capacity'])/50
        if(request.session['package_name'] == 'Silver Package'):
            if ((diff > 2)  and (int(context['nop']) > 100)):
                total = request.session['package_price']+(extra_days*int(context['Price_per_extra_day']))+(extra_person*int(context['Price_per_extra_fifty_person']))+request.session['hall_rent']
            elif ((diff > 2) and (int(context['nop']) <= 100)):
                total = request.session['package_price']+(extra_days*int(context['Price_per_extra_day']))+request.session['hall_rent']
            elif ((diff <= 2) and (int(context['nop']) > 100)):
                total = request.session['package_price']+(extra_person*int(context['Price_per_extra_fifty_person']))+request.session['hall_rent']
            else:
                total = request.session['package_price'] + request.session['hall_rent']
        elif(request.session['package_name'] == 'Gold Package'):
            if ((diff > 3)  and (int(context['nop']) > 300)):
                total = request.session['package_price']+(extra_days*int(context['Price_per_extra_day']))+(extra_person*int(context['Price_per_extra_fifty_person']))+request.session['hall_rent']
               
            elif ((diff > 3) and (int(context['nop']) <= 300)):
                total = request.session['package_price']+(extra_days*int(context['Price_per_extra_day']))+request.session['hall_rent']
            elif ((diff <= 3) and (int(context['nop']) > 300)):
                total = request.session['package_price']+(extra_person*int(context['Price_per_extra_fifty_person']))+request.session['hall_rent']
            else:
                total = request.session['package_price'] + request.session['hall_rent']
        else:
            if ((diff > 4)  and (int(context['nop']) > 500)):
                total = request.session['package_price']+(extra_days*int(context['Price_per_extra_day']))+(extra_person*int(context['Price_per_extra_fifty_person']))+request.session['hall_rent']
            
            elif ((diff > 4) and (int(context['nop']) <= 500)):
                total = request.session['package_price']+(extra_days*int(context['Price_per_extra_day']))+request.session['hall_rent']
            elif ((diff <= 4) and (int(context['nop']) > 500)):
                total = request.session['package_price']+(extra_person*int(context['Price_per_extra_fifty_person']))+request.session['hall_rent']
            else:
                total = request.session['package_price'] + request.session['hall_rent']
    context['total'] = total
    request.session['total'] = total
    messages.success(request,"Event Booked Successfully")
    return render(request,'booking_confirmed.html',context)

def silver_read_more(request):
    if not request.session.has_key('username'):
        return redirect(signin)
    else:
        if request.session['event_type'] == 'Birthday':
            package = Package.objects.all()
            request.session['package_id'] = 1
            if request.session.has_key('username') and request.session.has_key('persons'):
                return render(request,'silver_package.html',{'nop': request.session['persons'],'username':request.session['username'],'package':package})
            if request.session.has_key('username'):
                return render(request,'silver_package.html',{'username':request.session['username'],'package':package})
            else:
                return render(request,'silver_package.html')
        elif request.session['event_type'] == 'Wedding':
            package = Wedding_Package.objects.all()
            request.session['package_id'] = 1
            if request.session.has_key('username') and request.session.has_key('persons'):
                return render(request,'wedding_silver_package.html',{'nop': request.session['persons'],'username':request.session['username'],'total':request.session['total'],'package':package})
            if request.session.has_key('username'):
                return render(request,'wedding_silver_package.html',{'username':request.session['username'],'package':package})
            else:
                return render(request,'wedding_silver_package.html')
        elif request.session['event_type'] == 'Corporate':
            package = Corporate_Package.objects.all()
            request.session['package_id'] = 1
            if request.session.has_key('username') and request.session.has_key('persons'):
                return render(request,'corporate_silver_package.html',{'nop': request.session['persons'],'username':request.session['username'],'total':request.session['total'],'package':package})
            if request.session.has_key('username'):
                return render(request,'corporate_silver_package.html',{'username':request.session['username'],'package':package})
            else:
                return render(request,'corporate_silver_package.html')
        else:
            return redirect(book_event)
def gold_read_more(request):
    if not request.session.has_key('username'):
        return redirect(signin)
    else:
        if request.session['event_type'] == 'Birthday':
            package = Package.objects.all()
            if request.session.has_key('username') and request.session.has_key('persons'):
                return render(request,'silver_package.html',{'nop': request.session['persons'],'username':request.session['username'],'total':request.session['total'],'package':package})
            if request.session.has_key('username'):
                return render(request,'gold_package.html',{'nop': request.session['persons'],'username':request.session['username'],'package':package})
            else:
                return render(request,'gold_package.html')
        elif request.session['event_type'] == 'Wedding':
            package = Wedding_Package.objects.all()
            request.session['package_id'] = 1
            if request.session.has_key('username') and request.session.has_key('persons'):
                return render(request,'wedding_gold_package.html',{'nop': request.session['persons'],'total':request.session['total'],'username':request.session['username'],'package':package})
            if request.session.has_key('username'):
                return render(request,'wedding_gold_package.html',{'username':request.session['username'],'package':package})
            else:
                return render(request,'wedding_gold_package.html')
        elif request.session['event_type'] == 'Corporate':
            package = Corporate_Package.objects.all()
            if request.session.has_key('username') and request.session.has_key('persons'):
                return render(request,'corporate_gold_package.html',{'nop': request.session['persons'],'total':request.session['total'],'username':request.session['username'],'package':package})
            if request.session.has_key('username'):
                return render(request,'corporate_gold_package.html',{'username':request.session['username'],'package':package})
            else:
                return render(request,'corporate_gold_package.html')
        else:
            return redirect(book_event)    

def platinum_read_more(request):
    if not request.session.has_key('username'):
        return redirect(signin)
    else:
        if request.session['event_type'] == 'Birthday':
            package = Package.objects.all()
            if request.session.has_key('username') and request.session.has_key('persons'):
                return render(request,'platinum_package.html',{'nop': request.session['persons'],'total':request.session['total'],'username':request.session['username'],'package':package})
            if request.session.has_key('username'):
                return render(request,'platinum_package.html',{'nop': request.session['persons'],'username':request.session['username'],'package':package})
            else:
                return render(request,'platinum_package.html')
        elif request.session['event_type'] == 'Wedding':
            package = Wedding_Package.objects.all()
            if request.session.has_key('username') and request.session.has_key('persons'):
                return render(request,'wedding_platinum_package.html',{'nop': request.session['persons'],'total':request.session['total'],'username':request.session['username'],'package':package})
            if request.session.has_key('username'):
                return render(request,'wedding_platinum_package.html',{'nop': request.session['persons'],'username':request.session['username'],'package':package})
            else:
                return render(request,'wedding_platinum_package.html')
        elif request.session['event_type'] == 'Corporate':
            package = Corporate_Package.objects.all()
            if request.session.has_key('username') and request.session.has_key('persons'):
                return render(request,'corporate_platinum_package.html',{'nop': request.session['persons'],'total':request.session['total'],'username':request.session['username'],'package':package})
            if request.session.has_key('username'):
                return render(request,'corporate_platinum_package.html',{'username':request.session['username'],'package':package})
            else:
                return render(request,'corporate_platinum_package.html')
        else:
            return redirect(book_event)    
def select(request):
        package = Package.objects.values_list('Package_name','Price_per_person').get(id=request.session['package_id'])
        request.session['package_name'] = package[0]
        request.session['Price_per_person'] = package[1]
        # del request.session['package_id']
        return render(request,"silver_package.html",{"id":request.session['package_id'],'username':request.session['username']})

def c_pack(request):
    return render(request,"customize_package.html")

def confirm(request):
    # print(request.session['event_type'])
    if request.session.has_key('event_date'):
        total = (request.session['Price_per_person'] * float(request.session['persons'])) + request.session['hall_rent']
        events = Event(customer_name=request.session['username'], email = request.session['email'], no_of_persons = request.session['persons'],phnno = request.session['phonno'],event_type =  request.session['event_type'],starting_date = request.session['event_date'],ending_date = request.session['event_date'],event_time = request.session['event_time'],selected_package = request.session['package_name'],selected_hall = request.session['hall_name'],selected_cateror = " ",selected_decorator = " ",total_amount = total)
    else:
        # print(request.session['strating_date'])
        events = Event(customer_name=request.session['username'], email = request.session['email'], no_of_persons = request.session['persons'],phnno = request.session['phonno'],event_type =  request.session['event_type'],starting_date = request.session['strating_date'],ending_date = request.session['ending_date'],event_time = request.session['event_time'],selected_package = request.session['package_name'],selected_hall = request.session['hall_name'],selected_cateror = " ",selected_decorator = " ",total_amount = request.session['total'])
        if request.session.has_key('total'):
            del request.session['total']
    events.save()
    request.session['is_hall_booked'] = True
    return redirect('home')
    
def profile(request):
    if request.method == "GET":
        if request.session.has_key('username'):
            context = {
                'name': request.session['username']+" "+request.session['lname'],
                'username':request.session['username'],
                'email':  request.session['email'],
                'phonno': request.session['phonno'],
                'b_event': Event.objects.filter(email=request.session['email'],event_type='Birthday').all(),
                'w_event': Event.objects.filter(email=request.session['email'],event_type='Wedding').all(),
                'c_event': Event.objects.filter(email=request.session['email'],event_type='Corporate').all()
            }
            # print(context['b_event'])
            return render(request,'profile.html',context)
        else:
            return render(request,'login.html')
    else:
        firstname = request.POST['fname']
        lastname = request.POST['lname']
        email = request.POST['email']
        phoneno = request.POST['phno']
        customer = Customer.objects.filter(email=request.session['email']).update(firstname=firstname, lastname=lastname,email=email,phnno=phoneno)
        new_event = Event.objects.filter(email=request.session['email']).update(email=email)
        request.session['username'] = firstname
        request.session['name'] = firstname + " " + lastname
        request.session['phonno'] = phoneno
        request.session['email'] = email
        context = {
                'name': request.session['name'],
                'username':request.session['username'],
                'email':  request.session['email'],
                'phonno': request.session['phonno'],
                'b_event': Event.objects.filter(email=request.session['email'],event_type='Birthday').all(),
                'w_event': Event.objects.filter(email=request.session['email'],event_type='Wedding').all(),
                'c_event': Event.objects.filter(email=request.session['email'],event_type='Corporate').all()
            }
        return render(request,'profile.html',context)