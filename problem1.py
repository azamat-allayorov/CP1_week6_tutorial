def count_size(sizes, wanted):
    count = 0
    for size in sizes:
        if size == wanted:
            count += 1

    return count


            #version2
'''
def count_size(sizes, wanted):
    return sizes.count(wanted)
'''