def dist(p1, p2):
    return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2

def is_square(p1, p2, p3, p4):
    d1 = dist(p1, p2)
    d2 = dist(p1, p3)
    d3 = dist(p1, p4)
    d4 = dist(p2, p3)
    d5 = dist(p2, p4)
    d6 = dist(p3, p4)
    distances = [d1, d2, d3, d4, d5, d6]
    unique_distances = list(set(distances))
    if len(unique_distances) == 2:
        return 1
    else:
        return 0

n = int(input())
for i in range(n):
    p1 = tuple(map(int, input().split()))
    p2 = tuple(map(int, input().split()))
    p3 = tuple(map(int, input().split()))
    p4 = tuple(map(int, input().split()))
    print(is_square(p1, p2, p3, p4))
