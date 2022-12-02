from typing import List


def solution(lines: List[str]):
    temp = None
    count = 0
    for idx, line in enumerate(lines[:-2]):
        num = int(line) + int(lines[idx + 1]) + int(lines[idx + 2])
        if temp is None:
            temp = num
            continue
        if num > temp:
            count += 1
        temp = num
    return count


def test():
    questions = ["199", "200", "208", "210", "200", "207", "240", "269", "260", "263"]
    answer = 5
    my_answer = solution(questions)
    assert solution(questions) == answer
