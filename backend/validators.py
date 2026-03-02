def fib_base(answer: str) -> bool:
    a = answer.lower()
    return "0" in a and "1" in a and "return" in a


def fib_recursive_step(answer: str) -> bool:
    a = answer.lower()
    return ("fib" in a and
            ("n-1" in a or "-1" in a) and
            ("n-2" in a or "-2" in a) and
            ("+" in a or "add" in a))


def two_sum_hash_reason(answer: str) -> bool:
    a = answer.lower()
    return (("o(1)" in a or "constant" in a) and
            ("efficient" in a or "faster" in a))


def two_sum_structure(answer: str) -> bool:
    a = answer.lower()
    return ("key" in a and
            "value" in a and
            "index" in a and
            ("number" in a or "num" in a))

# Stack
def stack_reason(a): 
    a=a.lower()
    return "stack" in a and ("lifo" in a or "last" in a)

def stack_invalid_condition(a):
    a=a.lower()
    return "mismatch" in a or "empty" in a or "not stack" in a

# Two Pointers
def two_pointer_reason(a):
    a=a.lower()
    return "sorted" in a and ("two pointer" in a or "left" in a)

def two_pointer_logic(a):
    a=a.lower()
    return ("left" in a and "right" in a)

# Binary Search
def binary_reason(a):
    a=a.lower()
    return "sorted" in a and ("half" in a or "divide" in a)

def binary_pointer_logic(a):
    a=a.lower()
    return ("mid" in a and ("left" in a or "right" in a))

# Sliding Window
def sliding_window_reason(a):
    a=a.lower()
    return "window" in a or "two pointer" in a

def sliding_window_logic(a):
    a=a.lower()
    return "duplicate" in a or "shrink" in a or "set" in a

# Kadane
def kadane_reason(a):
    a=a.lower()
    return "negative" in a or "running" in a

def kadane_logic(a):
    a=a.lower()
    return "max" in a

# Linked List
def linked_list_reason(a):
    a=a.lower()
    return "pointer" in a or "prev" in a

def linked_list_logic(a):
    a=a.lower()
    return "head" in a or "loop" in a