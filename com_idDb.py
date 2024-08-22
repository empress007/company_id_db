
# Assignment
# You have been approach by an organisation to help build a computer that will perform registration duty. Collect firstname, lastname, address, position, and phone-number. The data collected will be needed in the future for other administrative purposes. 
# Write a satisfactory program to meet the requirements.  
# Going forward - generate identification number for each employee
# print("tolu, your id is - 5999jr")

import random
import string
import mysql.connector as mq
myInfo = mq.connect(
        host="localhost",
        port="6925",
        user="root",
        password="Tolulope1",
        database="tee_db",
        auth_plugin='mysql_native_password'
)
myCursor = myInfo.cursor()
# # myCursor.execute("CREATE DATABASE tee_db")
# # myCursor.execute('''
#   # CREATE TABLE Info (
#   #         CustomerId INT PRIMARY KEY AUTO_INCREMENT,
#   #         FirstName VARCHAR(50),  
#   #         LastName VARCHAR (50),
#   #         Address VARCHAR (100), 
#   #         Position VARCHAR (50),
#   #         PhoneNumber VARCHAR (20),
#   #         UniqueId  VARCHAR (50)
#   # )
#   # ''')

# '''Collect information'''
def register_user():
  firstName = input("enter your firstname: ").title().strip()
  global lastName
  lastName = input("enter your lastname: ").title().strip()
  address = input("enter your address: ").title().strip()
  position = input("enter your position: ").upper().strip()
  phoneNo = input("enter your number: ")
  
  letter = random.sample(string.ascii_lowercase,2)
  number = random.sample(string.digits, 4)
  number.extend(letter)
  id = [l.replace("'", '') for l in number]
  # random.shuffle(id)
  generatedId = ''.join(id)
  generatedId =  generatedId 
  
  userexist = f"SELECT * FROM Info WHERE PhoneNumber = '{phoneNo}'"
  # print(f"querying with {phoneNo}")
  myCursor.execute(userexist)
  output = myCursor.fetchone()
  # for inf in output:
  # print(output > 0)
  if output :
    print('user already exist')
  else :
    values_inputs = "INSERT INTO Info (FirstName, LastName, Address, Position, PhoneNumber,UniqueId) VALUES (%s, %s, %s, %s, %s, %s)"
    data = (
            firstName,lastName,address,position,phoneNo,generatedId
            
        )
    myCursor.execute(values_inputs,data)
    myInfo.commit()


def retrieve_id():
    # Retrieve user's ID by their full name
    
    phoneNo = input("Enter your phone number to retrieve your id: ")
    userexist = f"SELECT * FROM Info WHERE PhoneNumber = '{phoneNo}'"
    # print(f"querying with {phoneNo}")
    myCursor.execute(userexist)
    output = myCursor.fetchone()
    # print(output[1])
    print(f"{output[1]} {output[2]}, your ID is - {output[6]}")

def main():
    while True:
        print("\nMenu:")
        print("1. Register User")
        print("2. Retrieve ID")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ").strip()
        
        if choice == '1':
            register_user()
        elif choice == '2':
            retrieve_id()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")
main()