# Part 1
def solve1(lst):
    count = 0

    xmas = [
        [(0, 0), (0, 1), (0, 2), (0, 3)],       # horizontal right
        [(0, 0), (0, -1), (0, -2), (0, -3)],    # horizontal left 
        [(0, 0), (1, 0), (2, 0), (3, 0)],       # down
        [(0, 0), (-1, 0), (-2, 0), (-3, 0)],    # up
        [(0, 0), (-1, 1), (-2, 2), (-3, 3)],    # diag right-up
        [(0, 0), (1, 1), (2, 2), (3, 3)],       # diag right-down
        [(0, 0), (1, -1), (2, -2), (3, -3)],    # diag left-down
        [(0, 0), (-1, -1), (-2, -2), (-3, -3)]   # diag left-up
    ]

    height = len(lst)
    width = len(lst[0])

    for i in range(height):
        for j in range(width):
            for combo in xmas:
                possible = ""
                for pos in combo:
                    if (i + pos[0]) >= 0 and (j + pos[1]) >= 0 and (i + pos[0]) < height and (j + pos[1]) < width: 
                        possible += lst[i + pos[0]][j + pos[1]]
                if possible == "XMAS":
                    count += 1

    return count


def solve2(lst):
    count = 0

    xmas = [
        [(-1, -1), (0, 0), (1, 1)],     # \ down
        [(1, 1), (0, 0), (-1, -1)],     # \ up
        [(-1, 1), (0, 0), (1, -1)],     # / down
        [(1, -1), (0, 0), (-1, 1)]      # / up
    ]

    height = len(lst)
    width = len(lst[0])

    for i in range(height):
        for j in range(width):
            mas = []
            for combo in xmas:
                possible = ""
                for pos in combo:
                    if (i + pos[0]) >= 0 and (j + pos[1]) >= 0 and (i + pos[0]) < height and (j + pos[1]) < width: 
                        possible += lst[i + pos[0]][j + pos[1]]
                if possible == "MAS":
                    mas.append(possible)
            if len(mas) == 2:
                count +=1

    return count



def main():
    word_search = []
    with open("input.txt", 'r') as file:
        line = file.read().split("\n")
        for l in line[:-1]:
            word_search.append(list(l))

    print("Part 1:", solve1(word_search))
    print("Part 2:", solve2(word_search))

if __name__ == "__main__":
    main()