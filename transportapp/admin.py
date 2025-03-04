from django.contrib import admin
from .models import Contact,FeedBack_Rating,Scheme_Offers,Employee,vehicle_manage,customer_signup,check_fare,Goods_type,user_message,Vehicle_booking
# to see data in tabular form
class Admin_Contact(admin.ModelAdmin):
    list_display=('name','email','phone','city','message','date')
    list_filter=['date']

class Admin_FeedBack_Rating(admin.ModelAdmin):
    list_display=('name','email','feedback_text','ratings','date')
    search_fields=('ratings',)
    list_filter=['ratings']

class Admin_Employee(admin.ModelAdmin):
    list_display=('name','email','phone','designation','experience','gender')
    search_fields=('designation','experience')

class Admin_Contact(admin.ModelAdmin):
    list_display=('name','email','phone','city','message','date')
    
class Admin_vehicle_manage(admin.ModelAdmin):
    list_display=('truck_type','truck_size','truck_capacity','truck_weight')
    list_filter=['truck_type','truck_weight']
        

# Register your models here.
admin.site.register(Contact,Admin_Contact)
admin.site.register(Scheme_Offers)
admin.site.register(FeedBack_Rating,Admin_FeedBack_Rating)
admin.site.register(Employee,Admin_Employee)
admin.site.register(vehicle_manage,Admin_vehicle_manage)
admin.site.register(customer_signup)
admin.site.register(check_fare)
admin.site.register(Vehicle_booking)
admin.site.register(Goods_type)
admin.site.register(user_message)
# admin.site.register(user_login)
# admin.site.register(Scheme_Offers)


admin.site.site_header="Move Masters Administrations"
admin.site.site_title="Move Masters Admin Dashboard "
admin.site.index_title="Welcome to Move Masters"





