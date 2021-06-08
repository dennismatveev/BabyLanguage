def evaluate(root_node):
    # base case
    if root_node.l_child is None and root_node.r_child is None:
        #STOP
        return int(root_node.value)

    # recursive call
    else:
        result = 0
        left_result = evaluate(root_node.l_child)
        right_result = evaluate(root_node.r_child)
        if root_node.type == 'PLUS':
            result = left_result + right_result
        elif root_node.type == 'MINUS':
            result = left_result - right_result
        elif root_node.type == 'MULTIPLICATION':
            result = left_result * right_result
        elif root_node.type == 'DIVISION':
            result = left_result / right_result
        return result
