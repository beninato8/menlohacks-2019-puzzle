from imageio import imread
import matplotlib.pyplot as plt

def flatten_all(l):
    tmp = []
    for x in l:
        if isinstance(x, list):
            tmp += x
        else:
            tmp += [x]
    if any(isinstance(x, list) for x in tmp):
        return flatten(tmp)
    return tmp

def flatten(l):
    tmp = []
    for x in l:
        if isinstance(x, list):
            tmp += x
        else:
            tmp += [x]
    return tmp

image = imread("GridPixels.png")
l = image.tolist()
letters = [['j', 'w', 'n', 'm', 'M', 'c', 'x', 'e', '4', 'i', '6', '2', 'i', 'x', 'z', 'a', 'q', 'u', '2', '8'], ['i', 'u', 'b', 'c', '0', 'i', '7', 't', 'f', 'g', 'u', 'l', '9', '3', '2', 'x', 'G', 'o', 'P', 'l'], ['o', 'l', '3', '8', '9', 'q', 'o', 'p', '-', '>', '<', '9', '*', '&', 'j', 'y', 'i', 'f', 'O', 'P'], ['4', '9', 'f', 'w', 'r', '%', 'o', 'R', 'b', '8', 'L', 'l', 'z', 'w', 'B', '`', 'P', 'o', 'Q', 'Z'], ['f', 'k', 'i', '6', '9', '.', 'k', 'b', "'", '[', "'", 'P', '"', ']', 'h', 'd', 'e', '3', '8', '6'], ['h', '5', 'f', 'i', 'o', 'l', 'i', '.', "'", 'p', 'y', 'p', '1', '8', '7', '6', 'v', 'c', 'x', 'J'], ['i', 'i', 'h', 's', 'l', 'p', '7', '^', '0', '8', 'i', 'u', 't', 'P', 'w', '9', 'w', 'o', 'n', 'm'], ['c', 'P', 'T', 'u', '2', '7', '0', 'g', 'u', 'r', 'k', 'o', ';', '=', 'b', 'f', 's', ']', 'k', 'z'], ['6', '/', '.', '$', 'k', 'h', 'b', 'd', '4', '@', 'w', 'i', 'o', 'n', 'b', 'v', '0', '9', '6', 'h'], ['i', '7', 'u', '8', 'd', 'e', 't', '5', 'i', 'u', 'r', 'c', 'v', 'm', 'p', 'l', 'j', 'h', 'G', '3'], ['7', '8', 'y', 'i', '9', 'd', '5', 'n', 'b', 'c', '9', '7', 'p', '3', 'c', '9', 'z', 'c', '3', '0'], ['8', 'k', 'i', 'u', 'Y', '.', ']', ';', 'v', '`', 'i', 'u', 'g', 'l', 'o', 'P', 'P', 'G', 'w', 'Q'], ['8', '7', '6', 'G', 'G', 'r', 'w', 'p', '4', '&', '*', '2', 's', 'h', 'k', 'n', 'v', 'f', 'J', 'H'], ['O', 'P', '7', '3', 'h', 'j', 'i', '8', '5', 'd', 'c', 'v', 'j', 't', '9', '0', 'l', 'k', '7', 'j'], ['o', '9', '6', 'r', 'd', 'e', 'r', 'r', '3', 'h', '2', 'u', '7', 'r', 'v', 'K', 'h', 'g', '9', '4'], ['g', '8', 'G', 'I', 'Y', 't', 'w', '2', '1', '8', '9', '0', 'm', 'Q', 'j', 'b', 'x', 'v', 'o', '0'], ['7', '6', '0', 'p', 'k', '[', 'f', ']', '8', '7', 'g', 'j', 'f', 'j', 's', 'M', '4', '3', 'y', 't'], ['A', 'I', 'e', 'r', 't', '3', '#', '$', 'R', 'Y', 'H', '3', 'i', 'q', 'U', 'w', 'r', 'i', 'q', 'g']]

l2 = []
for i, x in enumerate(l):
    if i % 4 == 0:
        tmp = []
        for j, y in enumerate(x):
            if j % 4 == 0:
                tmp.append(y)
        l2.append(tmp)
l2 = l2[1:-1]

l = l2

a = flatten(l)
print(len(set([str(x) for x in a])))
colors = set([str(x) for x in a])
# print(colors)
for a in colors:
    print(a, end=' ')
    for i, x in enumerate(l):
        for j, y in enumerate(x):
            if str(l[i][j]) == a:
                print(letters[i][j], end='')
    print()
# exit()
plt.imshow(l)
plt.show()