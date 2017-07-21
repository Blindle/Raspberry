from stateEnum import StateEnum

states = [ StateEnum.MENU, StateEnum.LEARN_MENU, StateEnum.EVALUATE_MENU, StateEnum.LEARN, StateEnum.WRITE, StateEnum.EVALUATE, StateEnum.CONFIG ]

state_variables = {'state': StateEnum.MENU, 'level': StateEnum.LEVEL_1}

def set_state(new_state, new_level = None):
    if new_state in states:
        if new_state == StateEnum.LEARN or new_state == StateEnum.EVALUATE:
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

