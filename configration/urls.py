from django.urls import path
from .views import get_users


urlpatterns = [
     path('users',get_users,name='users' ),
    # path('admin/', admin.site.urls),
    # path('', include("configration.urls")),
    

]
