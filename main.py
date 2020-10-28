if __name__ == '__main__':
    n = 10  # int(input())
    w = 3  # int(input())
    h = 2  # int(input())
    count_of_row = 2
    area = n * w
    area_last = area + 1
    while area_last > area:
        area_last = area
        if n % count_of_row != 0:
            count_in_column = round(n / count_of_row)
            if count_in_column * count_of_row < n:
                count_in_column += 1
        else:
            count_in_column = n / count_of_row
        area = min(area, max(count_in_column * w, h * count_of_row))
        count_of_row += 1
    print(area)
