"create class Opamp"
class Opamp:


    "this is Inverting Opamp function"
    def INV(self):
        print((Rf/Rin)*Vin)

    "this is NON-Inverting Opamp function"
    def NINV(self):
        print(1+(Rf/Rin)*Vin)

    "this is Differntiator Opamp function"

    def DIFF(self):
        print((Rf/Rin)*(Vin-V1))

    "this is Summing Opamp function"
    def SUMM(self):
        print((Rf/Rin)*(Vin+C))

"Parameters used in desigining to the Amplifier"


Rf = int(input("Enter Rf  in ohm:"))
Rin = int(input("Enter Rin  in ohm:"))
Vin= int(input("Enter Vin  in ohm:"))
V1 = int(input("Enter V1  in ohm:"))

"create a Opamp object"
obj = Opamp()

"Make sure the user have entered the valid choice"
choice = 1

while choice != 0:
    print("1. INV")
    print("2. NINV")
    print("3. DIFF")
    print("4. SUMM")

    "choices According to the Function choice"

    choice = int(input("Enter your choice:"))
    if choice == 1:
        print(obj.INV())
    elif choice == 2:
        print(obj.NINV())
    elif choice == 3:
        print(obj.DIFF())
    elif choice == 4:
        print(obj.SUMM())
    else:
        print("Invalid choice")

if __name__ == '__main__':
    main()