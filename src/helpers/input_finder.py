import configHelper

CONFIG = configHelper.get_config()

if CONFIG['input'] == 'console':
    from input.console import ConsoleInput as Input
else:
    from input.buttons import ButtonsInput as Input