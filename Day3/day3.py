import re

def first_problem(s):
    answer = 0
    mults = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", s)
    for tup in mults:
        num1 = int(tup[0])
        num2 = int(tup[1])
        answer += num1 * num2
    return answer


def second_problem(s):
    no_whitespace = re.sub(r"\s", "", s)
    return re.sub(r"don\'t\(\).*?do\(\)", "", no_whitespace)


if __name__=="__main__":
    file = open('input.txt', 'r')
    file_str = file.read()
    print("First part answer:", first_problem(file_str))
    print("Second part answer:", first_problem(second_problem(file_str)))  