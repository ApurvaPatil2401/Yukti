problems = {

    # 1️⃣ Recursion
    "fibonacci": {
        "description": "Write a function to compute the nth Fibonacci number.",
        "steps": [
            {
                "concept": "recursion base case",
                "questions": [
                    "What are the base cases in recursive Fibonacci?",
                    "Why do we need base cases in recursion?",
                    "How do you prevent infinite recursion in Fibonacci?"
                ],
                "validator": "fib_base"
            },
            {
                "concept": "recursive relation",
                "questions": [
                    "What recursive formula defines Fibonacci?",
                    "How does the function combine smaller subproblems?",
                    "How does Fibonacci call itself recursively?"
                ],
                "validator": "fib_recursive_step"
            }
        ],
        "solution": """def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)"""
    },

    # 2️⃣ Hashing
    "two sum": {
        "description": "Return indices of two numbers that add up to target.",
        "steps": [
            {
                "concept": "hash map efficiency",
                "questions": [
                    "Why is a hash map more efficient than nested loops?",
                    "How does hashing reduce time complexity in Two Sum?",
                    "Why does nested iteration scale poorly?"
                ],
                "validator": "two_sum_hash_reason"
            },
            {
                "concept": "hash map structure",
                "questions": [
                    "What should be stored as key and value in the hash map?",
                    "How do you store complement efficiently?",
                    "What information is needed to return indices?"
                ],
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
    },

    # 3️⃣ Stack
    "valid parentheses": {
        "description": "Check if a string of brackets is valid.",
        "steps": [
            {
                "concept": "stack reasoning",
                "questions": [
                    "Why is a stack suitable for matching parentheses?",
                    "What property of stacks helps validate brackets?",
                    "Why do we need LIFO behavior here?"
                ],
                "validator": "stack_reason"
            },
            {
                "concept": "invalid condition",
                "questions": [
                    "When does the bracket string become invalid?",
                    "What condition would make you return False?",
                    "How do mismatched pairs get detected?"
                ],
                "validator": "stack_invalid_condition"
            }
        ],
        "solution": """def isValid(s):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    for char in s:
        if char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False
        else:
            stack.append(char)
    return not stack"""
    },

    # 4️⃣ Two Pointers
    "sorted two sum": {
        "description": "Given a sorted array, find two numbers that add up to target.",
        "steps": [
            {
                "concept": "two pointers idea",
                "questions": [
                    "Why can two pointers work on a sorted array?",
                    "How does sorted order help reduce search space?",
                    "Why move left or right pointer conditionally?"
                ],
                "validator": "two_pointer_reason"
            },
            {
                "concept": "pointer movement logic",
                "questions": [
                    "When should you move left pointer?",
                    "When should you move right pointer?",
                    "How does pointer movement ensure O(n) complexity?"
                ],
                "validator": "two_pointer_logic"
            }
        ],
        "solution": """def two_sum_sorted(nums, target):
    left, right = 0, len(nums)-1
    while left < right:
        s = nums[left] + nums[right]
        if s == target:
            return [left, right]
        elif s < target:
            left += 1
        else:
            right -= 1"""
    },

    # 5️⃣ Binary Search
    "binary search": {
        "description": "Search for target in sorted array using binary search.",
        "steps": [
            {
                "concept": "divide and conquer",
                "questions": [
                    "Why must the array be sorted for binary search?",
                    "How does divide and conquer reduce complexity?",
                    "Why do we eliminate half the search space?"
                ],
                "validator": "binary_reason"
            },
            {
                "concept": "pointer update logic",
                "questions": [
                    "How do you update left and right pointers?",
                    "When do you move left to mid+1?",
                    "When do you move right to mid-1?"
                ],
                "validator": "binary_pointer_logic"
            }
        ],
        "solution": """def binary_search(nums, target):
    left, right = 0, len(nums)-1
    while left <= right:
        mid = (left+right)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid+1
        else:
            right = mid-1
    return -1"""
    },

    # 6️⃣ Sliding Window
    "longest substring": {
        "description": "Find length of longest substring without repeating characters.",
        "steps": [
            {
                "concept": "sliding window idea",
                "questions": [
                    "Why use two pointers in sliding window?",
                    "How does sliding window maintain valid substring?",
                    "Why not restart from every index?"
                ],
                "validator": "sliding_window_reason"
            },
            {
                "concept": "duplicate handling",
                "questions": [
                    "What happens when duplicate character appears?",
                    "How do you shrink the window?",
                    "How do you track seen characters?"
                ],
                "validator": "sliding_window_logic"
            }
        ],
        "solution": """def lengthOfLongestSubstring(s):
    seen = set()
    left = 0
    max_len = 0
    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        max_len = max(max_len, right-left+1)
    return max_len"""
    },

    # 7️⃣ Dynamic Programming
    "maximum subarray": {
        "description": "Find maximum subarray sum.",
        "steps": [
            {
                "concept": "kadane idea",
                "questions": [
                    "Why maintain a running sum?",
                    "Why reset running sum when negative?",
                    "How does this avoid checking all subarrays?"
                ],
                "validator": "kadane_reason"
            },
            {
                "concept": "tracking maximum",
                "questions": [
                    "How do you track global maximum?",
                    "Why compare current sum with max?",
                    "What ensures O(n) complexity?"
                ],
                "validator": "kadane_logic"
            }
        ],
        "solution": """def maxSubArray(nums):
    current = max_global = nums[0]
    for num in nums[1:]:
        current = max(num, current+num)
        max_global = max(max_global, current)
    return max_global"""
    },

    # 8️⃣ Linked List
    "reverse linked list": {
        "description": "Reverse a singly linked list.",
        "steps": [
            {
                "concept": "pointer manipulation",
                "questions": [
                    "Why do we need previous and next pointers?",
                    "How do you reverse links safely?",
                    "What order should pointer updates follow?"
                ],
                "validator": "linked_list_reason"
            },
            {
                "concept": "iteration logic",
                "questions": [
                    "How do you move through the list?",
                    "When does the loop stop?",
                    "What becomes the new head?"
                ],
                "validator": "linked_list_logic"
            }
        ],
        "solution": """def reverseList(head):
    prev = None
    current = head
    while current:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
    return prev"""
    }
}