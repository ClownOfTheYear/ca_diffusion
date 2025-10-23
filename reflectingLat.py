import numpy as np

def reflectingLat(lat):
    result = np.zeros((lat.shape[0]+2, lat.shape[1]+2))
    result[1:-1, 1:-1] = lat[:, :]
    result[1:-1, 1:-1] = lat[:, :]
    
    result[0, :] = result[1, :]
    result[-1, :] = result[-2, :]
    result[:, 0] = result[:, 1]
    result[:, -1] = result[:, -2]
    
    return result


test1 = np.arange(6)
test1 = np.reshape(test1, (2,3))

print(test1)

test2 = reflectingLat(test1)
print(test2)