# Cmpoute loan installments

This project is aimed at computing the periodic installments, principal
amount paid, the interest paid, cumulative principal amount paid, total
principal amount remaining to be paid with each installment given the
annual interest rate, principal amount, the installment period or the
total installments if known or the period over which the loan will be
paid.

## Usage

The project is tested with Python 3.7 but should work fine with any
of the micro versions of Python 3.6, 3.7, 3.8 and 3.9.

After navigating to the project directory execute the `main.py` file
with the required arguments. Execute `main.py -h` or `main.py --help`
with python for more detail on the arguments. An example of usage is

```bash
python main.py -p 400000 -y 20 -t fortnights -r 0.0410
```

to find out the installment details when a borrower borrows $400,000
for a loan term of 20 years, borrower pays installments fortnightly and
the interest rate for the loan is 4.10%.