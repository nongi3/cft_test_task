import easygui

import comand_line
import correct_file


def comparison(order, data_type, a, b):
    if data_type == 'int':
        a = int(a)
        b = int(b)
    if order == 'a':
        return a < b
    else:
        return a > b


def logic(input_parameters):
    out_file = open(input_parameters['output_file_path'], 'w')
    input_files = []
    for file_path in input_parameters['input_file_path']:
        input_files.append(open(file_path, 'r'))
    while len(input_files) > 0:
        start_pos = input_files[0].seek(0, 1)
        min_value = input_files[0].readline()
        input_files[0].seek(start_pos)
        index_of_min_value = 0
        for file_index in range(1, len(input_files)):
            start_pos = input_files[file_index].seek(0, 1)
            line = input_files[file_index].readline()
            input_files[file_index].seek(start_pos)
            if len(line) == 0:
                continue
            if comparison(input_parameters['order'], input_parameters['type'], line, min_value):
                min_value = line
                index_of_min_value = file_index
        if len(min_value) > 0 and min_value[-1] != '\n':
            min_value += '\n'
        out_file.write(min_value)
        input_files[index_of_min_value].readline()
        start_pos = input_files[0].seek(0, 1)
        is_over = input_files[0].readline()
        if len(is_over) == 0:
            input_files[index_of_min_value].close()
            input_files.pop(index_of_min_value)
        else:
            input_files[0].seek(start_pos)


def main():
    input_parameters = comand_line.get_input_parameters()
    if not comand_line.is_correct_paths(input_parameters):
        easygui.msgbox("Some paths isn't correct. We have to remove them, sorry.")
        input_parameters = comand_line.remove_invalid_file_paths(input_parameters)
    logic(input_parameters)


if __name__ == '__main__':
    main()
