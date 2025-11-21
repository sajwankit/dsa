# Binary Search

## 1\. The Core Framework: "Closed Interval"

The author recommends consistently using a search interval of $[left, right]$ (closed at both ends). This simplifies the logic across all variations.

  * **Initialization:** `left = 0`, `right = len(nums) - 1`
  * **Loop Condition:** `while left <= right`
      * **Why:** The search terminates only when the interval is empty ($left > right$). If you use `<`, you miss the element where $left == right$.
  * **Mid Calculation:** `mid = left + (right - left) // 2`
      * **Why:** Prevents integer overflow compared to `(left + right) / 2`.

-----

## 2\. The Three Common Scenarios

The only logic that changes between scenarios is how you handle the `nums[mid] == target` condition and what you return.

### A. Basic Search (Find a Number)

Used when you just need to know if a number exists or return its index.

  * **Logic:** If `nums[mid] == target`, return `mid` immediately.
  * **Interval Update:** Since the interval is closed, always exclude `mid` from the next search:
      * If `nums[mid] < target`: `left = mid + 1`
      * If `nums[mid] > target`: `right = mid - 1`

### B. Find Left Boundary (First Occurrence)

Used when `target` has duplicates and you want the first one (or the insertion point).

  * **Logic:** If `nums[mid] == target`, **do not return**. Instead, tighten the *right* border to search the left side: `right = mid - 1`.
  * **Return:** Check `left`.
      * If `left` is out of bounds or `nums[left] != target`, return -1.
      * Otherwise, return `left`.

### C. Find Right Boundary (Last Occurrence)

Used when `target` has duplicates and you want the last one.

  * **Logic:** If `nums[mid] == target`, **do not return**. Instead, tighten the *left* border to search the right side: `left = mid + 1`.
  * **Return:** Check `right`.
      * If `right` is out of bounds or `nums[right] != target`, return -1.
      * Otherwise, return `right`.

-----

## 3\. Unified Code Template for Binary Search (Python)

Here is the consolidated template. Notice that the `...` sections are the only parts that change based on the goal.

```python
def binary_search_unified(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        elif nums[mid] == target:
            # VARIATION POINT:
            # 1. Basic: return mid
            # 2. Left Bound: right = mid - 1 (Lock Right)
            # 3. Right Bound: left = mid + 1 (Lock Left)
            pass 
            
    # RETURN POINT:
    # 1. Basic: return -1
    # 2. Left Bound: Check if left is within bounds & equals target
    # 3. Right Bound: Check if right is within bounds & equals target
    return -1
```

### 4\. Key Nuances & "Gotchas"

  * **Why `left = mid + 1`?** Because the search interval is $[left, right]$, `mid` has already been tested. You must exclude it to ensure the interval shrinks, avoiding infinite loops.
  * **Missing Targets:**
      * **Left Boundary Search:** If `target` is missing, `left` represents the index of the **first element greater than** `target`.
      * **Right Boundary Search:** If `target` is missing, `right` represents the index of the **last element smaller than** `target`.
  * **Pre-Condition:** The array **must be sorted** for this logic to work.

-----

### Summary Table

| Scenario | Loop Condition | If `nums[mid] == target` | Final Return Check |
| :--- | :--- | :--- | :--- |
| **Basic** | `left <= right` | `return mid` | Return -1 |
| **Left Bound** | `left <= right` | `right = mid - 1` | Check `nums[left]` |
| **Right Bound** | `left <= right` | `left = mid + 1` | Check `nums[right]` |

-----

### ⚠️ Logic: Why Pointers Can Go Out of Bounds

In the binary search loop, we aggressively update pointers using `mid + 1` or `mid - 1` to narrow the search space. Because of this increment/decrement logic, pointers can easily overshoot the array limits if the **target does not exist**.

1.  **`left` goes Out of Bounds (\> len(nums))**

      * **Cause:** If the `target` is **larger** than all elements, the condition `nums[mid] < target` is always true.
      * **Effect:** We keep executing `left = mid + 1`. Eventually, `left` exceeds the last index and becomes `len(nums)`.

2.  **`right` goes Out of Bounds (\< 0)**

      * **Cause:** If the `target` is **smaller** than all elements, the condition `nums[mid] > target` is always true.
      * **Effect:** We keep executing `right = mid - 1`. Eventually, `right` drops below 0 and becomes `-1`.

**Conclusion:**
Since the loop terminates when `left > right`, one of these pointers might be invalid. Therefore, you **must** have a post-processing check to ensure the index is valid before accessing the array.

**The Sanity Check:**

```python
# Prevents "IndexError: list index out of range"
if left < len(nums) and nums[left] == target:
    return left
return -1
```

OR

```python
# Prevents "IndexError: list index out of range"
if right >= 0 and nums[right] == target:
    return right
return -1
```

-----
