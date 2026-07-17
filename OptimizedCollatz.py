'''
Collatz Sequence Optimizer

This program calculates Collatz sequence lengths while using memoization
to avoid recalculating paths that have already been explored.

Base approach:
- For every number, independently calculate its entire Collatz sequence.
- Time complexity: O(n * k), where:
    n = amount of starting numbers tested
    k = average Collatz sequence length.

Optimized approach:
- Store previously calculated sequence lengths in a cache.
- Intermediate numbers are also stored, so future calculations can reuse them.
- The search through a range remains O(n), but the repeated Collatz calculations
  are reduced significantly because many paths are retrieved in O(1) from the cache.

'''

storage = {1: 0}  # Base case: Collatz(1) = 0 steps

def Collatz(n):
    global storage
    
    # If it's already in the cache, just return the stored value
    if n in storage:
        return storage[n]
    
    # Calculate the sequence
    original = n
    sequence = 0
    path = []  # Stores all numbers we will need to cache
    
    while n != 1:
        path.append(n)
        sequence += 1
        
        if n % 2 == 0:
            n = n // 2  # Use integer division instead of regular division
        else:
            n = (3 * n) + 1
        
        # If we find a number already stored in the cache, use its result
        if n in storage:
            sequence += storage[n]
            break
    
    # Store the results of every number in the path
    for i, num in enumerate(path):
        storage[num] = sequence - i
    
    return storage[original]

def CollatzChecker(number):
    global longest, longest_number
    
    # Calculate the sequence (it will also update the cache)
    seq_length = Collatz(number)
    
    # Update the record if this sequence is longer
    if seq_length > longest:
        longest = seq_length
        longest_number = number
    
    return seq_length

# Example usage
def find_longest_in_range(start, end):
    global longest, longest_number
    longest_number = 0
    longest = 0
    for i in range(start, end + 1):
        CollatzChecker(i)
    return longest_number, longest
    
def find_longest_in_random_array(array):
    global longest, longest_number
    longest_number = 0
    longest = 0
    for i in array:
        CollatzChecker(i)
    return longest_number, longest

print(f"Longest Sequence in range (1 - 100): {find_longest_in_range(1,100)}")
print(f"Longest Sequence in random array: {find_longest_in_random_array([2, 45, 7, 90, 1234, 123, 1, 89])}")
