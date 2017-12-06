def count_valid_passphrazes(f):
    #file is the system passphraze file.
    return len(filter(is_valid, f))
    

def is_valid(p):
    p = p.strip().split()
    for i in range(len(p)-1):
        for j in xrange(i+1, len(p)):
            if sorted(p[i]) == sorted(p[j]): # the two words are anagrams
                return False
    
    return True

if __name__ == "__main__":
    print count_valid_passphrazes(open("day4_input.txt"))