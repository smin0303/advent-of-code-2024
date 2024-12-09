import re

def find_top_hat(lst):
    for l in range(len(lst)):
        letter = re.search("\^", lst[l])
        if letter:
            start, end = letter.span()
            return l, start
        
def up(i, j):
    return i - 1, j

def down(i, j):
    return i + 1, j

def left(i, j):
    return i, j - 1

def right(i, j):
    return i, j + 1

def solve1(lst, start, end):
    height = len(lst)
    width = len(lst[0])
    row = start
    column = end
    direction = [up, right, down, left]
    idx = 0
    try:
        while row >=0 and row < height and column >= 0 and column < width :
            while lst[row][column] != '#':
                lst[row][column] = 'X'
                prev_r = row
                prev_c = column
                row, column = direction[idx % 4](row, column)
            row = prev_r
            column = prev_c
            idx += 1
    finally:
        c = 0
        for line in lst:
            c += line.count('X')
        return c

def solve2():
    return
 

def main():
    search = []
    with open("input.txt", 'r') as file:
        line = file.read().split("\n")
        for l in line[:]:
            search.append(l)

    row, column = find_top_hat(search)

    lst_lst = []
    for l in search:
        lst_lst.append(list(l))

    print("Part 1:", solve1(lst_lst, row, column))
    # print("Part 2:", solve2(word_search))

if __name__ == "__main__":
    main()