import cmath
from matplotlib import pyplot as plt

pi = cmath.pi

def sin(x, f):
    return cmath.sin(2 * pi * x * f)

def sound(x):
    return sin(x, 2) + sin(x, 7) + sin(x, 8) + sin(x, 16)

def FT(func, N, f, range_):
    sum = 0
    for t in range(range_[0]*N, range_[1]*N):
        t /= N
        sum += func(t) * cmath.exp(2 * pi * 1j * f * t)

    sum = abs(sum)
    return sum
x = []
y = []
for f in range(0, 200):
    f /= 10
    x.append(f)
    y.append(FT(sound, 100, f, (0, 10)))

ax = []
ay = []
for i in range(1000):
    i /= 1000
    ax.append(i)
    ay.append(sound(i))

plt.plot(x, y)
#plt.plot(ax, ay)
plt.xlabel('Frequency')
plt.ylabel('strength')
plt.title('Fourier transform')
plt.show()