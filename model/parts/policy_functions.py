import numpy as np
from model.utils import is_shock, runge_kutta4

def p_update_time(params, substep, state_history, previous_state):
    dtime = params['timestep']

    timestep = previous_state['timestep']
    curr_time = previous_state['curr_time']

    if previous_state['timestep'] == 0:
        np.random.seed(seed=previous_state['simulation']+previous_state['run']+previous_state['subset'])  

    if timestep == 0:
        new_curr_time = 0.
        new_prev_time = 0.
    else:
        new_curr_time = curr_time + dtime
        new_prev_time = curr_time

    return {
        'new_curr_time': new_curr_time,
        'new_prev_time': new_prev_time,
    }

def p_update_fund(params, substep, state_history, previous_state):
    timestep = params['timestep']
    shock_times = params['shock_times']
    rn_list = params['actual_profit_rate']
    rp_list = params['promised_profit_rate']
    rw_list = params['withdraw_rate']
    ri_list = params['investment_rate']
    s0_list = params['deposits_density']
    investment_list = params['investors_investments']
    manager_fund_list = params['manager_investments']
    invest_std = params['invest_std']
    withdraw_std = params['withdraw_std']

    curr_time = previous_state['curr_time']
    prev_time = previous_state['prev_time']
    epoch_index = previous_state['epoch_index']
    epoch_start = previous_state['epoch_start']
    epoch_promised_init_investment = previous_state['epoch_promised_init_investment']
    fund_balance = previous_state['fund_balance']
    promised_fund_balance = previous_state['promised_fund_balance']


    new_epoch_index = epoch_index
    new_epoch_start = epoch_start
    new_epoch_promised_init_investment = epoch_promised_init_investment

    shock_flag = is_shock(curr_time, prev_time, shock_times)
    if shock_flag:
        if epoch_index is None:
            new_epoch_index = 0
        else:
            new_epoch_index += 1
        new_epoch_promised_init_investment = promised_fund_balance + investment_list[new_epoch_index]
        new_epoch_start = curr_time

    rn = rn_list[new_epoch_index]
    rp = rp_list[new_epoch_index]
    rw = rw_list[new_epoch_index]
    ri = ri_list[new_epoch_index]
    s0 = s0_list[new_epoch_index]

    def s(t):
        return s0 * np.exp(ri * (t - new_epoch_start)) + np.random.normal(scale=invest_std)
    
    def w(t):
        dt = t - new_epoch_start
        try:
            return rw * np.exp((rp - rw) * dt) * \
                (new_epoch_promised_init_investment + s0 * (np.exp((rw + ri - rp) * dt) - 1) / (rw + ri - rp)) + \
                np.random.normal(scale=withdraw_std)
        except ZeroDivisionError:
            return rw * np.exp((rp - rw) * dt) * \
                (new_epoch_promised_init_investment + s0 * dt) + \
                np.random.normal(scale=withdraw_std)

    def fund_func(x, t):
        return rn * x + s(t) - w(t)
    
    def promised_fund_func(x, t):
        return rp * x + s(t) - w(t)

    if shock_flag:
        new_fund_balance = fund_balance + investment_list[new_epoch_index] + \
            manager_fund_list[new_epoch_index]
        new_promised_fund_balance = new_epoch_promised_init_investment
    else:     
        new_fund_balance = runge_kutta4(fund_balance, curr_time, timestep, fund_func)
        new_promised_fund_balance = runge_kutta4(promised_fund_balance, curr_time, timestep, promised_fund_func)

    return {
        'new_fund_balance': new_fund_balance,
        'new_promised_fund_balance': new_promised_fund_balance,
        'new_epoch_index': new_epoch_index,
        'new_epoch_start': new_epoch_start,
        'new_epoch_promised_init_investment': new_epoch_promised_init_investment,
    }