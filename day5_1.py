def count_steps(f):
    instrs = [int(l) for l in f]
    
    pos = 0
    steps = 0
    
    while 0 <= pos < len(instrs):
        ins = instrs[pos]
        instrs[pos] += 1
        pos += ins
        steps += 1
    
    return steps

if __name__ == "__main__":
    print count_steps(open("day5_input.txt"))