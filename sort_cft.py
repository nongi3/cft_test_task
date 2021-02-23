import easygui

import comand_line
import correct_file
import logic


def main():
    input_parameters = comand_line.get_input_parameters()
    if not comand_line.is_correct_paths(input_parameters):
        easygui.msgbox("Some paths isn't correct. We have to remove them, sorry.")
        input_parameters = comand_line.remove_invalid_file_paths(input_parameters)
    input_parameters['input_file_path'] = correct_file.check_for_correct_data(input_parameters)
    logic.logic(input_parameters)


if __name__ == '__main__':
    main()
