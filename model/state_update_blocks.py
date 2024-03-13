from model.parts.policy_functions import *
from model.parts.state_update_functions import *


partial_state_update_blocks = [
    # Обновление времени + задание seed'а в начале симуляции
    {
        'policies': {
            'update_time': p_update_time,
        },
        'variables': {
            'curr_time': s_update_curr_time,
            'prev_time': s_update_prev_time,
        }
    }, 

    # Обновление баланса фонда
    {
        'policies': {
            'update_fund': p_update_fund,
        },
        'variables': {
            'fund_balance': s_update_fund_balance,
            'promised_fund_balance': s_update_promised_fund_balance,
            'epoch_index': s_update_epoch_index,
            'epoch_start': s_update_epoch_start,
            'epoch_promised_init_investment': s_update_epoch_promised_init_investment,
        }
    }, 
]