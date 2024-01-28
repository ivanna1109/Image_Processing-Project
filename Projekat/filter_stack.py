
def create_stack():
    filter_stack = {}
    return filter_stack


def push_to_stack(filter_stack, newElement):
    exist_element = len([k[0] == newElement[0] for k in filter_stack.values()])
    print(exist_element)
    if (exist_element > 0):
        return None
    current_indeks = len(list(filter_stack.keys()))
    filter_stack[current_indeks] = newElement
    return filter_stack

def exist_element(filter_stack, filter):
    exist_element = len([k[0] == filter for k in filter_stack.values()])
    if (exist_element > 0):
        return [key for key, value in filter_stack.items() if value[0] == filter]
    return -1


def modify_stack(filter_stack, newElement):
    if exist_element(filter_stack, filter) == -1:
        filter_stack = push_to_stack(filter_stack, newElement)
    else:
        for key, value in filter_stack.items():
            if value[0] == filter:
                filter_stack[key] = newElement
                break
    return filter_stack

