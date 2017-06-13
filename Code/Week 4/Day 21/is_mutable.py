# Testing if an object is mutable by __hash__ value
tupl = (5,2,5,7,4,2,5,7,3,7)
test = set([1,2,3,4,5,4,54,6,5,6,6])
if (getattr(tupl, "__hash__", False)):
    print("immutable")
else: 
    print("mutable")
    
    
 
