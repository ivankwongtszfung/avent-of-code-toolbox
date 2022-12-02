from typing import List


def solution(lines: List[str]):
    x, y, aim = 0, 0, 0
    for line in lines:
        str_line = str(line, "utf-8") if isinstance(line, bytes) else line
        direction, step = str_line.split(" ")
        int_step = int(step)
        if direction == "forward":
            x += int_step
            y += int_step * aim
        elif direction == "up":
            aim -= int_step
        elif direction == "down":
            aim += int_step
    print({x, y, aim})
    return abs(x * y)


def test():
    questions = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]
    answer = 900
    my_answer = solution(questions)
    assert my_answer == answer
