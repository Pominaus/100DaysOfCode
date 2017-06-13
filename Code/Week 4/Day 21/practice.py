#This was a practice file for creating my formatted printing function


#sample data set.
dic1 =  {
        "ACCESS": ["172.17.110.1", "255.255.255.0"],
        "WAN": ["172.18.165.1", "255.255.255.0"],
        "APP": ["172.19.132.1", "255.255.255.0"],
        "LAN": ["172.19.34.1", "255.255.255.0"],
        "DNS": ["172.12.134.1", "255.255.255.0"]
        }
        
#practice data set with all lists pre-converted to tuples

dic2 =  {
        "ACCESS": ("172.17.110.1", "255.255.255.0"),
        "WAN": ("172.18.165.1", "255.255.255.0"),
        "APP": ("172.19.132.1", "255.255.255.0"),
        "LAN": ("172.19.34.1", "255.255.255.0"),
        "DNS": ("172.12.134.1", "255.255.255.0")
        }
 

pairs = tuple(zip(dic1.items(),dic2.items()))
newline = "\n\n"
print(pairs)
print(line_return)
for x, y, in pairs:
    space = " " * (40 - len(x[0]) + len(x[1]))
    print(str(x[0]) + ": " + str(x[1]) + space + 
          str(y[0]) + ": " + str(y[1]) + newline)

