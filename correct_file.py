import os


import logic


def is_correct_data_type(data, data_type):
    if data_type == 'int':
        return data[:-1].isdigit()
    return True


def check_for_correct_data(input_parameters):
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
                if len(current) == 0:
                    break
                if not is_correct_data_type(latest, input_parameters['type']):
                    is_good = False
                    break
                if not logic.comparison(input_parameters['order'], input_parameters['type'], latest, current) and \
                        file_path not in have_to_sort:
                    have_to_sort.append(file_path)
                latest = current
            if is_good:
                correct_files.append(file_path)
    for file_path in have_to_sort:
        if file_path in correct_files:
            file_sort(file_path, input_parameters['order'], input_parameters['type'])
    print(correct_files, have_to_sort)
    return correct_files


def delete_temp_files(files):
    for file in files:
        os.remove(file)


def file_sort(file_path, order, data_type):
    index_name = 0
    input_file_path = []
    with open(file_path, 'r') as file:
        latest = file.readline()
        current_chunk = open('current_chunk' + str(index_name), 'w')
        input_file_path.append('current_chunk' + str(index_name))
        current_chunk.write(latest)
        while True:
            current = file.readline()
            if len(current) == 0:
                break
            if logic.comparison(order, data_type, latest, current):
                current_chunk.write(current)
            else:
                index_name += 1
                current_chunk.close()
                current_chunk = open('current_chunk' + str(index_name), 'w')
                input_file_path.append('current_chunk' + str(index_name))
                current_chunk.write(current)
            latest = current
        current_chunk.close()
    logic.logic({'order': order,
                 'type': data_type,
                 'output_file_path': file_path,
                 'input_file_path': input_file_path})
    delete_temp_files(input_file_path)

# TODO check for filenames
