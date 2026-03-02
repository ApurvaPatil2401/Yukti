def fib_base(answer: str) -> bool:
    a = answer.lower()

    mentions_zero = "0" in a
    mentions_one = "1" in a
    mentions_return = "return" in a

    return mentions_zero and mentions_one and mentions_return


def fib_recursive_step(answer: str) -> bool:
    a = answer.lower()

    mentions_fib = "fib" in a
    mentions_minus1 = "-1" in a or "n-1" in a
    mentions_minus2 = "-2" in a or "n-2" in a
    mentions_add = "+" in a or "add" in a

    return mentions_fib and mentions_minus1 and mentions_minus2 and mentions_add


def two_sum_hash_reason(answer: str) -> bool:
    a = answer.lower()

    mentions_o1 = "o(1)" in a or "constant" in a
    mentions_nested = "nested" in a or "loop" in a
    mentions_faster = "faster" in a or "efficient" in a

    return mentions_o1 and mentions_faster


def two_sum_structure(answer: str) -> bool:
    a = answer.lower()

    mentions_key = "key" in a
    mentions_value = "value" in a
    mentions_index = "index" in a
    mentions_number = "number" in a or "num" in a

    return mentions_key and mentions_value and mentions_index and mentions_number