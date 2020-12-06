import argparse
from compute_installments import ComputeInstallments


parser = argparse.ArgumentParser(description='Compute the loan installments')
parser.add_argument(
  '-p',
  '--principal',
  type=float,
  help='The total amount borrowed'
)
parser.add_argument(
  '-i',
  '--iperiods',
  type=int,
  help='The number of installments in which the loan will be returned'
)
parser.add_argument(
  '-t',
  '--typeperiods',
  type=str,
  choices=['months', 'fortnights', 'weeks'],
  help='The unit of installment period'
)
parser.add_argument(
  '-r',
  '--rate',
  type=float,
  help='The annual interest rate of theloan'
)
args = parser.parse_args()
p_amount = args.principal
i_periods = args.iperiods
ip_type = args.typeperiods
i_rate = args.rate
computer = ComputeInstallments(p_amount=p_amount, i_periods=i_periods, ip_type=ip_type, i_rate=i_rate)
computer.find_installments()
