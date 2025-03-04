from django.shortcuts import render,HttpResponse
from .models import Contact,FeedBack_Rating,customer_signup,check_fare,Scheme_Offers,vehicle_manage,user_message,Goods_type,Vehicle_booking
from django.contrib import messages
# Create your views here.
def home(request):
    # return HttpResponse("<h1>Hii</h1>")
    offer_list=Scheme_Offers.objects.all()
    # print(type(offer_list))
    # print(offer_list)
    context={"offer_key":offer_list}
    return render(request,'transportapp/html/index.html',context)

def aboutus(request):
    return render(request,'transportapp/html/aboutus.html')

def contactus(request):
    if request.method=='GET':
        return render(request,'transportapp/html/contactus.html')
    if request.method=='POST':
        name=request.POST["user_name"]
        email=request.POST["user_email"]
        phone=request.POST["user_phone"]
        city=request.POST["user_city"]
        message=request.POST["user_message"]
        contact_obj=Contact(name=name,email=email,phone=phone,city=city,message=message)
        contact_obj.save()
        messages.success(request,"Thank you for Contacting Us")
        return render(request,'transportapp/html/contactus.html')
    
def demo(request):
    return render(request,'transportapp/html/demo_boostrap.html')

def trucktype(request):
    return render(request,'transportapp/html/trucktype.html')

def login(request):
    if request.method=='GET':
        return render(request,'transportapp/user/login.html')
    if request.method=='POST':
        id=request.POST["u_id"]
        password=request.POST["u_pass"]
        user_list=customer_signup.objects.filter(email=id,password=password)
        if len(user_list)>0:
            request.session["session_key"]=id
            return render(request,'transportapp/user/user_home.html')
        else:
            messages.error(request,"Invalid ID and Password.!!")
            return render(request,'transportapp/user/login.html')
        
def signup(request):
    if request.method=='GET':
        return render(request,'transportapp/user/signup.html')
    if request.method=='POST':
        fname=request.POST["f_name"]
        lname=request.POST["l_name"]
        email=request.POST["email"]
        phone=request.POST["phone"]
        password=request.POST["password"]
        signup_obj=customer_signup(fname=fname,lname=lname,email=email,phone=phone,password=password)
        signup_obj.save()
        messages.success(request,"You are successfully register")
        return render(request,'transportapp/user/signup.html')
    
def feedback(request):
    if request.method=='GET':
        return render(request,'transportapp/html/feedback.html')
    if request.method=='POST':
        name=request.POST["u_name"]
        email=request.POST["u_email"]
        message=request.POST["u_message"]
        rating=request.POST["rating"]
        feedback_obj=FeedBack_Rating(name=name,email=email,feedback_text=message,ratings=rating)
        feedback_obj.save()
        messages.success(request,"Thank you for your feedback")
        # print("Feedback Save Successfully")
        return render(request,'transportapp/html/feedback.html')
    
def faq(request):
    return render(request,'transportapp/html/faq.html')

def fare(request):
    if request.method=='POST':
        # print("in fare")
        if "session_key" in request.session.keys():
            pick=request.POST["pick"]
            drop=request.POST["drop"]
            distance=request.POST["distance"]
            fare_obj=check_fare(pick_up=pick,drop=drop,distance=distance)
            fare_obj.save()
            vehicle_list=vehicle_manage.objects.all()
            fare_object=check_fare.objects.get(id=fare_obj.id)
            type_list=Goods_type.objects.all()
            context={"vehicle_key":vehicle_list,"fare_key":fare_object,"type_key":type_list}
            return render(request,'transportapp/html/booking.html',context)
        else:
            messages.error(request,"Please do Login first") 
            return render(request,'transportapp/user/login.html')
        
def booking(request):
    if request.method=='POST':
        item_type=request.POST["itemtype"]
        id=request.POST["rd"]
        truck_type=request.POST["txt"+id]
        # print(item_type," ",id," ",truck_type)
        return render(request,'transportapp/user/pay_book.html')
        

        
def review(request):
    feed_list=FeedBack_Rating.objects.all()
    context={"feed_key":feed_list}
    return render(request,'transportapp/html/review.html',context)

def message(request):
    return render(request,'transportapp/html/message.html')

def view_profile(request):
    user_id=request.session["session_key"]#fetching value from session
    user_obj=customer_signup.objects.get(email=user_id)
    context={"user_key":user_obj}
    return render(request,'transportapp/user/view_profile.html',context)

def edit_profile(request):
    if request.method =='GET':
        user_id=request.session["session_key"]#fetching value from session
        user_obj=customer_signup.objects.get(email=user_id)
        context={"user_key":user_obj}
        return render(request,'transportapp/user/edit_profile.html',context)
    if request.method =='POST':
        m_phone=request.POST['phone']
        user_id=request.session["session_key"]#fetching value from session
        user_obj=customer_signup.objects.get(email=user_id)
        user_obj.phone=m_phone
        user_obj.save()
        context={"user_key":user_obj}
        return render(request,'transportapp/user/edit_profile.html',context)
    
def user_logout(request):
    del request.session["session_key"]
    offer_list=Scheme_Offers.objects.all()
    context={"offer_key":offer_list}
    return render(request,'transportapp/html/index.html',context)

def user_compose(request):
    if request.method =='GET':
        return render(request,'transportapp/user/compose_message.html')
    if request.method =='POST':
        sender_id=request.session["session_key"]
        receiver_id=request.POST["r_id"]
        subject=request.POST["sub"]
        message=request.POST["message"]
        com_obj=user_message(sender_id=sender_id,receiver_id=receiver_id,subject=subject,message=message)
        com_obj.save()
        messages.success(request,"Your message is compose successfully")
        return render(request,'transportapp/user/compose_message.html')

def inbox(request):
    receiver_id=request.session["session_key"]
    message_list=user_message.objects.filter(receiver_id=receiver_id,receiver_status="False")
    # print(message_list)
    context={"msg_key":message_list}
    return render(request,'transportapp/user/user_inbox.html',context)

def sent(request):
    sender_id=request.session["session_key"]
    message_list=user_message.objects.filter(sender_id=sender_id,sender_status="False")
    # print(message_list)
    context={"msg_key":message_list}
    return render(request,'transportapp/user/user_sent.html',context)

def delete_inbox(request):
    receiver_id=request.session["session_key"]
    msgid_list=request.POST.getlist("checkmsg")
    for m_id in msgid_list:
        msg_obj=user_message.objects.get(id=m_id)
        msg_obj.receiver_status="True"
        msg_obj.save()
    message_list=user_message.objects.filter(receiver_id=receiver_id,receiver_status="False")
    context={"msg_key":message_list}
    return render(request,'transportapp/user/user_inbox.html',context)

def delete_sent(request):
    sender_id=request.session["session_key"]
    msgid_list=request.POST.getlist("checkmsg")
    for m_id in msgid_list:
        msg_obj=user_message.objects.get(id=m_id)
        msg_obj.sender_status="True"
        msg_obj.save()
    message_list=user_message.objects.filter(sender_id=sender_id,sender_status="False")
    context={"msg_key":message_list}
    return render(request,'transportapp/user/user_sent.html',context)

def payment_booking(request):
    if request.method=='POST':
        user_id=request.session["session_key"]
        truck_id=request.POST["rd"]  
        item_type=request.POST["itemtype"] 
        pick=request.POST["pick"]
        drop=request.POST["drop"] 
        booking_date=request.POST["bookingdate"]
        truck_type=request.POST["txt"+truck_id]
        book_obj=Vehicle_booking(user_id==user_id,truck_id==truck_id,item_type==item_type,pick==pick,drop==drop,booking_date==booking_date,truck_type==truck_type)
        book_obj.save() 
        user_obj=customer_signup.objects.get(email=user_id)
        context={"book_key":book_obj,"name_key":user_obj}
        return render(request,'transportapp/user/pay_book.html',context)
     
              
