from django.conf.urls import *

from .views import ammamanager, gyms, promotions
urlpatterns = [
    # Examples:
    url(r'', ammamanager.home, name='home'),
    url(r'^gyms', include(([
        url(r'^', gyms.GymHomeView.as_view(), name='gym_home'),
        url(r'^fighters/', gyms.ListFightersView.as_view(), name='fighter_list'),
        url(r'^fighters/<int:pk>', gyms.fighter_view, name='fighter'),
        url(r'^fighters/<int:pk>/<int:offer_pk>/accept', gyms.accept_fight, name='accept_fight'),
        url(r'^fighters/<int:pk>/delete', gyms.fighter_delete, name='fighter_delete'),
        url(r'^fighters/add/', gyms.FighterCreateView.as_view(), name='fighter_add'),
    ],'ammamanager'), namespace='gyms')),
     url(r'^promotions/', include(([
        url(r'^', promotions.PromotionHomeView.as_view(), name='promotion_home'),
        url(r'^events/', promotions.ListEventsView.as_view(), name='event_list'),
        url(r'^events/add/', promotions.EventCreateView.as_view(), name='event_add'),
        url(r'^events/<int:pk>/', promotions.EventView.as_view(), name='event'),
        url(r'^events/<int:pk>/finished', promotions.finished_event, name='finished_event'),
        url(r'^events/<int:pk>/bout/add', promotions.bout_add, name='bout_add'),
        url(r'^events/<int:pk>/bout/<int:bout_pk>/', promotions.BoutView, name='bout'),
        url(r'^events/<int:pk>/bout/<int:bout_pk>/finished/<int:fighter_pk>', promotions.finished_bout, name='finished_bout'),
        url(r'^events/<int:pk>/bout/<int:bout_pk>/offer/<int:fighter_pk>', promotions.offer, name='offer'),
        url(r'^events/<int:pk>/bout/<int:bout_pk>/removefighters', promotions.removeFighters, name='remove_fighters'),
        url(r'^events/<int:pk>/bout/<int:bout_pk>/offerfight', promotions.offer_fight, name='offer_fight'),
    ], 'ammamanager'), namespace='promotions')),
]
