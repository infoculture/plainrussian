import numpy as np
import matplotlib.pyplot as plt

from metric import load_metrics

metrics = load_metrics()
x = []
y = []
for m in metrics:
    if m['grade'] == 5:
        x.append(m['avg_syl'])
        y.append(m['avg_slen'])

N = 50
area = np.pi * (15 * np.random.rand(N))**2 # 0 to 15 point radiuses

plt.scatter(x, y, s=area, alpha=0.5)
plt.show()