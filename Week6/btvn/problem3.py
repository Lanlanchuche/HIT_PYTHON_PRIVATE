
class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.list = []

    # @property
    # def capacity(self):
    #     return self.capacity
    #
    # @capacity.setter
    # def capacity(self, capacity):
    #     self.capacity = capacity

    def initialization(self):
        pass

    def isEmpty(self):
        if len(self.list) == 0:
            return True
        else:
            return False

    def isFull(self):
        if len(self.list) == self.capacity:
            return True
        else:
            return False

    def pop(self):
        if len(self.list) > 0:
            return self.list.pop()
        else:
            return None


    def push(self, value):
        if len(self.list) < self.capacity:
            self.list.append(value)
            return True
        else:
            return False
    def top(self):
        if len(self.list) > 0:
            return self.list[-1]
        else:
            return None

stack1 = Stack(capacity=5)
stack1.push(1)
stack1.push(2)
print(stack1.isFull())
print(stack1.top())
print(stack1.pop())
print(stack1.top())
print(stack1.pop())
print(stack1.isEmpty())