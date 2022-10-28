from model.user import User
from lib.helper import user_data_path


class Admin(User):
    """
    3.2.2 Admin class
    1. constructor. This method has five positional arguments:
    uid(int, default value is -1),username(str, default value is “”),
    password(str, default value is “”),
    register_time(str, default value is “yyyy-MM-dd_HH:mm:ss.SSS”)
    and role(int,default value is “admin”)
    """

    def __init__(self, uid=-1, username="", password="", register_time="yyyy-MM-dd_HH:mm:ss.SSS", role="admin"):
        User.__init__(self, uid, username, password, register_time, role)

    """
    3. register_admin() no return.
    This method will create a new admin account and write this 
    account into the user.txt file. This method does not need to call the 
    register method implemented in the User class. And, no validation required 
    for the admin account. The default username and password can be any value 
    predefined by yourself. For example, username=”admin”, password=”admin”. 
    Admin account cannot be registered via frontend webpages
    """

    def register_admin(self):
        uid = str(self.generate_unique_user_id())
        username = "admin"
        password = "admin"
        password = self.encrypt_password(password)

        text = ';;;'.join([uid, username, password,
                           self.register_time, self.role])

        user_file = open("data/temp_admin.txt", "w", encoding='utf-8')
        user_file.write(f'{text}\n')
        user_file.close()
        User().txt_merge()

    """
    2. __str__()->str.
    Return string format example:
    285108;;;aaaaa;;;**a****a****a****a****a**;;;2021-11-29 32:32:28.590;;;admin
    """

    def __str__(self):
        text = ';;;'.join([self.uid, self.username, self.password,
                           self.register_time, self.role])
        return text
