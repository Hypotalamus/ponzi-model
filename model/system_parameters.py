from dataclasses import dataclass
from typing import List
from radcad.utils import default


@dataclass
class Parameters:
    # длительность одного шага, год
    timestep: List[float]=default([1.e-3])
    # моменты изменения параметров модели, год
    shock_times: List[List[float]]=default([[0.58]])
    # C инвестиции менеджера, млн. USD
    manager_investments: List[List[float]]=default([[0., 0.]])
    # K инвестиции инвесторов, млн. USD 
    investors_investments: List[List[float]]=default([[0., 0.]])
    # s0 плотность депозитов в начале периодов, млн. USD / год  
    deposits_density: List[List[float]]=default([[1.13, 73.]])
    # ri скорость инвестиций, 1 / год 
    investment_rate: List[List[float]]=default([[7.187, 0.]])
    # rw скорость оттока средств, 1 / год 
    withdraw_rate: List[List[float]]=default([[1.47, 1.47]])
    # rp обещанная скорость прироста средств, 1 / год 
    promised_profit_rate: List[List[float]]=default([[2.773, 2.773]])
    # rn действительная скорость прироста средств, 1 / год 
    actual_profit_rate: List[List[float]]=default([[0.01, 0.01]])
    # Стандартное отклонение для инвестиций на каждом шаге
    invest_std: List[float]=default([1e1])
    # стандартное отклонение для оттока средств
    withdraw_std: List[float]=default([1e1])

parameters = Parameters().__dict__
