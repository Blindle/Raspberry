from stateEnum import StateEnum

states = [StateEnum.MENU.key,
          StateEnum.LEARN_MENU.key,
          StateEnum.EVALUATE_MENU.key,
          StateEnum.LEARN.key,
          StateEnum.WRITE.key,
          StateEnum.EVALUATE.key,
          StateEnum.CONFIG.key
         ]

state_variables = {'state': StateEnum.MENU.key, 'level': StateEnum.LEVEL_1.key}


def set_state(new_state, new_level=None):
    if new_state in states:
        if new_state == StateEnum.LEARN.key or new_state == StateEnum.EVALUATE.key:
            _set_level(new_level)

        state_variables['state'] = new_state
    else:
        raise Exception('Trying to set invalid state')


def get_state():
    return state_variables['state']

def get_level():
    return state_variables['level']


def _set_level(new_level):
    if not new_level:
        raise Exception(
            'Trying to set learn or write status without setting a level')

    state_variables['level'] = new_level
