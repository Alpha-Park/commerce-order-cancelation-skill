from client import OrderCancelationClient
def main():
    c = OrderCancelationClient()
    print(c.cancel_order("ORD-902", "shipped"))
if __name__ == '__main__':
    main()
