def make_checksum(s):
    #s is a spreadsheet represented as a string
    s = [[int(x) for x in line.split()] for line in s.split("\n")]
    t = 0
    for line in s:
        for i in xrange(1, len(line)):
            for j in xrange(i):
                if line[i] % line[j] == 0:
                    r = line[i] / line[j]
                    break
                if line[j] % line[i] == 0:
                    r = line[j] / line[i]
                    break
        t += r
    
    return t

if __name__ == "__main__":
    print make_checksum(open("day2_input.txt").read().strip())