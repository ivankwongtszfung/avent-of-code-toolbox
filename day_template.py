from typing import List


def solution(lines: List[str]):
    for line in lines:
        str_line = str(line, "utf-8") if isinstance(line, bytes) else line
    return


def test():
    questions = []
    answer = 0
    my_answer = solution(questions)
    assert my_answer == answer
