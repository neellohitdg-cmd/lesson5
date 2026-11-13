CP=float(input("Cost price:"))
SP=float(input("Selling price:"))
if CP>SP:
    print("you got scammed:LOSS=",CP-SP,"/-")
else:
    print("you are ok np:PROFIT=",SP-CP,"/-")