def score(x, y):
    radius  = (x**2 + y**2)**0.5
    return (radius <= 1)*5+(radius <= 5) * 4 + (radius <= 10) * 1