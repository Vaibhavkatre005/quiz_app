import random as rm
questions=["Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal"]
capital_of_states={
    "Andhra Pradesh": 'Amaravati',
    "Arunachal Pradesh": "Itanagar",
    "Assam": "Dispur",
    "Bihar": "Patna",
    "Chhattisgarh": "Raipur",
    "Goa": "Panaji",
    "Gujarat": "Gandhinagar",
    "Haryana": "Chandigarh",
    "Himachal Pradesh": "Shimla",
    "Jammu and Kashmir": "Srinagar (Summer) Jammu (Winter)",
    "Jharkhand": "Ranchi",
    "Karnataka": "Bengaluru",
    "Kerala": "Thiruvananthapuram",
    "Madhya Pradesh": "Bhopal",
    "Maharashtra": "Mumbai",
    "Manipur": "Imphal",
    "Meghalaya": "Shillong",
    "Mizoram": "Aizawl",
    "Nagaland": "Kohima",
    "Odisha": "Bhubaneswar",
    "Punjab": "Chandigarh",
    "Rajasthan": "Jaipur",
    "Sikkim": "Gangtok",
    "Tamil Nadu": "Chennai",
    "Telangana": "Hyderabad",
    "Tripura": "Agartala",
    "Uttar Pradesh": "Lucknow",
    "Uttarakhand": "Dehradun (Winter) and Gairsain (Summer)",
    "West Bengal": "Kolkata",
}
no_of_questions=5
points=0
for i in range(no_of_questions):
    que_state=rm.choice(questions)
    print('Que.',(i+1),". What is the Capital of",que_state,"?")
    print("\tYour Options are:")
    four_option={}
    ans_pos=rm.randint(0, 3)
    print(ans_pos)

    for n in range(4):
        if n==ans_pos:
            print_option=capital_of_states[que_state]
            print("\t",(n+1),".",print_option)
            currect=n+1
            four_option[currect]=print_option
        else:
            print_option=capital_of_states[rm.choice(questions)]
            print("\t",(n+1),".",print_option)
            four_option[n+1]=print_option
    # try:
    #     ans_state=int(input("Select option from 1 to 4: "))
    # except:
    #     print("Invalid Option Selected")
    ans_state=int(input("Select option from 1 to 4: "))
    print('[Your Selected Answer is', four_option[ans_state] ,"]")
    if four_option[ans_state]==four_option[currect]:
        points=points+1
        print("[Congratulation Your Entered Answer is Correct]\t\t +1 Point")
    else: 
        print("[Sorry Your Entered Answer is Wrong] [Correct Answer: ",four_option[currect],"]\t +0 Point")
    print('\n')
print("*************************************************************************************************************************************")
print("\t\t\t\tTotal Point Score: ",points)
print("*************************************************************************************************************************************")


