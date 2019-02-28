"""
Sample Akumen Python Model

Important sections of this are noted with !!'s.
"""

# !! Python runs 'headless' in Akumen. Thus, use a non-interactive backend such as 'Agg'.
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def akumen(first, second, **kwargs):
    """
    !! This akumen() function must exist in the execution file!

    Parameters:
        !! These lines define parameters, and a line must exist per input (or output).

        - Input: first [float]
        - Input: second [float]

        - Output: first_result [float]
        - Output: second_result [float]
    """
    print('Running Akumen model...')

    # Our model code goes here (including any calls to other functions, modules or libraries)
    first_result = first + second
    second_result = first - second

    # Images can be viewed through the Research Grid, if they are saved to outputs.
    plt.hist([first, second, first_result, second_result])
    plt.savefig('outputs/example.png')

    # The akumen() function must return a dictionary including keys relating to outputs.
    return {
        'first_result': first_result,
        'second_result': second_result
    }


if __name__ == '__main__':
    """
    Any local test code can be used in an import guard
    when developing on a local machine, you can put code here that won't
    get run by Akumen.
    """
    print('Running local tests...')
    assert (akumen(1, 2)['first_result'] == 3)
    assert (akumen(3, 4)['second_result'] == -1)
    print('Tests completed!')
