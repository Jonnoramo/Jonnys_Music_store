from django.conf.urls import url
from paypal_store import views as paypal_views

urlpatterns = [
    url(r'^paypal-return', paypal_views.paypal_return),
    url(r'^paypal-cancel', paypal_views.paypal_cancel),
]