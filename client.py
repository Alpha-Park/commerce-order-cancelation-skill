from typing import Dict, Any

class OrderCancelationClient:
    def cancel_order(self, order_id: str, current_status: str) -> Dict[str, Any]:
        cancelable_states = ["pending", "processing", "placed"]
        allowed = current_status.lower() in cancelable_states
        msg = f"Order {order_id} has been canceled and refund initiated." if allowed else f"Cannot cancel order {order_id} because status is {current_status}."
        return {
            "cancellation_approved": allowed,
            "refund_initiated": allowed,
            "status_message": msg
        }
