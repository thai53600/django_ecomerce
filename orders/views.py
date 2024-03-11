from rest_framework import views
from rest_framework.permissions import AllowAny
from backend_ecommerce.helpers import custom_response, parse_request
from django.http import Http404
from django.contrib.auth import get_user_model
from .models import Order, OrderDetail
from .serializers import OrderSerializer, OrderDetailSerializer
from products.models import Product
from .utils import make_paypal_payment, verify_paypal_payment
from decouple import config

User = get_user_model()


class OrderAPIView(views.APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        try:
            orders = Order.objects.all()
            serializers = OrderSerializer(orders, many=True)
            return custom_response('Get all categories successfully!', 'Success', serializers.data, 200)
        except:
            return custom_response('Get all categories failed!', 'Error', None, 400)

    def post(self, request):
        try:
            data = parse_request(request)
            user = User.objects.get(id=data['user_id'])
            order = Order(
                receiver_name=data['receiver_name'],
                receiver_phone=data['receiver_phone'],
                receiver_address=data['receiver_address'],
                description=data['description'],
                user_id=user
            )
            order.save()
            serializer = OrderSerializer(order)
            return custom_response('Create order successfully!', 'Success', serializer.data, 201)
        except Exception as e:
            return custom_response('Create order failed!', 'Error', [str(e)], 400)


class OrderDetailAPIView(views.APIView):
    permission_classes = [AllowAny]

    def get_object(self, id_slug):
        try:
            return Order.objects.get(id=id_slug)
        except:
            raise Http404

    def get(self, request, id_slug):
        try:
            order = self.get_object(id_slug)
            serializers = OrderSerializer(order)
            return custom_response('Get all order details successfully!', 'Success', serializers.data, 200)
        except:
            return custom_response('Get all order details failed!', 'Error', None, 400)

    def put(self, request, id_slug):
        try:
            data = parse_request(request)
            order = self.get_object(id_slug)
            serializer = OrderSerializer(order, data=data)
            if serializer.is_valid():
                serializer.save()
                return custom_response('Update order successfully!', 'Success', serializer.data, 200)
            else:
                return custom_response('Update order failed', 'Error', serializer.errors, 400)
        except:
            return custom_response('Update order failed', 'Error', "Order not found!", 400)

    def delete(self, request, id_slug):
        try:
            order = self.get_object(id_slug)
            order.delete()
            return custom_response('Delete order successfully!', 'Success', {"order_id": id_slug}, 204)
        except:
            return custom_response('Delete order failed!', 'Error', "Order not found!", 400)


class OrderDetailWithProductAPIView(views.APIView):
    permission_classes = [AllowAny]

    def get(self, request, order_id_slug):
        try:
            order_details = OrderDetail.objects.filter(order_id=order_id_slug).all()
            serializers = OrderDetailSerializer(order_details, many=True)
            return custom_response('Get all order detail successfully!', 'Success', serializers.data, 200)
        except:
            return custom_response('Get all order detail failed!', 'Error', None, 400)

    def post(self, request, order_id_slug):
        try:
            data = parse_request(request)
            order = Order.objects.get(id=data['order_id'])
            product = Product.objects.get(id=data['product_id'])
            order_detail = OrderDetail(
                amount=data['amount'],
                price=data['price'],
                discount=data['discount'],
                order_id=order,
                product_id=product
            )
            order_detail.save()
            serializer = OrderDetailSerializer(order_detail)
            return custom_response('Create order detail successfully!', 'Success', serializer.data, 201)
        except Exception as e:
            return custom_response('Create order detail failed!', 'Error', [str(e)], 400)


class OrderDetailWithProductDetailAPIView(views.APIView):
    permission_classes = [AllowAny]

    def get(self, request, order_id_slug, id_slug):
        try:
            order_detail = OrderDetail.objects.get(order_id=order_id_slug, id=id_slug)
            serializer = OrderDetailSerializer(order_detail)
            return custom_response('Get order detail successfully!', 'Success', serializer.data, 200)
        except:
            return custom_response('Get order detail failed!', 'Error', None, 400)

    def put(self, request, order_id_slug, id_slug):
        try:
            data = parse_request(request)
            order_detail = OrderDetail.objects.get(id=id_slug)
            serializer = OrderDetailSerializer(order_detail, data=data)
            if serializer.is_valid():
                serializer.save()
                return custom_response('Update order detail successfully!', 'Success', serializer.data, 200)
            else:
                return custom_response('Update order detail failed', 'Error', serializer.errors, 400)
        except:
            return custom_response('Update order detail failed', 'Error', "Order detail not found!", 400)

    def delete(self, request, order_id_slug, id_slug):
        try:
            order_detail = OrderDetail.objects.get(id=id_slug)
            order_detail.delete()
            return custom_response('Delete order detail successfully!', 'Success', {"order_detail_id": id_slug}, 204)
        except:
            return custom_response('Delete order detail failed!', 'Error', "Order detail not found!", 400)


class OrderCheckoutAPIView(views.APIView):
    permission_classes = [AllowAny]

    def get(self, request, order_id_slug):
        try:
            order = Order.objects.get(id=order_id_slug)
            checkResult = order.checkValidOrder()
            print('isValidOrder', checkResult)
            if not checkResult['status']:
                return custom_response(
                    'Create payment transaction failed!',
                    'Error',
                    {"reason": "Some products in cart has been out of stock!", "current_stock": checkResult['data']},
                    400
                )
            # Nếu đơn hàng đã thanh toán rồi thì cancel request luôn
            if order.is_paid:
                return custom_response('Create payment transaction failed!', 'Error', {"reason": "Order has been paid!"}, 400)
            # Lấy ra tổng tiền của đơn hàng
            order_total_price = order.total
            # Thực hiện tạo giao dịch
            status, payment_id, approved_url = make_paypal_payment(
                amount=order_total_price, currency="USD",
                return_url=config('FE_DOMAIN') + "/payment/success/",
                cancel_url=config('FE_DOMAIN') + "/payment/cancel/"
            )
            if status:
                # Nếu status = True -> Tạo giao dịch thành công
                return custom_response("Payment link has been successfully created", "success", data={
                    "approved_url": approved_url
                }, status_code=201)
            else:
                # Nếu status = False -> Tạo giao dịch thất bại
                return custom_response("Create payment transaction failed!", "failed", data={
                    "error": "Payment transaction failed"
                }, status_code=400)
        except Exception as e:
            return custom_response('Create payment transaction failed!', 'Error', [str(e)], 400)


class VerifyPaymentAPIView(views.APIView):
    permission_classes = [AllowAny]

    def post(self, request, order_id_slug):
        try:
            data = parse_request(request)
            payment_status = verify_paypal_payment(payment_id=data['payment_id'])
            print('payment_status', payment_status)
            # Giao dịch hợp lệ -> Chuyển trạng thái của Order
            if payment_status:
                order = Order.objects.get(id=data['order_id'])
                order.payment_id = data['payment_id']
                order.is_paid = True
                order.save()
                return custom_response("Payment has been verified!", "success", {}, status_code=200)
            else:
                # Giao dịch không hợp lệ hoặc không tồn tại
                return custom_response('Verify payment failed!', 'Error', {'payment': 'Verify payment failed!'}, 400)
        except Exception as e:
            return custom_response('Verify payment failed!', 'Error', [str(e)], 400)
