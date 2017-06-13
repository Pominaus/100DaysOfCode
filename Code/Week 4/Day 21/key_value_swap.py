"""
Switching the values and keys in a dictionary of lists. I saw someone ask this 
question on a forum with the dataset found in api_data. I immediately thought 
of lots of reasons you wouldn't do this - the api could change, etc, but then
I thought I'd like to try and find out how it could be done
"""

#sample data set.
api_data =  {
        "ACCESS": ["172.17.110.1", "255.255.255.0"],
        "WAN": ["172.18.165.1", "255.255.255.0"],
        "APP": ["172.19.132.1", "255.255.255.0"],
        "LAN": ["172.19.34.1", "255.255.255.0"],
        "DNS": ["172.12.134.1", "255.255.255.0"]
        }
        
#practice data set with all lists pre-converted to tuples

api_data_tupl =  {
        "ACCESS": ("172.17.110.1", "255.255.255.0"),
        "WAN": ("172.18.165.1", "255.255.255.0"),
        "APP": ("172.19.132.1", "255.255.255.0"),
        "LAN": ("172.19.34.1", "255.255.255.0"),
        "DNS": ("172.12.134.1", "255.255.255.0")
        }
 
def print_dics(dic1, dic2):
    """
    Prints out the two dictionarys in a comparison format. 
    Both dicts are assumed equal length.
    """
    newline = "\n\n"
    pairs = tuple(zip(dic1.items(),dic2.items()))
    print(newline + "Dictionary 1:" + (" " * 65) + 
        "Dictionary 2:")
    for x, y, in pairs:
        space = " " * (40 - len(x[0]) + len(x[1]))
        print(str(x[0]) + ": " + str(x[1]) + space + 
              str(y[0]) + ": " + str(y[1]) + newline)
    print(newline)
    
    
print_dics(api_data, api_data_tupl)
tupl_data = { tuple(value): key for key, value in api_data.items()}
inverted_data = dict(zip(api_data_tupl.values(), api_data_tupl.keys()))
print_dics(tupl_data, inverted_data)
for each in api_data:
    print(inverted_data[api_data_tupl[each]] == each)
