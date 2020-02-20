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
    n_books, n_libraries, n_days = np.asarray(lines[0].split()).astype(int)
    scores_of_books = np.asarray(lines[1].split(), int)
    main_dict = {idx: val for idx, val in enumerate(scores_of_books)}
    line_index = 2
    libraries = {}
    for lib_index in range(int(n_libraries)):
        libraries[lib_index] = [np.asarray(lines[line_index].split(), int),
                                np.asarray(lines[line_index + 1].split(), int),
                                score(np.asarray(lines[line_index + 1].split(), int), scores_of_books)]
        line_index += 2

print(n_books, n_libraries, n_days)
print(main_dict)
print(libraries)


