import math

class Triangle:
    def __init__(self, a, b, c): self.a, self.b, self.c = a, b, c
    def p(self): return self.a + self.b + self.c
    def s(self):
        m = self.p() / 2
        return math.sqrt(m * (m - self.a) * (m - self.b) * (m - self.c))

class Rectangle:
    def __init__(self, a, b): self.a, self.b = a, b
    def p(self): return 2 * (self.a + self.b)
    def s(self): return self.a * self.b

class Trapeze:
    def __init__(self, a, b, c, d): self.a, self.b, self.c, self.d = a, b, c, d
    def p(self): return self.a + self.b + self.c + self.d
    def s(self):
        h = math.sqrt(self.c**2 - (((self.b - self.a)**2 + self.c**2 - self.d**2) / (2 * (self.b - self.a)))**2)
        return ((self.a + self.b) / 2) * h

class Parallelogram:
    def __init__(self, a, b, h): self.a, self.b, self.h = a, b, h
    def p(self): return 2 * (self.a + self.b)
    def s(self): return self.a * self.h

class Circle:
    def __init__(self, r): self.r = r
    def p(self): return 2 * math.pi * self.r
    def s(self): return math.pi * self.r**2

figs = []
try:
    with open('figures.txt', 'r') as f:
        for line in f:
            p = line.split()
            if not p: continue
            t, v = p[0], [float(x) for x in p[1:]]
            if t == 'Triangle': figs.append(Triangle(*v))
            elif t == 'Rectangle': figs.append(Rectangle(*v))
            elif t == 'Trapeze': figs.append(Trapeze(*v))
            elif t == 'Parallelogram': figs.append(Parallelogram(*v))
            elif t == 'Circle': figs.append(Circle(*v))
except FileNotFoundError:
    print("Error: figures.txt not found")

if figs:
    max_s = max(figs, key=lambda x: x.s())
    max_p = max(figs, key=lambda x: x.p())
    
    print(f"RESULTS:")
    print(f"Max Area: {max_s.__class__.__name__} (S = {max_s.s():.2f})")
    print(f"Max Perimeter: {max_p.__class__.__name__} (P = {max_p.p():.2f})")