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
                          4.press any key to exit''' 
                          )
       
       if user_input == "1":
         self.signup()
       if user_input == "2":
         self.signin()
       if user_input == "3":
         pass
       if user_input == "4":
         pass
       if user_input == "5":
         exit()

    def signup(self):
      email = input("Enter your email here:")
      pwd = input("setup your password here:")
      self.username = email
      self.password = pwd
      print("You have signuped successfully!!")
      self.menu()
    
    def signin(self):
      if self.username == '' and self.password =='':
        print("Please signup first by pressing 1 in the main menu")
      else:
        uname = input("Enter your email/password")
        pwd = input("Enter your password here")
        if self.username ==uname and self.password == pwd:
          print("You have signed in succssfully!!")
          self.loggedin == True
        else:
          print("Please input correct credentials...")
          print("\n")
      self.menu()



    

obj = Chatbook()