def get_base(f):
    sup = {}
    weights = {}
    
    for line in f:
        line = line.strip()
        parts = line.split(" -> ")
        name = parts[0].split()[0]
        weights[name] = int(parts[0].split()[1][1:-1])
        
        if len(parts) == 1:
            sup[name] = []
        else:
            supporting = parts[1].split(", ")
            sup[name] = supporting
    
    return tower_weight(sup, weights, "bpvhwhh")
            
def tower_weight(tree, weights, node):
    ow = weights[node]
    
    cw = [tower_weight(tree, weights, c) for c in tree[node]]
    if len(cw) > 1 and not all([c == cw[0] for c in cw[1:]]):
        lcv = min([min(cw), max(cw)], key=cw.count) #least common value
        i = cw.index(lcv)
        mcv = cw[(i+1) % len(cw)]
        d = mcv - lcv
        bc = tree[node][i] # bad child (making this one unbalanced)
        print weights[bc] + d, cw, i, weights[bc]
        cw[i] = weights[bc] + d
    
    return ow + sum(cw)

if __name__ == "__main__":
    print get_base(open("day7_input.txt"))