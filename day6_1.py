def count_cycles(m):
    seen = [list(m)]
    l = len(m)
    cycles = 0
    
    while True:
        cycles += 1
        mmax = max(m)
        maxi = m.index(mmax)
        m[maxi] = 0
        for i in xrange(1, mmax+1):
            m[(maxi + i) % l] += 1
        
        if m in seen:
            return cycles
        
        seen.append(list(m))
        
    

if __name__ == "__main__":
    print count_cycles([int(x) for x in open("day6_input.txt").read().split()])