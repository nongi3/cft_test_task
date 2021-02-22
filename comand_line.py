import easygui
import os
import sys


def try_split_input_parameters(input_values):
    result = {'order': 'a'}
    if len(input_values) < 4:
        result['error'] = 'not enough parameters'
        return result
    if '-a' in input_values[1] or '-d' in input_values[1]:
        result['order'] = input_values[1][1:2]
        input_values.pop(1)
    if '-i' in input_values[1]:
        result['type'] = 'int'
    elif '-s' in input_values[1]:
        result['type'] = 'str'
    else:
        result['error'] = 'incorrect input parameters (type)'
        return result
    result['output_file_path'] = input_values[2]
    result['input_file_path'] = []
    for val in range(3, len(input_values)):
        result['input_file_path'].append(input_values[val])
    return result


def get_input_parameters():
    input_parameters = try_split_input_parameters(sys.argv)
    if 'error' in input_parameters:
        easygui.msgbox(input_parameters['error'], 'Some error!')
        if not easygui.ynbox('Wanna continue with default parameters? (asc, string, out.txt)'):
            return 1
        else:
            input_parameters['order'] = 'a'
            input_parameters['type'] = 'str'
            input_parameters['output_file_path'] = 'out.txt'
            input_parameters['input_file_path'] = []
            while True:
                path = easygui.fileopenbox('Choose file or close this window to continue:', 'Input files')
                if path is None:
                    break
                input_parameters['input_file_path'].append(path)
        input_parameters.pop('error') 
    return input_parameters


def is_correct_paths(input_parameters):
    if not os.path.isfile(input_parameters['output_file_path']):
        return False
    for path in input_parameters['input_file_path']:
        if not os.path.isfile(path):
            return False
    return True


def remove_invalid_file_paths(input_parameters):
    if not os.path.isfile(input_parameters['output_file_path']):
        input_parameters['output_file_path'] = 'out.txt'
    on_remove = []
    for path in input_parameters['input_file_path']:
        if not os.path.isfile(path):
            on_remove.append(input_parameters['input_file_path'].index(path))
    for index in on_remove:
        input_parameters['input_file_path'].pop(index)
    return input_parameters
