import numpy as np


class ComputeInstallments:
    def __init__(self, p_amount=100000, i_periods=360, ip_type='months', i_rate=0.0375):
        self.p_amount = p_amount
        self.i_periods = i_periods
        self.ip_type = ip_type
        self.i_rate = i_rate

    def interest_p_period(self):
        if self.ip_type == 'months':
            ip_rate = self.i_rate/12
        elif self.ip_type == 'fortnights':
            ip_rate = self.i_rate/(365.25/14)
        else:
            ip_rate = self.i_rate/(365.25/7)
        return ip_rate

    def create_matrix(self):
        r = self.interest_p_period()
        list_2d = [
          [-r] * i + [1] + [0] * (self.i_periods - 1 - i) + [-1] for
          i in range(self.i_periods)
        ]
        first_row = [1] * self.i_periods + [0]
        full_set = [first_row] + list_2d
        return full_set

    def create_constants(self):
        constants = [self.p_amount] + [-self.p_amount * self.interest_p_period()] * self.i_periods
        return constants

    def solve_system(self):
        A = np.array(self.create_matrix())
        inv_A = np.linalg.inv(A)
        B = np.array(self.create_constants())
        sol_set = inv_A.dot(B)
        return sol_set

    def find_installments(self):
        solution = self.solve_system()
        installment = solution[-1]
        for k, s in enumerate(solution[:(len(solution) - 1)]):
            print(
              'Installment {k}:   principal amount: {s:.1f},   interest: {interest:.1f}, total: {total:.1f}'.format(
                k=k + 1,
                s=s,
                interest=installment - s,
                total=installment
              )
            )
