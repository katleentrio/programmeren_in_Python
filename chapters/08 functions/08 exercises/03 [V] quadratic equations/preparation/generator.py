import os
import sys
import importlib
import random

# set fixed seed for generating test cases
random.seed(123456789)

# locate evaldir
evaldir = os.path.join('..', 'evaluation')
if not os.path.exists(evaldir):
    os.makedirs(evaldir)

# locate solutiondir
solutiondir = os.path.join('..', 'solution')
if not os.path.exists(solutiondir):
    os.makedirs(solutiondir)

# load functionality defined in sample solution
module_name = 'solution'
file_path = os.path.join(solutiondir, 'solution.en.py')
spec = importlib.util.spec_from_file_location(module_name, file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

for name in dir(module):
    if not (name.startswith('__') and name.endswith('__')):
        globals()[name] = eval(f'module.{name}')

# generate test data for functions discriminant and solutions
cases = [
    (1, 0, -1),
    (1, 4, -5),
]
while len(cases) < 50:
    a = random.randint(-10, 10)
    while not a:
        a = random.randint(-10, 10)
    b = random.randint(-10, 10)
    c = random.randint(-10, 10)
    parameters = (a, b, c)
    if parameters not in cases:
        cases.append(parameters)

# generate unit tests for functions discriminant and solutions
functions = [discriminant, solutions]
for index, func in enumerate(functions):
    sys.stdout = open(os.path.join('..', 'evaluation', f'{index}.in'), 'w', encoding='utf-8')
    for a, b, c in cases:

        # generate test expression
        print(f'>>> {func.__name__}({a}, {b}, {c})')

        # generate return value
        try:
            print(f'{func(a, b, c)}')
        except Exception as e:
            print('Traceback (most recent call last):\n{}: {}'.format(e.__class__.__name__, e))

        print()
