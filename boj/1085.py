x, y, w, h = map(int, input().split())

u = h - y
d = y
l = x
r = w - x
print(min(u, d, l, r))