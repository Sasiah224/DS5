# 🔍 Problem 1: Find Most Frequent Element
# Given a list of integers, return the value that appears most frequently.
# If there's a tie, return any of the most frequent.
#
# Example:
# Input: [1, 3, 2, 3, 4, 1, 3]
# Output: 3

def most_frequent(numbers):
    if not numbers:
        return None

    counts = {}
    most_common = None
    max_count = 0

    for num in numbers:
        counts[num] = counts.get(num, 0) + 1

        if counts[num] > max_count:
            max_count = counts[num]
            most_common = num

    return most_common


"""
Time and Space Analysis for problem 1:
- Best-case: O(n), because every number needs to be checked.
- Worst-case: O(n^2) if severe hash collisions slow down the
  dictionary. With normal dictionary operations, it is O(n).
- Average-case: O(n), because the list is scanned once.
- Space complexity: O(k), where k is the number of different
  numbers. This is O(n) when every number is different.
- Why this approach? A dictionary tracks how often each number
  appears, so I do not have to repeatedly search the list.
- Could it be optimized? This already checks each number once.
  Removing the dictionary could save memory, but repeatedly
  counting numbers would take O(n^2) time.
"""


# 🔍 Problem 2: Remove Duplicates While Preserving Order
# Write a function that returns a list with duplicates removed but preserves order.
#
# Example:
# Input: [4, 5, 4, 6, 5, 7]
# Output: [4, 5, 6, 7]

def remove_duplicates(nums):
    seen = set()
    result = []
    for num in nums:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result


"""
Time and Space Analysis for problem 2:
- Best-case: O(n), because every number must be checked.
- Worst-case: O(n^2) with severe set hash collisions.
  With normal set operations, it is O(n).
- Average-case: O(n), because I go through the list once.
- Space complexity: O(k) for the set and result list, where k
  is the number of unique values. This is at most O(n).
- Why this approach? The set tracks numbers already seen,
  and the result list keeps their original order.
- Could it be optimized? Checking only the result list would
  save the extra set, but could take O(n^2) time.
  Using the set trades extra memory for faster checks.
"""


# 🔍 Problem 3: Return All Pairs That Sum to Target
# Write a function that returns all unique pairs of numbers in the list that sum to a target.
# Order of output does not matter. Assume input list has no duplicates.
#
# Example:
# Input: ([1, 2, 3, 4], target=5)
# Output: [(1, 4), (2, 3)]

def find_pairs(nums, target):
    seen = set()
    pairs = set()

    for num in nums:
        complement = target - num
        if complement in seen:
            pairs.add((min(num, complement), max(num, complement)))
        seen.add(num)

    return list(pairs)

"""
Time and Space Analysis for problem 3:
- Best-case: O(n), because every number must be checked.
- Worst-case: O(n^2) with severe set hash collisions.
  With normal set operations, it is O(n).
- Average-case: O(n), because I go through the list once.
- Space complexity: O(n) for the set and the matching pairs.
- Why this approach? For each number, I check whether the
  number needed to reach the target has already appeared.
  Each pair is added once, when its second number is reached.
- Could it be optimized? Sorting and using two pointers could
  reduce the memory needed for tracking numbers, but sorting
  takes O(n log n) time and may require extra memory.
  The set uses extra memory to avoid needing to sort.
"""


# 🔍 Problem 4: Simulate List Resizing (Amortized Cost)
# Create a function that adds n elements to a list that has a fixed initial capacity.
# When the list reaches capacity, simulate doubling its size by creating a new list
# and copying all values over (simulate this with print statements).
#
# Example:
# add_n_items(6) → should print when resizing happens.

def add_n_items(n):
    if n < 0:
        raise ValueError("n must be nonnegative")

    capacity = 2
    storage = [None] * capacity
    size = 0

    for item in range(n):
        if size == capacity:
            new_capacity = capacity * 2
            print(f"Resizing from {capacity} to {new_capacity}")

            new_storage = [None] * new_capacity

            for index in range(size):
                new_storage[index] = storage[index]

            storage = new_storage
            capacity = new_capacity

        storage[size] = item
        size += 1

    return storage[:size]

"""
Time and Space Analysis for problem 4:
- When do resizes happen? The starting capacity is 2.
  It doubles when another item cannot fit, before adding
  items 3, 5, 9, and so on.
- What is the worst-case for a single append? O(m), where
  m is the current number of items, because they must all
  be copied into the larger list.
- What is the amortized time per append overall? O(1).
  An individual resize is expensive, but all n insertions
  together take O(n) time.
- Best, worst, and average total time: O(n). The resizing
  schedule depends on n. Returning the final slice is also O(n).
- Space complexity: O(n) for storage, temporary space during
  resizing, and the returned list.
- Why does doubling reduce the cost overall? It leaves room
  for more items before another copy is needed. The total
  copying work grows like 2 + 4 + 8 + ..., which stays O(n).
- Could it be optimized? Since n is known, allocating n slots
  at the start would avoid resizing, but would skip the simulation.
- Trade-offs: Doubling uses extra empty space, but avoids
  copying the entire list every time an item is added.
"""


# 🔍 Problem 5: Compute Running Totals
# Write a function that takes a list of numbers and returns a new list
# where each element is the sum of all elements up to that index.
#
# Example:
# Input: [1, 2, 3, 4]
# Output: [1, 3, 6, 10]
# Because: [1, 1+2, 1+2+3, 1+2+3+4]

# Original version: repeatedly adds up earlier numbers.
def running_total_original(nums):
    result = []

    for index in range(len(nums)):
        result.append(sum(nums[:index + 1]))

    return result


# Optimized version: reuses the previous total.
def running_total(nums):
    # Changed from O(n^2) to O(n) time by avoiding repeated sums.
    # Also removes temporary slices, using O(1) extra working
    # space besides the result list.
    result = []
    total = 0

    for num in nums:
        total += num
        result.append(total)

    return result
   

"""
Time and Space Analysis for problem 5:
- Best-case: O(n), because every number is processed once.
- Worst-case: O(n), because the total work grows with the
  number of items.
- Average-case: O(n).
- Space complexity: O(n) for the result list and O(1) extra
  working space for the running total.
- Why this approach? I keep the previous total and add the
  next number instead of adding earlier numbers again.
- Could it be optimized? Changing the input list directly
  could save the output allocation, but the assignment asks
  for a new list. This approach keeps the input unchanged.

Optimization comparison:
- The original version takes O(n^2) time because it slices
  and sums the beginning of the list repeatedly.
- The optimized version takes O(n) time because it adds
  each number to the total once.
- Both versions use O(n) space overall for the output.
  The original also needs up to O(n) temporary slice space.
  The optimized version needs only O(1) working space
  besides the output.
"""

# Tests for Problem 1
assert most_frequent([1, 3, 2, 3, 4, 1, 3]) == 3
assert most_frequent([]) is None
assert most_frequent([5]) == 5
assert most_frequent([2, 2, 2]) == 2
assert most_frequent([1, 1, 2, 2]) in (1, 2)
assert most_frequent([-1, -1, 2]) == -1

print("Problem 1 tests passed!")

# Tests for Problem 2
assert remove_duplicates([4, 5, 4, 6, 5, 7]) == [4, 5, 6, 7]
assert remove_duplicates([]) == []
assert remove_duplicates([5]) == [5]
assert remove_duplicates([2, 2, 2]) == [2]
assert remove_duplicates([3, 1, 2]) == [3, 1, 2]
assert remove_duplicates([-1, 0, -1, 0]) == [-1, 0]

print("Problem 2 tests passed!")

# Tests for Problem 3
assert sorted(find_pairs([1, 2, 3, 4], 5)) == [(1, 4), (2, 3)]
assert find_pairs([], 5) == []
assert find_pairs([3], 6) == []
assert find_pairs([1, 2, 3], 10) == []
assert find_pairs([-3, 0, 3], 0) == [(-3, 3)]
assert find_pairs([0, 5], 5) == [(0, 5)]

print("Problem 3 tests passed!")

# Tests for Problem 4
assert add_n_items(0) == []
assert add_n_items(1) == [0]
assert add_n_items(2) == [0, 1]
assert add_n_items(3) == [0, 1, 2]
assert add_n_items(6) == [0, 1, 2, 3, 4, 5]

print("Problem 4 tests passed!")

# Tests for Problem 5
assert running_total([1, 2, 3, 4]) == [1, 3, 6, 10]
assert running_total([]) == []
assert running_total([5]) == [5]
assert running_total([0, 0, 0]) == [0, 0, 0]
assert running_total([-2, 3, -4]) == [-2, 1, -3]

# Check that both versions give the same results.
for nums in ([], [5], [1, 2, 3, 4], [-2, 3, -4]):
    assert running_total(nums) == running_total_original(nums)

# Check that the original input stays unchanged.
numbers = [1, 2, 3]
assert running_total(numbers) == [1, 3, 6]
assert numbers == [1, 2, 3]

print("Problem 5 tests passed!")