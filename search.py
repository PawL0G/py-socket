from typing import Any

"""
Implementation of search criteria by "category" or "user" or "time" in one function
"""


def search(file_name: str, criteria: str) -> Any:
    with open(file_name) as f:
        lines = f.readlines()
        count = 0
        for i, line in enumerate(lines):
            if criteria in line:
                if count < 10:
                    for j in lines[i:i + 1]:
                        print(f'Line in {file_name} #{i}: ' + j)
                        count += 1
        f.close()


if __name__ == "__main__":
    # get 10 event from broadcast server in buffered text
    # filter types: category, user, time
    criteria_dict = {'category': '#update', 'user': '@all', 'time': '13/06/2021 11:05:43'}
    search('data.txt', criteria_dict.get('user'))
