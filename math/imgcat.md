## imgcat
render matplotlib plots in the terminal (iTerm2 or mintty)

the backend for matplotlib can be set in the environment
to use the imgcat module with `MPLBACKEND="module://imgcat"`

``` python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 6.28, 100)
plt.plot(x, np.sin(x))
plt.show()
```

alternatively send an image to the terminal directly by calling imgcat()
