from labs.lab1.array_tests import process_file
from labs.lab1.arrays import BitVectorArray

b1 = BitVectorArray(100)   # can store values up to 100
process_file('file0.txt', b1)
b3 = BitVectorArray(10000)  # can store values up to 10000
process_file('file3.txt', b3)