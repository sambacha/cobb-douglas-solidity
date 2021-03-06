import decimal
import json
import matplotlib.pyplot as plt
import math
import os.path

decimal.getcontext().prec = 128

def get_native_error(x):
    actual = decimal.Decimal(math.log(float(x)))
    expected = decimal.Decimal(float(x)).ln()
    return float(abs(expected - actual))

DATA_FILE = os.path.normpath(os.path.join(os.path.dirname(__file__), '../data/ln.json'))
with open(DATA_FILE) as f:
    data = json.loads(f.read())

data = sorted(data, key=lambda d: float(d['input']))
max_error = max(d['error'] for d in data)
min_error = min(d['error'] for d in data)
print(f'error range: [{min_error}, {max_error}]')

plt.plot(
    [float(d['input']) for d in data],
    [get_native_error(d['input']) for d in data],
    label='math.log() (native)',
    alpha=0.33
)
plt.plot(
    [float(d['input']) for d in data],
    [d['error'] for d in data], label='FixedMath.ln()',
)
plt.yscale('log')
plt.ylabel('ln(x) error (log scale)')
plt.xlabel('input x')
plt.title(f'ln(x) absolute error')
plt.legend()
plt.show()
