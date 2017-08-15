import configHelper


CONFIG = configHelper.get_config()

def get_input_processor():
    if CONFIG['input'] == 'console':
        from input.console import ConsoleInput as Input
    else:
        from input.buttons import ButtonsInput as Input
    return Input()

def get_output_processor():
    if CONFIG['output'] == 'console':
        from output.console import ConsoleOutput as Output
    else:
        from output.arduino import ArduinoOutput as Output
    return Output()