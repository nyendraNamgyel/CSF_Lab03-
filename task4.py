class CustomerQueue:
    def __init__(self):
        self.queue = []

    def add_customer(self, name):
        self.queue.append(name)

    def serve_customer(self):
        if self.queue:
            return self.queue.pop(0)
        return "No customers"

    def display(self):
        return self.queue


cq = CustomerQueue()
cq.add_customer("Sonam")
cq.add_customer("Pema")
cq.add_customer("Karma")

print("Customers waiting:", cq.display())
served = cq.serve_customer()
print("Serving customer:", served)
print("Remaining queue:", cq.display())