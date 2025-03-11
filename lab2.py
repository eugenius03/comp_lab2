import matplotlib.pyplot as plt

def island(x1, y1, x2, y2, n, ratio=0.25):
    if n == 0:
        plt.plot([x1, x2], [y1, y2])
    else:
        dx = x2-x1
        dy = y2-y1

        p1x = x1 + ratio * dx - ratio * dy
        p1y = y1 + ratio * dy + ratio * dx
        p2x = x1 + (1 - ratio) * dx + ratio * dy
        p2y = y1 + (1 - ratio) * dy - ratio * dx
        
        island(x1, y1, x2, y2, n-1, ratio)
        island(x1, y1, p1x, p1y, n-1, ratio)
        island(p1x, p1y, p2x, p2y, n-1, ratio)
        island(p2x, p2y, x2, y2, n-1, ratio)
        

depth = int(input("Enter the depth: "))
ratio = float(input("Enter the ratio (0.25, 0.3): "))
island(0, 0, 1, 0, depth, ratio)
island(1, 0, 1, 1, depth, ratio)
island(1, 1, 0, 1, depth, ratio)
island(0, 1, 0, 0, depth, ratio)
plt.show()