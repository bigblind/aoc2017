def run_instructions(f):
    regs = {}
    for line in f:
        line = line.strip()
        name, direction, value, _, left, op, right = line.split()
        value = int(value)
        right = int(right)
        if not check_condition(left, op, right, regs):
            print "condition not true:", left, op, right
            continue
        set_register(name, direction, value, regs)
        
        print regs
    
    return max(regs.values())


def check_condition(left, op, right, regs):
    ops = {
        "==": lambda x, y: x == y,
        "!=": lambda x, y: x != y,
        ">=": lambda x, y: x >= y,
        "<=": lambda x, y: x <= y,
        ">": lambda x, y: x > y,
        "<": lambda x, y: x < y
    }
    
    v = ops[op](regs.get(left, 0), right)
    print left, op, right, "=", v
    return v


def set_register(name, direction, value, regs):
    if direction == "dec":
        value = -value
    
    if name not in regs:
        regs[name] = value
    else:
        regs[name] += value

if __name__ == "__main__":
    print run_instructions(open("day8_input.txt"))