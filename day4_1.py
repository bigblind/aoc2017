def count_valid_passphrazes(f):
    #file is the system passphraze file.
    is_valid = lambda p: len(p.strip().split()) == len(set(p.strip().split()))
    return len(filter(is_valid, f))
    

if __name__ == "__main__":
    print count_valid_passphrazes(open("day4_input.txt"))