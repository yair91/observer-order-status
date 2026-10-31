from .subject import Subject


class OrderStatus(Subject):
    def __init__(self, order_id: str):
        super().__init__()
        self.order_id = order_id
        self.status = "NEW"

    def set_status(self, status: str) -> None:
        self.status = status
        self.notify(self.order_id, status)
