from typing import List


def solution(lines: List[str]):
    length = len(lines)
    digits = len(lines[0])
    results = [0] * digits
    gamma = 0
    epsilon = 0
    nums = get_str_input(lines)

    # for idx, result in enumerate(results):
    #     print(result, len(results) - idx)
    #     if result > length // 2:
    #         gamma += 1 << (len(results) - idx - 1)
    #     else:
    #         epsilon += 1 << (len(results) - idx - 1)
    o2, co2 = get_result(nums, 0), get_result_rev(nums, 0)
    return int(o2,2) * int(co2,2)

def get_result(nums: List[str], digit: int):
    if len(nums) == 1:
        return nums[0]
    pos = get_position_result(nums)
    if pos[digit] == len(nums)/ 2: # 1 is the MCB
        return get_result(get_filtered_result(nums, digit, "1"), digit+1)
    elif pos[digit] >= len(nums)/ 2: # 1 is the MCB
        return get_result(get_filtered_result(nums, digit, "1"), digit+1)
    else: # 0 is the MCB
        return get_result(get_filtered_result(nums, digit, "0"), digit+1)

def get_result_rev(nums: List[str], digit: int):
    if len(nums) == 1:
        return nums[0]
    pos = get_position_result(nums)
    if pos[digit] == len(nums)/ 2: # 1 is the MCB
        return get_result_rev(get_filtered_result(nums, digit, "0"), digit+1)
    elif pos[digit] >= len(nums)/ 2: # 1 is the MCB
        return get_result_rev(get_filtered_result(nums, digit, "0"), digit+1)
    else: # 0 is the MCB
        return get_result_rev(get_filtered_result(nums, digit, "1"), digit+1)

def get_str_input(lines: List[str]):
    return [str(line, "utf-8") if isinstance(line, bytes) else line for line in lines]

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
