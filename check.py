from typing import Callable, Optional
from os.path import exists
import os
import pickle
import importlib.util
import sys

import typer

from helper import AventOfCode, BadRequest

SESSION_CACHE = "./.cache/aoc_session"


def import_module(question_no, year) -> Callable:
    file_path = f"./{year}/day{question_no}.py"
    module_name = "{year}day{question_no}"
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


def create_cache_folder():
    if not exists("./.cache"):
        os.mkdir("./.cache")


def write_session():
    session_id = input(
        "Please give us the session id from https://adventofcode.com/2022:\n"
    )
    create_cache_folder()
    try:
        aoc = AventOfCode(session_id)
        with open(SESSION_CACHE, "wb") as file:
            pickle.dump(aoc, file)
    except Exception as e:
        os.remove(SESSION_CACHE)
        raise e


def read_session() -> AventOfCode:
    with open(SESSION_CACHE, "rb") as f:
        return pickle.load(f)


def main(question_no: int, year: int = 2022):
    if not exists(SESSION_CACHE):
        write_session()
    retry = False
    while True:
        try:
            aoc_client = read_session()
            question_input = aoc_client.get_question_input(question_no, year)
            break
        except BadRequest:
            if retry:
                raise Exception("something's wrong")
            print("Bad Request!!!!!")
            retry = True
            write_session()
    module = import_module(question_no, year)
    module.test()
    print("tests passed")
    print(module.solution(question_input))


if __name__ == "__main__":
    typer.run(main)
