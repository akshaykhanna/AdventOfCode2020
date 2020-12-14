import math

print('day13')


# def find(n, s):
#     a = s.split(",");
#     print("a: ", a)
#     md = 0
#     bus = 0
#     flag = False
#     for e in a:
#         if e == 'x':
#             continue
#         ne = int(e)
#         # print("ne:", ne)
#         f = math.floor(n / ne)
#         # print("f:", f)
#         nf = n / ne
#         # print("nf:", nf)
#         if nf > f:
#             f += 1
#         bt = ne * f
#         diff = bt - n
#         if not flag or diff < md:
#             md = diff
#             bus = ne
#             flag = True
#             print('bus:', bus, ' md:', md)
#     return bus * md

def find(n, s):
    buses = {}
    bid = 0
    a = s.split(",");
    for b in a:
        if b != 'x':
            buses[bid] = int(b)
        bid += 1

    def modInv(b, m):
        g, x, y = gcd(b, m)
        if g != 1:
            return
        return x % m

    def gcd(a, b):
        if a == 0:
            return b, 0, 1
        g, x1, y1 = gcd(b % a, a)
        return g, y1 - (b/a) * x1, x1

    print('buses:', buses)


n = 939
s = "7,13,x,x,59,x,31,19";
nn = 1008169
sn = "29,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,41,x,x,x,37,x,x,x,x,x,653,x,x,x,x,x,x,x,x,x,x,x,x,13,x,x,x,17,x,x,x,x,x,23,x,x,x,x,x,x,x,823,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,19"
print(find(n, s));
