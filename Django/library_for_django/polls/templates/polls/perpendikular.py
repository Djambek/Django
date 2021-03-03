def per(x1,y1, x2, y2):
    k = (y1-y2)/(x1-x2)
    b = y2 - k*x2
    b_answer = abs(y2-y1)/2 + y1
    k_answer = -1/k
    return k_answer, b_answer
def peresechenia(k1, b1, k2, b2, k3, b3):
    x1 = -b1/(k1-k2) + b2/(k1-k2)
    y1 = k1(-b1/(k1-k2) + b2/(k1-k2)) + b1
    x2 = -b2/(k2-k3) + b3/(k2-k3)
    y2 = k2(-b2/(k2-k3) + b3/(k2-k3)) + b2
    x3 = -b3/(k3-k1) + b1/(k3-k1)
    y3 = k3(-b3/(k3-k1) + b1/(k3-k1)) + b3
    if x1 == x2 == x3 and y1 == y2 == y3:
        return x1, y1



y = k1x + b1
y = kx + b
kx -kx1 + b - b1 = 0
x(k-k1) + b - b1 = 0
x + b/(k-k1) - b1/(k-k1) = 0
x = - b/(k-k1) + b1/(k-k1)
y = k(- b/(k-k1) + b1/(k-k1)) + b