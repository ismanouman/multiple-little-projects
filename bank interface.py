                                        # bank account interface

class bank:
    def imp_details(self,name,email,adress):
        self.name=name
        self.email=email
        self.adress=adress
        print("imp_details")
        print("name:",self.name)
        print("email:",self.email)
        print("adress:",self.adress)
class account(bank):
    def hidden_details(self,CNIC,ph_no):
        self.CNIC=CNIC
        self.ph_no=ph_no
        print("hidden details")
        print("CNIC:",self.CNIC,"ph_no:",self.ph_no)
    
A=account()
A.imp_details("Isma","isma@gmail","multan city")

