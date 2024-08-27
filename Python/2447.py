def draw_star(n):
    if n == 1:
        return '*'
    
    star = draw_star(n//3)
    result = []
    for i in range(n):
        if (i // (n//3)) == 1:
            result.append(star[i%(n//3)] + ' ' * (n//3) + star[i%(n//3)])
            continue
        result.append(star[i%(n//3)] * 3)
    return result
    
if __name__ == "__main__":
    stars = draw_star(int(input()))
    for s in stars:
        print(s)
