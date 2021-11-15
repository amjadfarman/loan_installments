import argparse
from compute_installments import ComputeInstallments


parser = argparse.ArgumentParser(description="Compute the loan installments")
loan_period_choices = ["months", "fortnights", "weeks"]

parser.add_argument(
  "-p",
  "--principal",
  type=float,
  help='The total amount borrowed',
)

parser.add_argument(
  "-i",
  "--iperiods",
  type=int,
  nargs="?",
  #const=-1,
  help="The number of installments in which the loan will be returned",
)

parser.add_argument(
  "-y",
  "--years",
  type=int,
  nargs="?",
  #const=-1,
  help=(
    "The number of installments in which the loan will be returned. Optional but one "
    "from -i and -y must be supplied"
  ),
)

parser.add_argument(
  "-t",
  "--typeperiods",
  type=str,
  choices=loan_period_choices,
  help=(
    "The unit of installment period. Optional but one from -i and -y must be supplied"
  ),
)

parser.add_argument(
  "-r",
  "--rate",
  type=float,
  help="The annual interest rate of the loan",
)

args = parser.parse_args()
p_amount = args.principal
i_periods = args.iperiods
loan_years = args.years
ip_type = args.typeperiods
i_rate = args.rate
print(i_periods, loan_years)

if not i_periods and not loan_years:
  msg = (
    "No loan term (in years) specified by the argument -y or --years or number of "
    "installments specified by the argument -i or --iperiods"
  )
  print(msg)
elif not i_periods and loan_years:
  periods_multiplier = {
    "months": 12,
    "fortnights": 365.25/14,
    "weeks": 365.25/7
  }
  i_periods = int(loan_years * periods_multiplier[ip_type])
  computer = ComputeInstallments(
    p_amount=p_amount, i_periods=i_periods, ip_type=ip_type, i_rate=i_rate
  )
  computer.find_installments()

else:
  computer = ComputeInstallments(
    p_amount=p_amount, i_periods=i_periods, ip_type=ip_type, i_rate=i_rate
  )
  computer.find_installments()
