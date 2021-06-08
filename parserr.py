class treeNode:
    def __init__(self, type, value, precedence):
        self.type = type
        self.value = value
        self.precedence = precedence

    parent = None
    l_child = None
    r_child = None


def getPrecedence(type):
    precedence = 0
    if type == "PLUS" or type == "MINUS":
        precedence = 1
    elif type == "MULTIPLICATION" or type == "DIVISION":
        precedence = 2
    elif type == "LPAREN":
        precedence = 4
    elif type == "RPAREN":
        precedence = 4
    return precedence


def createTreeNodeList(tok_seq):
    new_toq_seq = []
    tree_node_list = []
    num_paren = 0
    for token in tok_seq:
        if token.type == "LPAREN":
            num_paren += 1
        elif token.type == "RPAREN":
            num_paren -= 1
        else:
            new_node = treeNode(token.type, token.value, getPrecedence(token.type) + 4 * num_paren)
            tree_node_list.append(new_node)
    return tree_node_list


def findRoot(tree_node_list):
    root_node = None
    for node in tree_node_list:
        if node.parent is None and node.type != "DUMMY":
            root_node = node
            break
    return root_node


def parsing(tree_node_list):
    dummy_node = treeNode("DUMMY", "", 0)
    tree_node_list.insert(0, dummy_node)
    tree_node_list.append(dummy_node)
    for index in range(len(tree_node_list)):
        node = tree_node_list[index]
        if node.type == "NUMBER":
            l_op = tree_node_list[index - 1]
            r_op = tree_node_list[index + 1]
            if l_op.type == "LPAREN":
                l_op = tree_node_list[index - 2]
            elif r_op.type == "RPAREN":
                r_op = tree_node_list[index + 2]
            if r_op.precedence > l_op.precedence:
                # right
                r_op.l_child = node
                node.parent = r_op
                if l_op.type != "DUMMY":
                    l_op.r_child = r_op
                    r_op.parent = l_op
            elif r_op.type == "DUMMY" and l_op.type == "DUMMY":
                break

            else:
                # left
                l_op.r_child = node
                node.parent = l_op
                if r_op.type != "DUMMY":
                    while l_op.parent:
                        if l_op.parent.precedence < r_op.precedence:
                            break
                        l_op = l_op.parent
                    if l_op.parent:
                        l_op.parent.r_child = r_op
                        r_op.parent = l_op.parent
                    r_op.l_child = l_op
                    l_op.parent = r_op


def parse(tok_seq):
    root_node = None
    tree_node_list = createTreeNodeList(tok_seq)
    parsing(tree_node_list)
    root_node = findRoot(tree_node_list)
    return root_node


def printTree(root_node):
    if root_node.l_child is None and root_node.r_child is None:
        # operand
        print(root_node.value, end="")
    else:
        # operator
        print("(", end="")
        printTree(root_node.l_child)
        print(root_node.value, end="")
        printTree(root_node.r_child)
        print(")", end="")
