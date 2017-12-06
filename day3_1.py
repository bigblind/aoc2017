import itertools
import json

def get_distance(n):
    """Returns the manhatten distance from 1 to n in a number spiral
    
    The spiral is laid out as followers
    
    17 16 15 14 13
    18 5  4  3  12
    19 6  1  2  11
    20 7  8  9  10
    21 22 23 24 ...
    
    Manhatten distance is horizontal distance + vertical distance
    """
    if n == 1: # right on the spot
        return 0
    
    for i in itertools.count(1): # count from 1 to infinity (luckily, we break out at some point)
        square_size = 1 + i*2
        if n < square_size ** 2:
            ring_distance = i
            inner_square_size = square_size - 2
            ring_pos = n - (inner_square_size**2) - 1
            side_pos = ring_pos % (square_size - 1)
            half_square = (square_size - 1) / 2
            side_distances = range(half_square - 1, 0, -1) + range(half_square + 1)
            res = ring_distance + side_distances[side_pos]
            print json.dumps(locals(), indent=4)
            return res
        

if __name__ == "__main__":
    print get_distance(int(raw_input("Enter a positive integer: ")))