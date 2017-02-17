lst_ = [0, 0, 0, [[1, 2], 2], [[3, [8]], [4, 5, [6, [7, [9]]]]], 0, 0]


def gen_open_lst(lst):
    for elem in lst:
        if not isinstance(elem, list):
            continue
        else:
            val_index = lst.index(elem)
            lst.remove(elem)
            for i in elem:
                new_index = elem.index(i)
                lst.insert(val_index + new_index, i)
    yield lst



