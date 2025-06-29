class Chatbook:
    def __init__(self):
      self.username = ""
      self.password = ""
      self.loggedin = False
      self.menu()




    def menu(self):
       user_input = input('''Welcome to Chatbook. proceed?"
                          1.press 1 to signup
                          2.press 2 to signin
                          3.press 3 to message a friend
                          4.press any key to exit''' )
       
       if user_input == "1":
         pass
       
       


obj = Chatbook()