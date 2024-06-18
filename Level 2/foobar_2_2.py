def process_parents(max_idx, converter):
    if max_idx < converter:
        return -1
    else:
        node_offset = 0
        subtree_size = max_idx
        result = -1 
        
        while subtree_size>0:    
            subtree_size = subtree_size >> 1
        
            left_node = node_offset + subtree_size
            right_node = left_node + subtree_size
            my_node = right_node + 1
            
            if (left_node == converter) or (right_node == converter):
                result = my_node

            if (converter > left_node):
                node_offset = left_node
   
        return result

def solution(h, q):
    max_idx = 2**h - 1
    return [ process_parents(max_idx, converter) for converter in q ]

if __name__ == '__main__':
    sol = solution(5, [19, 14, 28])
    print(sol)