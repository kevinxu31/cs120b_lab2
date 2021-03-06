# Array of tests to run (in order)
# Each test contains
#   description - 
#   steps - A list of steps to perform, each step can have
#       inputs - A list of tuples for the inputs to apply at that step
#       *time - The time (in ms) to wait before continuing to the next step 
#           and before checking expected values for this step. The time should be a multiple of
#           the period of the system
#       *iterations - The number of clock ticks to wait (periods)
#       expected - The expected value at the end of this step (after the "time" has elapsed.) 
#           If this value is incorrect the test will fail early before completing.
#       * only one of these should be used
#   expected - The expected output (as a list of tuples) at the end of this test
# An example set of tests is shown below. It is important to note that these tests are not "unit tests" in 
# that they are not ran in isolation but in the order shown and the state of the device is not reset or 
# altered in between executions (unless preconditions are used).
tests = [ {'description': 'wa=20,wb=30,wc=40',
    'steps': [ {'inputs': [('PINA', 0x14)],'iterations': 1}, 
        {'inputs': [('PINB',0x1E)], 'iterations': 1 }, 
        {'inputs': [('PINC',0x28)], 'iterations': 1 }, ],
    'expected': [('PORTD',0x58)],},
{'description': 'wa=50,wb=50,wc=50',
    'steps': [ {'inputs': [('PINA', 0x32)],'iterations': 1}, 
        {'inputs': [('PINB',0x32)], 'iterations': 1 }, 
        {'inputs': [('PINC',0x32)], 'iterations': 1 }, ],
    'expected': [('PORTD',0x95)],},
{'description': 'wa=30,wb=50,wc=140',
    'steps': [ {'inputs': [('PINA', 0x1E)],'iterations': 1}, 
        {'inputs': [('PINB',0x32)], 'iterations': 1 }, 
        {'inputs': [('PINC',0x8C)], 'iterations': 1 }, ],
    'expected': [('PORTD',0xDF)],},
{'description': 'wa=10,wb=10,wc=100',
    'steps': [ {'inputs': [('PINA', 0x0A)],'iterations': 1}, 
        {'inputs': [('PINB',0x0A)], 'iterations': 1 }, 
        {'inputs': [('PINC',0x64)], 'iterations': 1 }, ],
    'expected': [('PORTD',0x7A)],},


    ]

# Optionally you can add a set of "watch" variables these need to be global or static and may need
# to be scoped at the function level (for static variables) if there are naming conflicts. The 
# variables listed here will display everytime you hit (and stop at) a breakpoint
#watch = ['<function>::<static-var>','PORTB']

