class NewString:
    def __init__(self):
        self.msg = ""

    def get_string(self):
        self.msg = input("Enter text: ")

    def print_String(self):
        print(f"{self.msg.upper()}")

str_tester = NewString()
str_tester.get_string()
str_tester.print_String()