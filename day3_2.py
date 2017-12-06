import itertools
import math


class icomplex(complex):
    """Little wrapper around the complex type that returns the imaginary and real portions as integers."""
    
    @property
    def real(self):
        return int(super(icomplex, self).real)
    
    @property
    def imag(self):
        return int(super(icomplex, self).imag)
    
    def __add__(self, other):
        r = super(icomplex, self).__add__(other)
        return icomplex(r.real, r.imag)
    
    def __mul__(self, other):
        r = super(icomplex, self).__mul__(other)
        return icomplex(r.real, r.imag)
    
    


def get_neighbour_suares(n):
    """Returns the answer for Advent Of Code 2017's second problem for day 3
    
    It concerns a number spiral like this
    
    17 16 15 14 13
    18 5  4  3  12
    19 6  1  2  11
    20 7  8  9  10
    21 22 23 24 ...
    
    If we were to clear the grid, and fill up the cells starting at 1 in the following way way, what would be the first value written greater than n?
    
    square 1 has value 1.
    For each square, enter the sum of all the values that have already been filled in in its neighbours (including diagonal).
    
    A note about this solution: I first misread the problem as requiring the nth value, because I missed a line in the problem statement. I quickly modified my solution to find the first value greater than n,
    but it's still based on the original code. I could probably tweak the code to be better suited to the actual problem, and might do so in the future, though PRs are welcome as well.
    """
    if n == 1: # right on the spot
        return 1
    
    grid = []
    s = int(math.ceil(math.sqrt(n)))
    
    if s % 2 == 0:
        s += 1
    
    for i in xrange(s):
        grid.append([0] * s)
    
    grid[(s - 1) / 2][(s - 1) / 2] = 1
    
    # We represent co-ordinates as complex numbers, because it allows us to do a couple of neat tricks
    # Complex numbers consist of a *real* and an *imaginary* part. We see these as our x and y co-ordinates respectively.
    # If you add 2 complex numbers together, you create a ew number with the sum of the two real parts of the others, and the sum of the imaginary parts, just like vector addition.
    # If you multiply a complex number with I (I is a complex number with real part 0 and imaginary part 1), you're basically rotating it by 90 degrees around the origin counterclockwise.
    I = icomplex(0, 1)
    pos = icomplex((s-1) / 2 + 1, (s-1) / 2) # one cell to the right of center.
    print (pos.real, pos.imag)
    dir = icomplex(1, 0)
    neighdirs = list(itertools.starmap(complex, [(1, 1), (1, 0), (0, 1), (-1, 0), (0, -1), (-1, -1), (1, -1), (-1, 1)]))
    
    for i in xrange(2, n+1):
        t = 0
        for nd in neighdirs:
            neigh = pos + nd
            if neigh.real < 0 or neigh.real >= s or neigh.imag < 0 or neigh.imag >= s:
                continue
            t += grid[neigh.real][neigh.imag]
        
        if t > n:
            return t
        
        grid[pos.real][pos.imag] = t
        
        left = pos + (dir * I)
        if grid[left.real][left.imag] == 0:
            dir *= I
        
        if i < n:
            pos = pos + dir
    
    return grid[pos.real][pos.imag]

if __name__ == "__main__":
    print get_neighbour_suares(int(raw_input("Enter a positive integer: ")))