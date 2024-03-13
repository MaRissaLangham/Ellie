""" This file Desiciption can be found in the comment below """
# Author: Marissa Langham
# Date: 03/12/2023
# Description: Calculation skill file for Ellie
# File Name: calculations.py

import re
from sympy import sympify, SympifyError

def performCalculation(command):
    """
    Extracts a mathematical expression from the command and evaluates it using sympy.
    Returns the result or an error message if the expression is invalid.
    """
    expression = re.search(r"calculate (.+)", command)
    if expression:
        expression = expression.group(1)
        if re.match(r"^[0-9+\-*/.() ]+$", expression):
            try:
                # Use sympify to evaluate the expression
                result = sympify(expression)
                return result
            except SympifyError as e:
                return "Error in calculation: " + str(e)
        else:
            return "Invalid expression"
    else:
        return "No expression found"