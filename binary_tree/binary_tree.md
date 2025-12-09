# Mastering Binary Trees: The Unified Theory of Traversals

### 1\. The Core Philosophy

Binary trees are the key to mastering recursion. Many advanced algorithms are just binary tree traversals in disguise:

  * **QuickSort:** A **Preorder** traversal. (Partition the array first, *then* recursively sort the sub-arrays).
  * **MergeSort:** A **Postorder** traversal. (Recursively sort sub-arrays first, *then* merge the results).

-----

### 2\. The Three "Time Moments" of Traversal

Traversals are not just sorted lists of nodes; they represent **execution timings**.

  * **Preorder Position:** Code runs **before** entering children. (Good for passing data *down*).
  * **Inorder Position:** Code runs between visiting the Left and Right child. (Crucial for BSTs).
  * **Postorder Position:** Code runs **after** returning from children. (Crucial for passing data *up*).

**Visualizing the Code Execution:**

```python
def traverse(root):
    if not root: return
    
    # [Preorder Position]: Code here runs when you ENTER the node.
    # Can access data passed from parent.
    
    traverse(root.left)
    
    # [Inorder Position]: Code here runs after Left child, before Right child.
    
    traverse(root.right)
    
    # [Postorder Position]: Code here runs when you LEAVE the node.
    # Can access data returned from both subtrees. Most powerful position.
```

-----

### 3\. The Two Solution Frameworks

When solving a binary tree problem, choose one of these two mental models:

#### A. The Traversal Approach (Walk the Tree)

  * **Logic:** Can I calculate the answer by walking the tree once and updating a global variable?
  * **Mechanism:** Use a `traverse()` function (usually `void` return) + **External Variables**.

**Example: Max Depth (Traversal Style)**

```python
class Solution:
    def __init__(self):
        self.res = 0    # External variable
        self.depth = 0  # Track current depth

    def maxDepth(self, root):
        self.traverse(root)
        return self.res

    def traverse(self, root):
        if not root: return
        
        # Preorder: Enter node, increase depth
        self.depth += 1
        
        # Update result if it's a leaf
        if not root.left and not root.right:
            self.res = max(self.res, self.depth)
            
        self.traverse(root.left)
        self.traverse(root.right)
        
        # Postorder: Leave node, decrease depth (Backtrack)
        self.depth -= 1
```

#### B. The Decomposition Approach (Divide & Conquer)

  * **Logic:** Can the answer for the current node be derived entirely from the answers of its subtrees?
  * **Mechanism:** Use a recursive function with a **Return Value**.
  * **Equation:** `Result(Root) = Combine(Result(Left), Result(Right))`

**Example: Max Depth (Decomposition Style)**

```python
class Solution:
    def maxDepth(self, root):
        if not root: return 0
        
        # 1. Ask subtrees for their depth
        leftMax = self.maxDepth(root.left)
        rightMax = self.maxDepth(root.right)
        
        # 2. Decomposition logic (Postorder position)
        # My depth = 1 + max depth of children
        return 1 + max(leftMax, rightMax)
```

-----

### 4\. Special Case: The Necessity of Postorder

If a problem requires knowing the status of the entire subtree (e.g., "what is the diameter?"), you **must** use the Postorder position (Decomposition).

**Case Study: Diameter of Binary Tree**

  * **Naive (Bad):** Traverse every node, then call `maxDepth` for every node. $O(N^2)$.
  * **Optimized (Good):** Calculate diameter *inside* the Postorder phase of the `maxDepth` function.

<!-- end list -->

```python
class Solution:
    def __init__(self):
        self.maxDiameter = 0

    def diameterOfBinaryTree(self, root):
        self.maxDepth(root)
        return self.maxDiameter

    def maxDepth(self, root):
        if not root: return 0
        
        leftMax = self.maxDepth(root.left)
        rightMax = self.maxDepth(root.right)
        
        # [Postorder Code]: We now know the depth of both sides.
        # Calculate diameter passing through THIS root.
        myDiameter = leftMax + rightMax
        self.maxDiameter = max(self.maxDiameter, myDiameter)
        
        # Return height to parent (standard maxDepth logic)
        return 1 + max(leftMax, rightMax)
```

-----

### 5\. Unified Theory: DP vs Backtracking vs DFS

The article argues these are all variations of tree traversal, distinguished by their "Focus Point":

| Algorithm | Focus Point | Logic Placement |
| :--- | :--- | :--- |
| **DFS** | **The Node** | Logic executes on the node itself (e.g., `visited[node]=true`). Logic is *outside* the loop. |
| **Backtracking** | **The Branch** | Focuses on the edge/choice between nodes. Logic sits *inside* the loop (Make choice -\> Recurse -\> Undo choice). |
| **Dynamic Programming** | **The Subtree** | Focuses on the result returned by the subtree. Decomposes the problem (Postorder). |

**DFS vs Backtracking Code Structure:**

```python
# DFS: Focus on Node
def dfs(root):
    if not root: return
    # Make choice (Enter node)
    print(f"Enter {root.val}")
    for child in root.children:
        dfs(child)
    # Undo choice (Leave node)
    print(f"Leave {root.val}")

# Backtracking: Focus on Branch (Choice)
def backtrack(root):
    if not root: return
    for child in root.children:
        # Make choice (Edge to child)
        print(f"Traveling edge {root.val}->{child.val}")
        backtrack(child)
        # Undo choice (Return from edge)
        print(f"Returning edge {child.val}->{root.val}")
```

### 6\. Level Order Traversal (BFS)

Iterative approach using a **Queue**. Used for shortest paths.

[Image of binary tree level order traversal]

```python
def levelOrder(root):
    if not root: return []
    q = collections.deque([root])
    depth = 0
    
    while q:
        sz = len(q)
        # Iterate over all nodes at current level
        for i in range(sz):
            cur = q.popleft()
            # Add children for NEXT level
            if cur.left: q.append(cur.left)
            if cur.right: q.append(cur.right)
        depth += 1
```

### Summary Checklist for Problem Solving

1.  **Traverse or Decompose?** (Global variable vs Return value?)
2.  **Which Position?** (Preorder for passing data down, Postorder for passing data up).
3.  **Subtree Dependency?** If `root` depends on `left` and `right` results, you need **Postorder**.

-----

## The key detail: **the scope of variables available to you.**

### 1\. DFS = Focus on the "Node" (The Destination)

In the DFS code, the logic (`print`) happens **outside the loop**.

  * **Context:** When you are inside `dfs(root)`, you are "standing" on that node. You mostly care about **where you are right now**.
  * **Data:** You typically operate on `root` alone (e.g., `visited[root] = True`). You don't necessarily care which specific branch got you there, just that you arrived.
  * **Analogy:** Think of a courier delivering packages. The "activity" is dropping off the package at the **House** (Node).

<!-- end list -->

```python
def dfs(root):
    if not root: return

    # OPERATE ON THE NODE ITSELF
    # We are "at" the node. We don't care which child we go to next yet.
    print(f"I have arrived at {root.val}") 
    
    for child in root.children:
        dfs(child)
```

### 2\. Backtracking = Focus on the "Branch" (The Journey)

In the Backtracking code, the logic (`print`) happens **inside the loop**.

  * **Context:** You are standing at a crossroads (Parent), looking at a path (Edge) leading to a destination (Child). You care about **the decision/choice** you are about to make.
  * **Data:** You have access to both `root` (start of edge) and `child` (end of edge). This allows you to describe the relationship or the "move" between them.
  * **Analogy:** Think of a person testing a maze. The "activity" is drawing a chalk line on the **Path** (Edge) they are walking. If they hit a dead end, they walk back and erase that chalk line (Undo choice).

<!-- end list -->

```python
def backtrack(root):
    if not root: return
    
    for child in root.children:
        # OPERATE ON THE EDGE (CHOICE)
        # We are defining the relationship between Parent -> Child
        print(f"I am choosing to go from {root.val} to {child.val}")
        
        backtrack(child)
        
        # UNDO THE CHOICE
        print(f"I am retreating from {child.val} back to {root.val}")
```

### Why does this matter?

The "Backtracking" style gives you finer control over the **state changes**.

  * **In DFS:** You mark a node as visited. That's a static property of the node.
  * **In Backtracking:** You add an item to a `current_path` list. That is a property of the *sequence of choices* (edges) you made.

**Summary Table:**

| Feature | DFS (Node Focus) | Backtracking (Branch Focus) |
| :--- | :--- | :--- |
| **Logic Location** | **Outside** the `for` loop | **Inside** the `for` loop |
| **Data Access** | Mostly `root` (current node) | `root` (parent) AND `child` (next step) |
| **Concept** | "I am processing this State." | "I am making (and un-making) a Choice." |