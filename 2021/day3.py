from typing import List


def solution(lines: List[str]):
    nums = get_str_input(lines)
    o2, co2 = get_result(nums), get_result(nums, mcb=False)
    return int(o2, 2) * int(co2, 2)


def get_str_input(lines: List[str]):
    return [str(line, "utf-8") if isinstance(line, bytes) else line for line in lines]


def get_result(nums: List[str], digit: int = 0, mcb: bool = True):
    if len(nums) == 1:
        return nums[0]
    pos = get_position_result(nums)
    if pos[digit] >= len(nums) / 2:  # 1 is the MCB
        target = "1" if mcb else "0"
        return get_result(get_filtered_result(nums, digit, target), digit + 1, mcb)
    else:  # 0 is the MCB
        target = "0" if mcb else "1"
        return get_result(get_filtered_result(nums, digit, target), digit + 1, mcb)


def get_position_result(nums: List[str]):
    results = [0] * len(nums[0])
    for num in nums:
        pos_of_1 = [idx for idx, digit in enumerate(num) if digit == "1"]
        for pos in pos_of_1:
            results[pos] += 1
    return results


def get_filtered_result(nums: List[str], digit: int, target: str):
    return [num for num in nums if num[digit] == target]


def test():
    questions = [
        "00100",
        "11110",
        "10110",
        "10111",
        "10101",
        "01111",
        "00111",
        "11100",
        "10000",
        "11001",
        "00010",
        "01010",
    ]
    answer = 230
    my_answer = solution(questions)
    assert my_answer == answer
