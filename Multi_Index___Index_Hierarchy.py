import pandas as pd
import numpy as np

inside = ['Class A', 'Class B', 'Class C', 'Class A', 'Class B', 'Class C']
outside = ['School 1', 'School 1', 'School 1', 'School 2', 'School 2', 'School 2']

zip(outside, inside)
multi_index = list(zip(outside, inside))

print(multi_index)
     
hier_index = pd.MultiIndex.from_tuples(multi_index)
print(hier_index) 

np.random.seed(101)
df = pd.DataFrame(np.random.randint(70, 100, size = (6,2)), index = hier_index, 
                  columns = ['1st Semester', '2nd Semester'])
print(df)

