import numpy as np
import os


def score(indexes_of_books, books):
    result = 0
    for i in indexes_of_books:
        result += books[i]
    return result


path_data = os.path.join("datasets", "a_example.txt")  # CHECK

with open(path_data) as f:
    lines = f.readlines()
    number_of_books, number_of_libraries, number_of_days = lines[0].split()
    scores_of_books = np.asarray(lines[1].split(), int)
    line_index = 2
    libraries = {}
    for lib_index in range(int(number_of_libraries)):
        libraries[lib_index] = [np.asarray(lines[line_index].split(), int),
                                np.asarray(lines[line_index + 1].split(), int),
                                score(np.asarray(lines[line_index + 1].split(), int), scores_of_books)]
        line_index += 2
    print(number_of_books, number_of_libraries, number_of_days)
    print(scores_of_books)
    print(libraries)
