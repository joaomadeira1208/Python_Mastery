high_income = True
good_credit = False
student = False

if (high_income and good_credit) and not student:
    print("Eligible for loan")
else:
    print("Not eligible for loan")

# Short-circuit Evaluation
# Python uses short-circuit evaluation to evaluate logical expressions.
# It evaluates the left operand and then decides whether to evaluate the right operand.
# For example, in the expression x or y, if x is true, Python does not evaluate y.
