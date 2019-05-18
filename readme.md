# Python Command Line Calculator

Get expressions results from command line.

## Setup

```
# Clone the project
git clone https://github.com/yasutot/python-command-line-calculator.git

# Enter the app directory
cd python-command-line-calculator

# Calculate
python3 calculator.py "(2+3)^2/(1+6)"  # 3
```

### Usage Examples

- Operations: Sum, Subtraction, Multiplication, Division, Modulo and Exponentiation
- It only calculates integer values.

```
# Write down the expression as argument for calculator.py
python3 calculator.py 2+3
# 5

python3 calculator.py 10-3
# 7

python3 calculator.py 7*7
# 49

python3 calculator.py 90/9
# 10

python3 calculator.py 2^10
# 1024

python3 calculator.py 27%4
# 3

python3 calculator.py 2+3*6
# 20

# It also accepts expressions with spaces
python3 calculator.py 2/   3      -6
# -6

# To use parenthesis, the expression must be between quotation marks
python3 calculator.py "(6/2) * 2 ^ 3"
# 24
```