def get_base(f):
    sup = {}
    supported = []
    for line in f:
        line = line.strip()
        parts = line.split(" -> ")
        name = parts[0].split()[0]
        if len(parts) == 1:
            sup[name] = []
        else:
            supporting = parts[1].split(", ")
            sup[name] = supporting
            supported += supporting
    
    for name in sup:
        if name not in supported:
            return name
            
        

if __name__ == "__main__":
    print get_base(open("day7_input.txt"))