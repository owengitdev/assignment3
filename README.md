# Undo/Redo and Ticketing Line Systems

You've joined the internal tools team at a productivity software company. Two internal teams are requesting features for their systems: one team needs an Undo/Redo manager for a collaborative editor, and the other needs a Help Desk ticketing system to manage customer requests in the order they’re received.

Instead of relying on built-in lists or Python's deque, you're tasked with building two custom data structures, **a Stack and a Queue**, using nodes and pointers. Your program should run in the terminal and allow users to:
- Perform, undo, and redo actions using a custom stack
- Add customers, serve them in order, and monitor a help desk queue
- View the current state of each system interactively

This assignment builds your understanding of how stacks and queues behave under the hood, and how pointer-based logic differs from list-based operations. These skills are foundational for interview preparation and for building tools that require predictable control over the order in which data is accessed and processed.

## File Structure
- `node.py` – Contains the shared `Node` class for both data structures
- `undo_redo.py` – Contains the `Stack` class and Undo/Redo CLI interface
- `help_desk_queue.py` – Contains the `Queue` class and Help Desk CLI interface

## Classes

### `Node` Class
Represents a single element in a linked structure.

**Constructor**

```python
Node(value)
```

**Attributes**
- `value` (Any): The value stored in the node.
- `next` (`Node` or `None`): Pointer to the next node in the structure.

### `Stack` Class
Implements a LIFO stack using linked nodes.

**Constructor**

```python
Stack()
```

**Attributes**
- `top` (`Node` or `None`): Points to the top of the stack.

**Methods**
- `push(value)`: Adds a value to the top of the stack.
- `pop()`: Removes and returns the top value.
- `peek()`: Returns the top value without removing it.
- `print_stack()`: Prints the stack from top to bottom.

### `Queue` Class
Implements a FIFO queue using linked nodes.

**Constructor**

```python
Queue()
```

**Attributes**
- `front` (`Node` or `None`): First item in the queue.
- `rear` (`Node` or `None`): Last item in the queue.

**Methods**
- `enqueue(value)`: Adds a value to the end of the queue.
- `dequeue()`: Removes and returns the front value.
- `peek()`: Returns the front value without removing it.
- `print_queue()`: Prints the queue from front to rear.