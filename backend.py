class bank:
    
    
    def __init__(self,bal=0, msg = []):
        self.bal = bal
        self.msg = msg
        
        
    def deposit(self,dep):
        self.bal += dep
        self.msg += [f"{dep} deposit successfully ({self.bal})"]
        return self.msg[-1]
    
    def withdraw(self,wit):
        
        if wit <= self.bal:
            self.bal -=wit
            self.msg += [f" {wit} withdraw successfully ({self.bal})"]
            return self.msg[-1]
        else :
            self.msg += [f"You Have not sufficient money {self.bal}"]
            return self.msg[-1]
    
    def balance(self):
        return f"{self.bal} net"
    
    
    def view(self):
        return self.msg