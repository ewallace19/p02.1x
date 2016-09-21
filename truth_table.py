"""
Problem:

    A truth table is used to demonstrate how an individual logic gate, or a
    whole system of gates, reacts to different inputs.

    A system of gates takes three inputs: a, b and c.  The output for each
    combination of inputs is shown in the table below:

        a       b       c        Output
      ==================================
        0       0       0           0
        0       0       1           1
        0       1       0           1
        0       1       1           0
        1       0       0           1
        1       0       1           0
        1       1       0           0
        1       1       1           1

    The function truth_table takes in three inputs: a, b and c and should
    print the relevant output.

    Try to minimise the number of if statements necessary.

Tests:

    >>> truth_table(0, 0, 0)
    0
    >>> truth_table(0, 0, 1)
    1
    >>> truth_table(0, 1, 0)
    1
    >>> truth_table(0, 1, 1)
    0
    >>> truth_table(1, 0, 0)
    1
    >>> truth_table(1, 0, 1)
    0
    >>> truth_table(1, 1, 0)
    0
    >>> truth_table(1, 1, 1)
    1

"""

# Use this to test your solution. Don't edit it!   
import doctest   
def run_tests():   
    doctest.testmod(verbose=True)   


# Edit this function
def truth_table(a, b, c):

