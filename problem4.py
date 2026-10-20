'''
def jump_limits(distances):
    return (min(distances), max(distances))


'''
def jump_limits(distances):
    shortest = distances[0]
    longest = distances[0]
    for distance in distances:
        if distance < shortest:
            shortest = distance
        if distance > longest:
            longest = distance
    return(shortest, longest)

    
assert jump_limits([4.2, 3.8, 4.5, 4.0]) == (3.8, 4.5)
assert jump_limits([3.5, 3.5]) == (3.5, 3.5)
assert jump_limits([0.1]) == (0.1, 0.1)
