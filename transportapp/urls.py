from django.urls import path
from . import views
urlpatterns=[
    path("",views.home,name='home'),
    path("About_us/",views.aboutus,name='aboutus'),
    path("Contact_us/",views.contactus,name='contactus'),
    path("Truck_type/",views.trucktype,name='trucktype'),
    path("Login/",views.login,name='login'),
    path("Sign_up/",views.signup,name='signup'),
    path("Feedback/",views.feedback,name='feedback'),
    path("FAQ/",views.faq,name='faq'),
    path("fare/",views.fare,name='fare'),
    path("booking/",views.booking,name='booking'),
    path("Review/",views.review,name="review"),
    path("c_message/",views.user_compose,name="message"),
    path("view_profile/",views.view_profile,name="view_profile"),
    path("edit_profile/",views.edit_profile,name="edit_profile"),
    path("user_logout/",views.user_logout,name="user_logout"),
    path("inbox/",views.inbox,name="inbox"),
    path("sent/",views.sent,name="sent"),
    path("delete_inbox/",views.delete_inbox,name="delete_inbox"),
    path("delete_sent/",views.delete_sent,name="delete_inbox"),
    path("pay_book/",views.payment_booking,name="payment_booking"),
]