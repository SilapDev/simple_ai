import numpy as np
from sklearn import preprocessing


input_Data = np.array([[5.1, -2.9, 3.3], [-1.2, 7.8, -6.1],[3.9, 0.4, 2.1],
[7.3, -9.9, 4.5]])

data_binarized = preprocessing.Binarizer(threshold=2.1).transform(input_Data)

print(f"binarized data: {data_binarized}")

# Вывод среднего значения и стандартного отклонение

print("Before")
print("mean =", input_Data.mean(axis=0))
print(" std deviation= ", input_Data.std(axis=0))

data_scaled = preprocessing.scale(input_Data)

print("After")
print("Mean=", data_binarized.mean(axis=0))