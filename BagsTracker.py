from math import ceil, floor


def get_min_size_of_square(n, w, h):
    left = 1
    right = max(w, h) * n
    while True:
        if right - left == 1:
            ans = right
            break
        middle = ceil((right - left) / 2 + left)
        count_in_row = floor(middle / w)
        count_in_column = floor(middle / h)
        area = count_in_row * count_in_column
        if area < n:
            left = middle
        elif area > n:
            right = middle
        else:
            ans = middle
            break
    return ans
