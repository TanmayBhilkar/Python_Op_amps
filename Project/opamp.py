"create class Opamp"
class opamp:


    "these are different types of Opamps function"
    def inv_opamp(self):
        print((Rf/Rin)*Vin)
    def n_inv_opamp(self):
        print(1+(Rf/Rin)*Vin)
    def diff_opamp(self):
        print((Rf/Rin)*(Vin-V1))
    def sum_opamp(self):
        print((Rf/Rin)*(Vin+V1))
    def vol_foll(self):
        print(Vin*V1)


Rf = int(input("Enter Rf  in ohm:"))
Rin = int(input("Enter Rin  in ohm:"))
Vin= int(input("Enter Vin  in ohm:"))
V1 = int(input("Enter V1  in ohm:"))

"create a Opamp object"
obj = opamp()

"Make sure the user have entered the valid choice"
Choice = 1
while Choice != 0:
    print("1. INV")
    print("2. NINV")
    print("3. DIFF")
    print("4. SUMM")
    print("5. VOl_Foll")
    print("6. Exit")

    Choice = int(input("Enter your choice:"))
    if Choice == 1:
        print(obj.inv_opamp())
    elif Choice == 2:
        print(obj.n_inv_opamp())
    elif Choice == 3:
        print(obj.diff_opamp())
    elif Choice == 4:
        print(obj.sum_opamp())
    elif Choice == 5:
        print(obj.vol_foll())
    elif Choice == 6:
        print("you want to exit")
        Choice == 0
    else:
        print("Invalid choice")
        