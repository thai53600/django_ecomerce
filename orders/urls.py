from django.urls import path
from orders import views

urlpatterns = [
    path("orders/", views.OrderAPIView.as_view()),
    path("orders/<slug:id_slug>/", views.OrderDetailAPIView.as_view()),
    path("orders/<slug:order_id_slug>/detail/", views.OrderDetailWithProductAPIView.as_view()),
    path("orders/<slug:order_id_slug>/detail/<slug:id_slug>/", views.OrderDetailWithProductDetailAPIView.as_view()),

    # Paypal payment
    path("orders/<slug:order_id_slug>/payment/", views.OrderCheckoutAPIView.as_view()),
    path("orders/<slug:order_id_slug>/payment/verify/", views.VerifyPaymentAPIView.as_view())
]
