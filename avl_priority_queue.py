class Node:
    """
    A class representing a single node in the AVL tree.
    """
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.left = None
        self.right = None
        self.height = 1


class AVLPriorityQueue:
    """
    A priority queue implementation using an AVL tree.
    """
    def __init__(self):
        self.root = None

    @staticmethod
    def get_height(node):
        """
        Gets the height of a given node.

        :param node: The node whose height is to be determined.
        :return: height
        """
        if node:
            height = node.height
        else:
            height = 0
        return height

    def get_balanced(self, node):
        """
        Calculates the balance factor of a given node.

        :param node: The node to calculate the balance factor for.
        :return: balanced_rate
        """
        if node:
            balanced_rate = self.get_height(node.left) - self.get_height(node.right)
        else:
            balanced_rate = 0
        return balanced_rate

    def rotate_left(self, x):
        """
        Performs a left rotation on the given node to rebalance the AVL tree.

        :param x: The root of the unbalanced subtree.
        :return: y
        """
        y = x.right
        inner_subtree = y.left
        y.left = x
        x.right = inner_subtree
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def rotate_right(self,y):
        """
        Performs a right rotation on the given node to rebalance the AVL tree.

        :param y: The root of the unbalanced subtree.
        :return: x
        """
        # y - корінь дерева; x - ліве піддерево(розбалансоване)
        x = y.left
        inner_subtree = x.right
        x.right = y
        y.left = inner_subtree
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        return x

    def insert(self, value, priority, node="default"):
        """
        Inserts a new element with the specified value and priority into the queue.

        :param value: The data to be inserted.
        :param priority: The priority of the inserted value.
        :param node: The current node during recursion, or "default" for the initial
                    public call.
        :return: result_node
        """
        result_node = node
        if node == "default":
            self.root = self.insert(value, priority, self.root)
            result_node = self.root
        elif not node:
            result_node = Node(value, priority)
        else:
            if priority <= node.priority:
                node.left = self.insert(value, priority, node.left)
            else:
                node.right = self.insert(value, priority, node.right)

            if node.left:
                left_h = node.left.height
            else:
                left_h = 0
            if node.right:
                right_h = node.right.height
            else:
                right_h = 0
            node.height = 1 + max(left_h, right_h)
            balanced = left_h - right_h

            if balanced > 1 and priority < node.left.priority:
                result_node = self.rotate_right(node)
            elif balanced < -1 and priority >= node.right.priority:
                result_node = self.rotate_left(node)
            elif balanced > 1 and priority >= node.left.priority:
                node.left = self.rotate_left(node.left)
                result_node = self.rotate_right(node)
            elif balanced < -1 and priority < node.right.priority:
                node.right = self.rotate_right(node.right)
                result_node = self.rotate_left(node)
            else:
                result_node = node
        return result_node


    def pop(self, value=None, priority=None, node="default"):
        """
        Removes and returns the element with the highest priority.

        :param value: The value of the node to remove.
        :param priority: The priority of the node to remove.
        :param node: The current node during recursion, or "default" for the initial
                    public call.
        :return: result
        """
        result = None
        if node == "default":
            if self.root:
                current = self.root
                while current.right:
                    current = current.right
                result = (current.value, current.priority)
                self.root = self.pop(current.value, current.priority, self.root)
        elif node:
            if priority < node.priority:
                node.left = self.pop(value, priority, node.left)
                result = node
            elif priority > node.priority:
                node.right = self.pop(value, priority, node.right)
                result = node
            else:
                if node.value != value:
                    node.right = self.pop(value, priority, node.right)
                    result = node
                else:
                    if not node.left:
                        result = node.right
                    elif not node.right:
                        result = node.left
                    else:
                        temporary = node.right
                        while temporary.left:
                            temporary = temporary.left
                        node.value = temporary.value
                        node.priority = temporary.priority
                        node.right = self.pop(temporary.value, temporary.priority, node.right)
                        result = node

                #Rebalancing after deletion
                if result and isinstance(result, Node):
                    left_h = result.left.height if result.left else 0
                    right_h = result.right.height if result.right else 0
                    result.height = 1 + max(left_h, right_h)
                    balanced = left_h - right_h

                    if balanced > 1:
                        left_left_h = result.left.left.height if result.left and result.left.left else 0
                        left_right_h = result.left.right.height if result.left and result.left.right else 0
                        if (left_left_h - left_right_h) >= 0:
                            result = self.rotate_right(result)
                        else:
                            result.left = self.rotate_left(result.left)
                            result = self.rotate_right(result)
                    elif balanced < -1:
                        right_left_h = result.right.left.height if result.right and result.right.left else 0
                        right_right_h = result.right.right.height if result.right and result.right.right else 0
                        if (right_left_h - right_right_h) <= 0:
                            result = self.rotate_left(result)
                        else:
                            result.right = self.rotate_right(result.right)
                            result = self.rotate_left(result)

        return result


    def peek(self):
        """
        Retrieves the element with the highest priority without removing it.
        :return: result
        """
        result = None
        if self.root:
            current = self.root
            while current.right:
                current = current.right
            result = (current.value, current.priority)
        return result


def main():
    """
    Retrieves the element with the highest priority without removing it.
    """
    priority_queue = AVLPriorityQueue()
    elements_for_queue = [
        (101, 1),
        (1001, 10),
        (505, 5),
        (202, 2),
        (404, 4)
    ]

    print("\n insert:")
    for value, priority in elements_for_queue:
        print(f"Element {value} with priority {priority} was added")
        priority_queue.insert(value, priority)

    print("\n peek:")
    top_element = priority_queue.peek()
    if top_element:
        print(f"Top element is {top_element[0]}; it`s priority is {top_element[1]}")

    print("\n pop:")
    while True:
        element = priority_queue.pop()
        if element is None:
            break
        print(f"Element {element[0]} with priority {element[1]}")
    print("The queue is empty")


if __name__ == "__main__":
    main()