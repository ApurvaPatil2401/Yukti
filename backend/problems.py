problems = {
    "fibonacci": {
        "description": "Write a function to compute the nth Fibonacci number.",
        "steps": [
            {
                "question": "How would you define the base cases for recursion in computing the nth Fibonacci number?",
                "validator": "fib_base"
            },
            {
                "question": "After defining the base case, how would the recursive step combine smaller subproblems?",
                "validator": "fib_recursive_step"
            }
        ],
        "solution": """def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)"""
    },

    "two_sum": {
        "description": "Return indices of two numbers that add up to target.",
        "steps": [
            {
                "question": "Why would using a hash map improve lookup time compared to a nested loop approach?",
                "validator": "two_sum_hash_reason"
            },
            {
                "question": "What would you store as the key and value inside the hash map to make the lookup efficient?",
                "validator": "two_sum_structure"
            }
        ],
        "solution": """def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i"""
    }
}