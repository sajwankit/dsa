# Sliding Window Algorithm

The Sliding Window technique is fundamentally designed to work only with `contiguous subarrays or substrings`.

## Core Concepts

* **Purpose**: The algorithm is primarily used to find the longest or shortest subarray/substring that satisfies a certain condition.
* **Mechanism**: It uses two pointers, `left` and `right`, to define a "window" `[left, right)` over the data.  
  * The `right` pointer expands the window by including new elements
  * The `left` pointer shrinks the window by excluding elements.
* **Efficiency**: This approach reduces the time complexity from a brute-force `$O(N^2)$` to a more efficient linear time `$O(N)$`, because each element is processed only twice (once when `right` passes over it, and once when `left` passes over it).

## Key Questions to ask for applying Sliding Window

> 1.  When should you move `right` to expand the window?
> 2.  When should you stop expanding and start moving `left` to shrink the window?
> 3.  When should you update the final result?

The pseudocode for the template is:

```python
def slidingWindow(s: str):

    "Data structure to track window contents (e.g., a hash map)"
    window = ... 

    left, right = 0, 0
    
    while right < len(s):

        " This step identifies the new character that is about to enter the window. It is not yet officially part of the window [left, right)."
        c = s[right]


        " 1. Expand the window. By incrementing right, we are officially expanding the window's boundary. The new character c is now conceptually inside the window."
        right += 1


        " Update window data...Now that the character c is officially in our new, larger window, we update our tracking data structures (like the window hash map) to reflect its presence."
        ...some_updates(window)

        """Shrink the window when a condition is met.
        Only after the window has been expanded and our data is updated do we check if this new state violates a condition (e.g., contains too many duplicates, is too long, etc.)
        """
        while window_needs_to_shrink:
            d = s[left]
            left += 1
            " Update window data... as we have removed character d from the window"
            ...some_updates(window)
    
    """ Return result """
```

## Why `right++` is Before the Shrinking Loop

> The short answer is: the `right += 1` operation **is the action that actually expands the window**. The shrinking loop (`while window_needs_to_shrink`) needs to evaluate the state of the window *after* it has been expanded.

### Sequence of Events

Here is a step-by-step breakdown of the logic inside the main `while` loop:

1.  **`c = s[right]`**
    * This step **identifies the new character** that is about to enter the window. It is not yet officially part of the window `[left, right)`.

2.  **`right += 1`**
    * **This is the critical step.** By incrementing `right`, we are officially **expanding the window's boundary**. The new character `c` is now conceptually inside the window. For example, if the window was `[0, 3)`, after `right++`, it becomes `[0, 4)`.

3.  **`// Perform a series of updates...`**
    * Now that the character `c` is officially in our new, larger window, we update our tracking data structures (like the `window` hash map) to reflect its presence.

4.  **`while window_needs_to_shrink:`**
    * **Only after** the window has been expanded and our data is updated do we check if this new state violates a condition (e.g., contains too many duplicates, is too long, etc.). The purpose of this inner loop is to react to the change we just made. It asks, "Now that I've added this new character, do I need to fix the left side of the window?"


### Why Use the `[left, right)` Interval in Sliding Window?

The half-open interval `[left, right)` is a standard convention for the sliding window algorithm because it leads to cleaner, more intuitive, and less error-prone code.

* **Clean Initialization for an Empty Window:** 
  * With `[left, right)`: The algorithm starts with left = 0 and right = 0. The interval [0, 0) correctly represents an empty window with a size of 0 - 0 = 0. This is a very natural and logical starting point.

  * With [left, right]: To represent an empty window, you'd have to use an awkward initialization like left = 0 and right = -1. This is less intuitive and can complicate the initial loop conditions.
  
* **Cleaner Loop Logic:** The code for expanding the window and the loop's termination condition (`while right < len(s)`) are simpler.
* **Programming Idiom Consistency:** It aligns with conventions in many languages, like Python's slicing (`s[start:end]`) and C++ iterators, making the code more readable.  