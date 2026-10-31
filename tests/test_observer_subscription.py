from order_status.analytics_observer import AnalyticsObserver
from order_status.customer_notifier import CustomerNotifier
from order_status.order_status import OrderStatus


def test_analytics_joins_and_unsubscribed_observer_stops_receiving():
    order = OrderStatus("A-200")
    customer = CustomerNotifier()
    analytics = AnalyticsObserver()
    order.subscribe(customer)
    order.subscribe(analytics)

    order.set_status("PAID")
    order.unsubscribe(customer)
    order.set_status("SHIPPED")

    assert customer.messages == ["A-200:PAID"]
    assert analytics.status_counts == {"PAID": 1, "SHIPPED": 1}
