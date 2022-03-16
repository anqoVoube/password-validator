class PasswordValidator():
    __SPECIAL_SYMBOLS = ['$', '@', '#', '%']
    final_response = {}
    password: str
    
    def __init__(self, password: str):
        self.password = password
    
    def minlength(self, length: int):
        if len(self.password) < length:
            self.final_response = ["Length less than required"]
        return self
    
    def maxlength(self, length: int):
        if len(self.password) > length:
            self.final_response = ["Length greater than permited"]
        return self
    
    def has_uppercase(self):
        if not any(str(char).isupper() for char in self.password):
            self.final_response = ["Password should have at least one uppercase letter"]
        return self
    
    def has_lowercase(self):
        if not any(str(char).islower() for char in self.password):
            self.final_response = ["Password should have at least one lowercase letter"]
        return self
    
    def has_numeral(self):
        if not any(str(char).isdigit() for char in self.password):
            self.final_response = ['Password should have at least one numeral']
        return self
    
    def has_specific_symbol(self):
        if not any(char in self.__SPECIAL_SYMBOLS for char in self.password):
            self.final_response = ['Password should have at least one of those symbols: $@#%']
        return self
    
    def get_response(self) -> dict:
        return self.final_response
 
# a = PasswordValidator("Jujo")
# print(a.minlength(5).has_lowercase().get_response())
# -> ["Password should have at least one uppercase letter"]
