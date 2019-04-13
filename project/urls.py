from django.conf.urls import *

from ammamanager.views import ammamanager, gyms, promotions

urlpatterns = [
    # Examples:
    url(r'^$', include('ammamanager.urls')),
    url(r'^accounts', include('django.contrib.auth.urls')),
    url(r'^accounts/signup/', ammamanager.SignUpView.as_view(), name='signup'),
    url(r'^accounts/signup/gym/', gyms.GymSignUpView.as_view(), name='gym_signup'),
    url(r'^accounts/signup/promotion/', promotions.PromotionSignUpView.as_view(), name='promotion_signup'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]

