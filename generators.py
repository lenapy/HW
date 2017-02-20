lst_ = [0, 0, 0, [[1, 2], 2], [[3, [8]], [4, 5, [6, [7, [9]]]]], 0, 0]


def gen_open_lst(lst):
    for elem in lst:
        if not isinstance(elem, list):
            yield elem
        else:
            g = gen_open_lst(elem)
            for i in g:
                yield i

g = gen_open_lst(lst_)
print([i for i in g])







