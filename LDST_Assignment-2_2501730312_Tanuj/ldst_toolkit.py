# -------------------------------
# Task 1: Dynamic Array
# -------------------------------

class DynamicArray:
    def __init__(self, initial_capacity=2):
        self._capacity = initial_capacity
        self._size = 0
        # internal plain Python list just as fixed-size storage
        self._data = [None] * self._capacity

    def _resize(self, new_capacity):
        new_data = [None] * new_capacity
        for i in range(self._size):
            new_data[i] = self._data[i]
        self._data = new_data
        self._capacity = new_capacity

    def append(self, x):
        if self._size == self._capacity:
            # double capacity when full
            self._resize(self._capacity * 2)
        self._data[self._size] = x
        self._size += 1

    def pop(self):
        if self._size == 0:
            print("DynamicArray underflow: cannot pop from empty array")
            return None
        value = self._data[self._size - 1]
        self._data[self._size - 1] = None
        self._size -= 1
        return value

    def __len__(self):
        return self._size

    def __str__(self):
        return "[" + ", ".join(str(self._data[i]) for i in range(self._size)) + f"] (size={self._size}, capacity={self._capacity})"

    def print_array(self):
        print(self.__str__())


# -------------------------------
# Task 2: Linked List Operations
# -------------------------------

class SLLNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, x):
        new_node = SLLNode(x)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, x):
        new_node = SLLNode(x)
        if self.head is None:
            self.head = new_node
            return
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = new_node

    def delete_by_value(self, x):
        if self.head is None:
            print("SLL: List is empty, nothing to delete.")
            return

        # if head has the value
        if self.head.data == x:
            self.head = self.head.next
            return

        prev = None
        curr = self.head
        while curr is not None and curr.data != x:
            prev = curr
            curr = curr.next

        if curr is None:
            print(f"SLL: Value {x} not found, nothing deleted.")
            return

        prev.next = curr.next

    def traverse(self):
        elements = []
        curr = self.head
        while curr is not None:
            elements.append(str(curr.data))
            curr = curr.next
        print("SLL:", " -> ".join(elements) if elements else "Empty list")


class DLLNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    # we will treat position as 0-based index for delete_at_position
    def __init__(self):
        self.head = None

    def insert_at_end(self, x):
        new_node = DLLNode(x)
        if self.head is None:
            self.head = new_node
            return
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = new_node
        new_node.prev = curr

    def insert_after_node(self, target, x):
        # insert x after first occurrence of target
        curr = self.head
        while curr is not None and curr.data != target:
            curr = curr.next

        if curr is None:
            print(f"DLL: Target {target} not found, cannot insert after it.")
            return

        new_node = DLLNode(x)
        new_node.next = curr.next
        new_node.prev = curr
        if curr.next is not None:
            curr.next.prev = new_node
        curr.next = new_node

    def delete_at_position(self, pos):
        if self.head is None:
            print("DLL: List is empty, nothing to delete.")
            return

        if pos < 0:
            print("DLL: Invalid position, must be >= 0.")
            return

        curr = self.head
        idx = 0

        # delete head
        if pos == 0:
            self.head = curr.next
            if self.head is not None:
                self.head.prev = None
            return

        # traverse to the node at position pos
        while curr is not None and idx < pos:
            curr = curr.next
            idx += 1

        if curr is None:
            print("DLL: Position out of range, nothing deleted.")
            return

        # curr is node to delete
        if curr.next is not None:
            curr.next.prev = curr.prev
        if curr.prev is not None:
            curr.prev.next = curr.next

    def traverse_forward(self):
        elements = []
        curr = self.head
        while curr is not None:
            elements.append(str(curr.data))
            curr = curr.next
        print("DLL forward:", " <-> ".join(elements) if elements else "Empty list")


# -------------------------------
# Task 3: Stack & Queue using SLL
# -------------------------------

class Stack:
    # LIFO, use SinglyLinkedList, push/pop at head for O(1)
    def __init__(self):
        self._list = SinglyLinkedList()

    def push(self, x):
        self._list.insert_at_beginning(x)

    def pop(self):
        if self._list.head is None:
            print("Stack underflow: cannot pop from empty stack")
            return None
        value = self._list.head.data
        self._list.head = self._list.head.next
        return value

    def peek(self):
        if self._list.head is None:
            print("Stack is empty, nothing to peek")
            return None
        return self._list.head.data

    def is_empty(self):
        return self._list.head is None


class Queue:
    # FIFO, use SinglyLinkedList with head and tail for O(1) enqueue/dequeue
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, x):
        new_node = SLLNode(x)
        if self.tail is None:  # empty
            self.head = self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    def dequeue(self):
        if self.head is None:
            print("Queue underflow: cannot dequeue from empty queue")
            return None
        value = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return value

    def front(self):
        if self.head is None:
            print("Queue is empty, nothing at front")
            return None
        return self.head.data

    def is_empty(self):
        return self.head is None


# -------------------------------
# Task 4: Balanced Parentheses Checker
# -------------------------------

def is_balanced(expr):
    stack = Stack()
    # mapping of closing to opening
    pairs = {')': '(', '}': '{', ']': '['}

    for ch in expr:
        if ch in "({[":
            stack.push(ch)
        elif ch in ")}]":
            if stack.is_empty():
                return False
            top = stack.pop()
            if pairs[ch] != top:
                return False

    # if stack empty, everything matched
    return stack.is_empty()


# -------------------------------
# Main runner: run required test cases and print output
# -------------------------------

def main():
    print("=== Task 1: DynamicArray Tests ===")
    da = DynamicArray(initial_capacity=2)
    print("Initial:", da)
    for i in range(10):  # append 10+ items
        da.append(i)
        print(f"After append({i}):", da)
    # perform 3 pops
    print("Pop 1:", da.pop())
    print("After pop 1:", da)
    print("Pop 2:", da.pop())
    print("After pop 2:", da)
    print("Pop 3:", da.pop())
    print("After pop 3:", da)

    print("\n=== Task 2A: SinglyLinkedList Tests ===")
    sll = SinglyLinkedList()
    # insert 3 at beginning
    sll.insert_at_beginning(10)
    sll.traverse()
    sll.insert_at_beginning(20)
    sll.traverse()
    sll.insert_at_beginning(30)
    sll.traverse()
    # insert 3 at end
    sll.insert_at_end(40)
    sll.traverse()
    sll.insert_at_end(50)
    sll.traverse()
    sll.insert_at_end(60)
    sll.traverse()
    # delete one by value
    sll.delete_by_value(40)
    sll.traverse()

    print("\n=== Task 2B: DoublyLinkedList Tests ===")
    dll = DoublyLinkedList()
    # create base list
    dll.insert_at_end(1)
    dll.insert_at_end(2)
    dll.insert_at_end(3)
    dll.insert_at_end(4)
    dll.traverse_forward()
    # insert after a target
    dll.insert_after_node(2, 99)
    dll.traverse_forward()
    # delete at positions like 1 and last (0-based)
    dll.delete_at_position(1)
    dll.traverse_forward()
    # delete last position -> we need to know current length, but for simplicity try large index last-1 step-by-step
    dll.delete_at_position(3)  # adjust this index depending on current length
    dll.traverse_forward()

    print("\n=== Task 3A: Stack Tests ===")
    st = Stack()
    st.push(100)
    st.push(200)
    st.push(300)
    print("Stack peek:", st.peek())
    print("Stack pop:", st.pop())
    print("Stack pop:", st.pop())
    print("Stack pop:", st.pop())
    print("Stack pop (underflow):", st.pop())

    print("\n=== Task 3B: Queue Tests ===")
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print("Queue front:", q.front())
    print("Dequeue:", q.dequeue())
    print("Dequeue:", q.dequeue())
    print("Dequeue:", q.dequeue())
    print("Dequeue (underflow):", q.dequeue())

    print("\n=== Task 4: Balanced Parentheses Tests ===")
    tests = ["([])", "([)]", "(((", "", "{[()]}", "{[(])}", "[]{}()"]
    for t in tests:
        print(f"{t!r} -> {is_balanced(t)}")


if __name__ == "__main__":
    main()