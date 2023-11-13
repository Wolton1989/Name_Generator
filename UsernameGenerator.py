from xml.dom import UserDataHandler

#function to take all the necessary details from the user in 
#order to generate username
def user_details():
    #it should take use first name
    first_name=input("Insert your first name\n").lower()
    #its checks if the first name has a number
    while(any(r.isdigit() for r in first_name)):
        print("Invalid first name")
        first_name=input("Insert your first name\n").lower()
    while first_name=='':
        print("Invalid first name")
        first_name=input("Insert your first\n").lower()
    #its should accept last name
    last_name=input("Insert your last name\n").lower()
    #check if there is numbers in last name and accept
    while(any(r.isdigit() for r in last_name)):
        print("Invalid last name")
        last_name=input("Insert your last name\n").lower()
    #accept cohort from user
    cohort=int(input("Insert your cohort\n"))
    #if cohort value is invalid it should accept
    while(cohort<2022):
        print("Invalid cohort:")
        cohort=int(input("Insert your cohort\n"))
    
    #aaccept campus value from the user
    final_campus=input("Insert the campus you will be attending in\n")
    #if campus name is not valid then take it again
    while user_campus(final_campus)==-8:
        print("Invalid campus")
        final_campus=input("Insert the campus you will be attending in\n")
    
    #show user name
    print(create_user_name(first_name,last_name ,cohort,final_campus))
    
    

#it should generate user name and data 
def create_user_name(first_name, last_name, cohort, final_campus):
    user_name=""
    if(len(first_name)==1):
         user_name=user_name+first_name[:]+'oo'
    if(len(first_name)<3):
        user_name=user_name+first_name[:]+'o'
    elif(len(first_name)>=3):
        user_name=user_name+first_name[-3:]
    
    if(len(last_name)==1):
        user_name=user_name+last_name[:]+'oo'
    if(len(last_name)<3):
        user_name=user_name+last_name[:]+'o'
    elif(len(last_name)>=3):
        user_name=user_name+last_name[0:3]
    
    user_name=user_name+str(cohort)
    user_name=user_name.lower()+user_campus(final_campus)
    return user_name
        
#method to check if the campus if valid 
#it should return campus call 
def user_campus(campus):
    campus_list={'Johannesburg':'JHB', 'Cape Town':'CPT',
        'Durban':'DBN','Phokeng':'PHO','johannesburg':'JHB', 'cape town':'CPT', 'durban': 'DBN', 'phokeng': 'PHO'
    }
    if campus not in campus_list.keys():
        return -8
    return campus_list[campus]


#the out come
if __name__=='__main__':
    user_details()

