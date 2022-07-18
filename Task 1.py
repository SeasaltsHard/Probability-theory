import math

Salaries = [100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150]

#                                                 Arithmetic mean
ar_me = (sum(Salaries)) / (len(Salaries))
print(f'Arithmetic mean for the student salaries = {ar_me}')

#                                                Standard deviation

z = 0
for x in Salaries:
    y = x - ar_me
    z += y ** 2
print(f'Standard deviation for the student salaries = {math.sqrt(z / (len(Salaries)))}')

#                                               Bias of an estimator

print(f'Bias of an estimator for the student salaries = {(z / (len(Salaries)))}')

#                                                Unbiased estimator

print(f'Unbiased estimator for the student salaries = {(z / (len(Salaries) - 1))}')
