import pandas as  pd 
reading_data = pd.read_csv('/home/nineleaps/Downloads/MySQL/Scaler_data/Scaler_Data.csv')                                                                                             
results = {}

for row_no, col in reading_data.iterrows(): # The iterrows function of the DataFrame is used 
                                            # to iterate through each row as a tuple of the 
                                            # row index and the row data.
    if col['id'] not in results:
        results[col['id']] = {}
    if(col['scalar'] in results[col['id']]):
        results[col['id']][col['scalar']] += col['data']
    else:
        results[col['id']][col['scalar']] = col['data']
        
print(results)

for i,j in results.items(): # items() is a built-in method in Python that is used to return 
                            # a list of tuples, where each tuple contains a key-value pair 
                            # from a given dictionary.
    print(i,j)
    
    