states = [ 'menu', 'learn-menu', 'evaluate-menu', 'learn', 'write', 'evaluate', 'config' ]

state_variables = {'state': 'menu', 'level': 1}

def set_state(new_state, new_level = None):
    if new_state in states:
        if new_state == 'learn' or new_state == 'evaluate':
            _set_level(new_level)

        state_variables['state'] = new_state
    else:
        raise Exception('Trying to set invalid state')

def get_state():
    return state_variables['state']

def _set_level(new_level):
    if not new_level:
        raise Exception('Trying to set learn or write status without setting a level')

    state_variables['level'] = new_level

