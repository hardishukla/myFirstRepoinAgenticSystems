import numpy as np
data=[10, 20, 30, 40]
m=np.mean(data)
sd=np.std(data)
normal=(data-m)/sd
new = normal.reshape(2,2)
"""Original data: [10 20 30 40]
Mean: 25.0
Standard Deviation: 11.18
Normalized data: [-1.34 -0.45  0.45  1.34]
Reshaped data shape: (2, 2)
"""
print(f"orignal data:{data}\nmean:{m}\nstandard deviation:{sd}\nnormalization data:{normal}\nReshaped data  shape : {new.shape}")