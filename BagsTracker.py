def get_min_size_of_square(n, w, h):
    count_of_row = 2
    area = n * w
    area_last = area
    while area_last >= area and count_of_row <= n:
        area_last = area
        if n % count_of_row != 0:
            count_in_column = round(n / count_of_row)
            if count_in_column * count_of_row < n:
                count_in_column += 1
        else:
            count_in_column = n / count_of_row
        area = min(area, max(count_in_column * w, h * count_of_row))
        count_of_row += 1
    return area
