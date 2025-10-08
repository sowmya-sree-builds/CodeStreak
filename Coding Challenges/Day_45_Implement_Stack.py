#  Day 45: Implement Stack using List

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(f"Pushed {item}")

    def pop(self):
        if not self.is_empty():
            print(f"Popped {self.stack[-1]}")
            return self.stack.pop()
        print("Stack is empty!")

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None

    def is_empty(self):
        return len(self.stack) == 0

    def display(self):
        print("Stack:", self.stack)


# 🧩 Test
s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.display()
s.pop()
s.display()
print("Top Element:", s.peek())
