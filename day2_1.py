def make_checksum(s):
    #s is a spreadsheet represented as a string
    s = [[int(x) for x in line.split()] for line in s.split("\n")]
    t = 0
    l = len(s)
    for i in xrange(l):
        lo, hi = min(s[i]), max(s[i])
        t += hi - lo
    
    return t

if __name__ == "__main__":
    print make_checksum(open("day2_input.txt").read().strip())