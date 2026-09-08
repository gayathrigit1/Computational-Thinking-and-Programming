
from dataclasses import dataclass, field
from collections import deque
from typing import Generic, TypeVar

T = TypeVar("T")


# =========================
# Stack Implementation
# =========================

@dataclass
class Stack(Generic[T]):
    items: list[T] = field(default_factory=list)

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items.pop()

    def peek(self) -> T:
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items[-1]

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def size(self) -> int:
        return len(self.items)


# =========================
# Queue Implementation
# =========================

@dataclass
class Queue(Generic[T]):
    items: deque[T] = field(default_factory=deque)

    def enqueue(self, item: T) -> None:
        self.items.append(item)

    def dequeue(self) -> T:
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items.popleft()

    def front(self) -> T:
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items[0]

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def size(self) -> int:
        return len(self.items)


# =========================
# Main Program
# =========================

# Stack Example
stack: Stack[int] = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

print("STACK")
print("Stack:", stack.items)
print("Top element:", stack.peek())
print("Popped element:", stack.pop())
print("Stack after pop:", stack.items)
print("Stack size:", stack.size())


# Queue Example
queue: Queue[str] = Queue()

queue.enqueue("A")
queue.enqueue("B")
queue.enqueue("C")

print("\nQUEUE")
print("Queue:", list(queue.items))
print("Front element:", queue.front())
print("Dequeued element:", queue.dequeue())
print("Queue after dequeue:", list(queue.items))
print("Queue size:", queue.size())