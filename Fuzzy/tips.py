import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Создаем входные и выходные переменные
quality = ctrl.Antecedent(np.arange(0, 11, 1), 'quality')
service = ctrl.Antecedent(np.arange(0, 11, 1), 'service')
tip = ctrl.Consequent(np.arange(0, 26, 1), 'tip')

# Автоматическое создание функций принадлежности
quality.automf(3)
service.automf(3)

# Ручное создание функций принадлежности для выходной переменной
tip['low'] = fuzz.trimf(tip.universe, [0, 0, 13])
tip['medium'] = fuzz.trimf(tip.universe, [0, 13, 25])
tip['high'] = fuzz.trimf(tip.universe, [13, 25, 25])

# Создаем правила нечеткого вывода
rule1 = ctrl.Rule(quality['poor'] | service['poor'], tip['low'])
rule2 = ctrl.Rule(service['average'], tip['medium'])
rule3 = ctrl.Rule(service['good'] | quality['good'], tip['high'])

# Создаем и настраиваем систему управления
tipping_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
tipping = ctrl.ControlSystemSimulation(tipping_ctrl)

# Пример входных данных
tipping.input['quality'] = 6.5
tipping.input['service'] = 9.8

# Вычисление результата
tipping.compute()

print(tipping.output['tip'])
