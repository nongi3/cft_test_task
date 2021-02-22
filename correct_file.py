def is_correct_data_type(data, data_type):
    if data_type == 'str':
        return data.isalpha()
    else:
        return data.isdigit()


def comparison(order, data_type, a, b):
    if data_type == 'int':
        a = int(a)
        b = int(b)
    if order == 'a':
        return a < b
    else:
        return a > b


def check_for_correct_data_types(input_parameters):
    correct_files = []
    have_to_sort = []
    for file_path in input_parameters['input_file_path']:
        with open(file_path, 'r') as file:
            latest = file.readline()
            if not is_correct_data_type(latest, input_parameters['type']):
                continue
            is_good = True
            while True:
                current = file.readline()
                if not is_correct_data_type(latest, input_parameters['type']):
                    is_good = False
                    break
                if len(current) == 0:
                    break
                if not comparison(input_parameters['order'], input_parameters['type'], latest, current) and \
                        file_path not in have_to_sort:
                    have_to_sort.append(file_path)
            if is_good:
                correct_files.append(file_path)
    return correct_files


# TODO check for filenames
