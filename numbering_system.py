class numbering_systems:

    # convert decimal to binary
    def decimal_binary(self):
        self.num = int(input("Enter decimal number : "))
        self.binary = bin(self.num)
        # print(self.binary)
        print(f"Binary of decimal number {self.num} is: {self.binary}")

    # convert decimalto hexadecimal
    def decimal_hexadecimal(self):
        self.num = int(input("Enter decimal number : "))
        self.hexa = hex(self.num)
        # print(self.hexa)
        print(f"Hexadecimal of decimal number {self.num} is: {self.hexa}")

    # convert decimal to octal
    def decimal_octal(self):
        self.num = int(input("Enter decimal number : "))
        self.octa = oct(self.num)
        # print(self.octa)
        print(f"Octal of decimal number {self.num} is: {self.octa}")

    # covert hexadecimal to decimal
    def hexadecimal_decimal(self):
        self.hexadecimal = input("Enter hexadecimal number : ")
        self.decimal = int(self.hexadecimal, base=16)
        # print(self.decimal)
        print(f"Decimal of hexadecimal number {self.hexadecimal} is: {self.decimal}")

    # covert binary to decimal
    def binary_decimal(self):
        self.binary = input("Enter binary number : ")
        self.decimal = int(self.binary, base=2)
        # print(self.decimal)
        print(f"Decimal of binary number {self.binary} is: {self.decimal}")

    # convert octal to decimal
    def octal_decimal(self):
        self.octal = input("Enter octal number : ")
        self.decimal = int(self.octal, base=8)
        # print(self.decimal)
        print(f"Decimal of octal hexadecimal number {self.octal} is: {self.decimal}")

    # convert binary to octal
    def binary_octal(self):
        self.bin_string = input("Enter binary number : ")
        self.bin_integer = int(self.bin_string, 2)
        self.oct_string = oct(self.bin_integer)
        # print(self.oct_string)
        print(f"Octal of binary number {self.bin_string} is: {self.oct_string}")

    # convert octal to binary
    def octal_binary(self):
        self.oct_string = input("Enter octal number : ")
        self.oct_integer = int(self.oct_string, 8)
        self.binary_string = format(self.oct_integer, 'b')
        # print(self.binary_string)
        print(f"Binary of oct number {self.oct_string} is: {self.binary_string}")

    # convert hexadecimal to binary
    def hexadecimal_binary(self):
        self.hex_string = input("Enter hexadecimal number : ")
        self.hex_integer = int(self.hex_string, 16)
        self.binary_string = format(self.hex_integer, 'b')
        # print(self.binary_string)
        print(f"Binary of hexadecimal number {self.hex_string} is: {self.binary_string}")

    # convert binary to hexadecimal
    def binary_hexadecimal(self):
        self.bin_string = input("Enter binary number : ")
        self.bin_integer = int(self.bin_string, 2)
        self.hexa_string = hex(self.bin_integer)
        # print(self.hexa_string)
        print(f"Hexadecimal of binary number {self.bin_string} is: {self.hexa_string}")

    # convert octal to hexadecimal
    def octal_hexadecimal(self):
        self.octal_string = input("Enter octal number : ")
        self.octal_integer = int(self.octal_string, 8)
        self.hexa_string = hex(self.octal_integer)
        # print(self.hexa_string)
        print(f"hexadecimal of octal number {self.octal_string} is: {self.hexa_string}")

    # convert hexadecimal to octal
    def hexadecimal_octal(self):
        self.hexa_string = input("Enter hexadecimal number : ")
        self.hexa_integer = int(self.hexa_string, 16)
        self.oct_string = oct(self.hexa_integer)
        # print(self.oct_string)
        print(f"Octal of hexadecimal number {self.hexa_string} is: {self.octal_string}")


    # choice any converter in class used number of choice
    def choice_convert(self):
        while True:
            print('0. exit program')
            print('1. convert decimal to binary')
            print('2. convert decimal to hexadecimal')
            print('3. convert decimal to octal')
            print('4. convert hexadecimal to decimal')
            print('5. convert binary to decimal')
            print('6. convert octal to decimal')
            print('7. convert binary to octal')
            print('8. convert octal to binary')
            print('9. convert hexadecimal to binary')
            print('10.convert binary to hexadecimal')
            print('11.convert octal to hexadecimal')
            print('12.convert hexadecimal to octal')

            self.number = int(input("please enter number of choice : "))

            if self.number == 1:
                self.decimal_binary()
            elif self.number == 2:
                self.decimal_hexadecimal()
            elif self.number == 3:
                self.decimal_octal()
            elif self.number == 4:
                self.hexadecimal_decimal()
            elif self.number == 5:
                self.binary_decimal()
            elif self.number == 6:
                self.octal_decimal()
            elif self.number == 7:
                self.binary_octal()
            elif self.number == 8:
                self.octal_binary()
            elif self.number == 9:
                self.hexadecimal_binary()
            elif self.number == 10:
                self.binary_hexadecimal()
            elif self.number == 11:
                self.octal_hexadecimal()
            elif self.number == 12:
                self.hexadecimal_octal()
            elif self.number == 0:
                break
            else:
                print('Error input')




nums = numbering_systems()
nums.choice_convert()


# if __name__ == "__main__":
#     nums = numbering_systems()
#     nums.choice_convert()

