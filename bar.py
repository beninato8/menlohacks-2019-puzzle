from imageio import imread
import matplotlib.pyplot as plt
image = imread("bar.png")
l = image.tolist()
print(len(l[0]))
a = ''
# for x in l:
#     if x == [0, 0, 0]:
#         print(0, end='')
#         a += '0'
#     else:
#         print(1, end='')
#         a += '1'

for x in l[0]:
    print(str(x).replace('[255, 255, 255]', '0').replace('[0, 0, 0]', '1'), end='')
print()

for x in l[0]:
    print(str(x).replace('[255, 255, 255]', '1').replace('[0, 0, 0]', '0'), end='')
print()
# 102010201020203020101020303010
# 010101010301030101010103030102
from pprint import pprint
# binaries = ['101101011010001101100011101101010110001110001110100', '010010100101110010011100010010101001110001110001011']
# l = []
# for s in binaries:
#     a = [x for x in s.split('1') if x != '']
#     l.append([len(x) for x in a])
#     a = [x for x in s.split('0') if x != '']
#     l.append([len(x) for x in a])

# lengths = [[1, 1, 1, 1, 3, 1, 3, 1, 1, 1, 1, 3, 3, 1, 2], [1, 2, 1, 2, 1, 2, 2, 3, 2, 1, 1, 2, 3, 3, 1]]
# pprint(l)


"""
101101011010001101100011101101010110001110001110100
010010100101110010011100010010101001110001110001011
"""
exit()

plt.imshow(l[0:1])
plt.show()