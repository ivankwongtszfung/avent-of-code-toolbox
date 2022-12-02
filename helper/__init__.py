from typing import List

import requests


class BadRequest(Exception):
    pass


class AventOfCode:
    def __init__(self, session_id):
        self.session_id = session_id

    def get_question_input(self, question_no: int, year: int) -> List[str]:
        if int(question_no) != question_no:
            raise Exception("question_no has to be a number")
        r = requests.get(
            f"https://adventofcode.com/{year}/day/{question_no}/input",
            cookies={"session": self.session_id},
            stream=True,
        )
        if not r.ok:
            raise BadRequest("we get a bad request, try renew your session")
        return [
            str(line, "utf-8") if isinstance(line, bytes) else line
            for line in r.iter_lines()
        ]
