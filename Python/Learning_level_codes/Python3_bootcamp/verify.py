import re
class Verify:
            
    """
    1. pass email id and phone number as kwargs OR
    2. pass first argument as email id and second as phone number OR
    3. if you leave both value as null , any verification method will return null
    4.If phone number.email id is valid, respective method will return true
      Else false
     """
    def __init__(self,email_id=None,phone_number=None):
        self.email_id = '' if email_id==None else str(email_id)
        self.ph_no = '' if phone_number==None else str(phone_number)
    def verifyPhone(self):
        if(re.findall('\d{3}-\d{3}-\d{4}',self.ph_no)==self.ph_no):
            return True
        return False
    def verifyEmail(self):
           if(re.findall('[a-zA-Z0-9+_\-.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$',self.email_id)==self.email_id):
            return True
           return False
        
