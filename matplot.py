
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 20, 100)  
print(x)  
plt.plot(x, np.sin(x))       
plt.show()
# import matplotlib.pyplot as plt
# import numpy as np

# import scipy.io as sio;

# #loading data
# mat_contents = sio.loadmat('data.mat')#Ubicacion del archivo