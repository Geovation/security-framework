'''
Created on 30 Sep 2019

@author: aymar

'''
industry = input("Select your industry (Defense /Finance /Public Sector /Charity /Services /Other): ")

question_one = input("Is Data central to your business? (Yes/No): ")
question_two = input("Is your business home and office based? (Yes/No): ")
question_three = input("Is the company size greater than 10? (Yes/No): ")

question_four = input("Is your solution a Web app /Mobile app? (Yes/No)")
question_five = input("Do you use Third parties? (Yes/No)")
question_six = input("Is registered users greater than 1000? (Yes/No)")

color = {"Green", "Yellow", "Orange", "Red"}

if industry == "Defense" :
    if question_one == "Yes" and question_two == "Yes" and question_three == "Yes" :
        print(" Your Security risk: Very High")
        print(" Contents of text file to follow to adjust Security posture...\n Could be checklist format\n Could be a game format")
    elif (question_one == "Yes" and question_two == "Yes") or (question_one == "Yes" and question_three == "Yes") :
        print(" Your Security risk: High")
    else :
        print(" Your Security risk: Medium")  
elif industry == "Finance" :
    if question_one == "Yes" and question_two == "Yes" and question_three == "Yes" :
        print(" Your Security risk: Very High")
    elif question_one == "Yes" and question_two == "Yes" :
        print(" Your Security risk: High")
    elif (question_one == "Yes" and question_three == "Yes") or (question_two == "Yes" and question_three == "Yes") or question_one == "Yes" :
        print(" Your Security risk: Medium")
    else :
        print(" Your Security risk: Low")
elif industry == "Public Sector" :
    if (question_one == "Yes" and question_two == "Yes" and question_three == "Yes") or (question_one == "Yes" and question_two == "Yes") :
        print(" Your Security risk: High")
    elif (question_one == "Yes" and question_three == "Yes") or (question_two == "Yes" and question_three == "Yes") or question_one == "Yes" :
        print(" Your Security risk: Medium")
    elif question_two == "Yes" :
        print(" Your Security risk: Low")
    else :
        print(" Your Security risk: Very Low")
elif industry == "Online_Services" :
    if question_one == "Yes" and question_four == "Yes" :
        print(" Your Security risk: High")
    elif (question_one == "Yes" and question_three == "Yes") or (question_four == "Yes" and question_two == "Yes") :
        print(" Your Security risk: Medium")
    else :
        print(" Your Security risk: Very Low")
elif industry == "Charity" :
    if (question_one == "Yes" and question_two == "Yes" and question_three == "Yes") :
        print(" Your Security risk: Medium")
    elif (question_one == "Yes" and question_three == "Yes") or (question_two == "Yes" and question_three == "Yes") or (question_one == "Yes" and question_two == "Yes") :
        print(" Your Security risk: Low")
    else :
        print(" Your Security risk: Very Low")
else:
    print(" This Feature Not implemented yet.\n", "Therefore, Your Security risk: Unclear \n Why not try the 5 Basics Cyber Hygiene Assessment")
