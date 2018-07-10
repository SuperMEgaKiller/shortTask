"""
Short task description:
1. Load numbers from file (any method)
2. Pass them to calculate_numbers function
3. Compare output with basic implementation
4. Tweak until you're gonna get better time ;-)


"""
from utils import timing
import os
from math import sqrt, pow
import pandas as pd
import multiprocessing as mp

@timing
def load_file(base_dir: str) -> list:
    rlist = []
    csv_path = os.path.join(base_dir, "filedir", "numbers.csv")
    df = pd.read_csv(csv_path, sep=" ")
    rlist = df.values.tolist()
    return rlist


def calculate_numbers(numbers_pair: list) -> float:
    summed_output = 0
    for i in range(0, 50000):
        summed_output += pow(sqrt((numbers_pair[0] + numbers_pair[1]) * 5), 10)
    return summed_output


@timing
def algorithm_basic_logic_implementation(numbers_list) -> list:
    results = []
    for pair in numbers_list:
        sum_result = calculate_numbers(pair)
        results.append(sum_result)
    return results


# Warning, do not reimplement calculate_numbers function, reimplement algorithm_basic_logic_implementation one
# So that it will pass faster.
@timing
def your_algorithm_executing_function(numbers_list) -> list:
    pool = mp.Pool(mp.cpu_count() - 1)
    result = pool.map(calculate_numbers, numbers_list)
    pool.close()
    pool.join()
    return result


def main() -> list:
    work_directory = os.path.dirname(os.path.abspath(__file__))

    numbers_to_calculate = load_file(work_directory)
    base_results = algorithm_basic_logic_implementation(numbers_to_calculate)

    your_implementation_results = your_algorithm_executing_function(numbers_to_calculate)

    return [base_results, your_implementation_results]


if __name__ == "__main__":
    output = main()
