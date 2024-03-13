from radcad.types import StateVariables


initial_state: StateVariables = {
    'fund_balance': 0.0, # действительный счет фонда, млн. USD
    'promised_fund_balance': 0.0, # заявленный счет фонда, млн. USD
    'curr_time': 0.0, # Текущее время, год
    'prev_time': 0.0, # Время на предыдущем шаге, год
    'epoch_index': None, # Индекс текущей эпохи; в рамках эпохи параметры постоянны
    'epoch_start': 0.0, # Начало текущей эпохи
    'epoch_promised_init_investment': 0.0, # Инвестиции на начало текущей эпохи исходя из обещанной ставки
}