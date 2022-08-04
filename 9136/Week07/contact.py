class Contact:
    def __init__(self, name, organisation, phones = []):
        #write your answer here
        self.name = name
        self.organisation = organisation
        self.phones = phones
        
    def update_name(self, name):
        #write your answer here
        self.name = name
        
    def update_organisation(self,organisation):
         #write your answer here
        self.organisation =  organisation
        
    def match_name(self, substr):
        #write your answer here
        if self.name.lower().startswith(substr.lower()):
            return True
        else:
            return False
    
    def add_phone(self,phone):
        #write your answer here
        if phone in self.phones:
            print("Phone number already exists!")
        else:
            self.phones.append(phone)
    
    def remove_phone(self, index):
        #write your answer here
        if index in range(0,len(self.phones)):
            del self.phones[index]
            return True
        else:
            print("Index out of range")
            return False
        
    def update_phone(self, index, new_phone):
        #write your answer here
        if index in range(0,len(self.phones)):
            self.phones[index] = new_phone
            return True
        else:
            print("Index out of range")
            return False
     
    #__str__(self): This is  the overloaded method that is useful for formatting the output of the contact represented in this Contact class.
    def __str__(self):
        #write your answer here
        formatted_str = "Name: " + self.name+ " Organisation: " + self.organisation + '\nPhone Number/s: '
        for phone in self.phones: # sorted according to keys, e.g., 'phone1','phone2',....
            formatted_str += phone + '\n                ' 
        return formatted_str
      
      
    def __eq__(self, other):
        #write your answer here
        name_self = self.name.lower()
        name_other = other.name.lower()
        org_self = self.organisation.lower()
        org_other = other.organisation.lower()
        if name_self == name_other and org_self == org_other:
            return True
        else:
            return False
      
    def __lt__(self, other):
        #write your answer here
        name_self = self.name.lower()
        name_other = other.name.lower()
        org_self = self.organisation.lower()
        org_other = other.organisation.lower()
        
        if name_self < name_other:
            return True
        elif name_self == name_other:
            if org_self < org_other:
                return True
            else:
                return False
        else:
            return False
        
    def __gt__(self, other):
        #write your answer here
        name_self = self.name.lower()
        name_other = other.name.lower()
        org_self = self.organisation.lower()
        org_other = other.organisation.lower()
        
        if name_self > name_other:
            return True
        elif name_self == name_other:
            if org_self > org_other:
                return True
            else:
                return False
        else:
            return False
            
            
class ExtendedContact(Contact):
    
    def __init__(self, name, organisation, phones = [], email="", address = ""):
        super().__init__(name, organisation, phones)
        self.set_email(email)
        self.set_address(address)
            
        
    def set_address(self, address):
        if self.verify_address(address):
            self.Address = address
        else:
            print("Wrong/Missing Address\nYour address is set as empty\n")
            self.Address = ""
        
    def get_address(self):
        return self.Address
    
    def set_email(self, email):
        self.email = email
        
    def get_email(self):
        return self.email
    
    def verify_address(self, address):
        return address.isalpha()
        
    def __str__(self):
        formatted_str = super().__str__() + "\nEmail: "+ str(self.email)
        formatted_str += "\nAddress: " + str(self.Address) + "\n"
        return formatted_str       