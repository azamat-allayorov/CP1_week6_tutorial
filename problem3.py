'''
def total_download_size(sizes):
    total = 0
    for size in sizes:
        total += size
    return total 

'''

def total_download_size(sizes):
    return sum(sizes)

assert total_download_size([100, 200, 200]) == 500
assert total_download_size([]) == 0
assert total_download_size([80]) == 80
