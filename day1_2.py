def solve_captcha(s):
    #s is a captcha string
    t = 0
    l = len(s)
    for i in xrange(l):
        if s[i] == s[(i + l / 2) % l]:
            t += int(s[i])
    
    return t

if __name__ == "__main__":
    print solve_captcha(open("day1_input.txt").read().strip())