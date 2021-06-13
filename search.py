from typing import Any

"""
Implementation of search criteria by "category" or "user" or "time" in one function
"""


def search(file_name: str, criteria: str) -> Any:
    with open(file_name) as f:
        lines = f.readlines()
        f.close()
        count = 0
        for i, line in enumerate(lines):
            if criteria in line:
                if count < 10:
                    for j in lines[i:i + 1]:
                        print(f'Line in {file_name} #{i}: '+j)
                        count += 1


if __name__ == "__main__":
    search('data.txt', '#update')
