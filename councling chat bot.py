print("THIS IS A COUNSELLING CHAT BOT")
print("I'M HERE TO ASK YOU SOME QUESTIONS ABOUT YOUR SELF")
print("ANSWER IN yes OR no")
count = 0
q1 = input("Q1. Do you feel motivated to attend school every day?\n:")
if q1 =="yes":
    print("That's great!")
    count +=2
q2 = input("Q2. Are you able to concentrate well during class?\n:")
if q2 == "yes":
    print("That's great!")
    count +=2
q3 = input("Q3. Do you feel comfortable sharing your thoughts with your teachers?\n:")
if q3 == "yes":
    print("That's great!")
    count +=2
    
q4 = input("Q4. Have you been sleeping well lately?\n:")
if q4 == "yes":
    print("That's great!")
    count +=2
q5 = input("Q5. Do you often feel anxious about your academic performance?\n:")
if q5 == "no":
    print("That's great!")
    count +=2
q6 = input("Q6. Are you satisfied with your current social relationships at school?\n:")
if q6 == "yes":
    print("That's great!")
    count +=2
q7 = input("Q7. Do you find it easy to manage stress?\n:")
if q7 == "yes":
    print("That's great!")
    count +=2
q8 = input("Q8. Do you feel supported by your family in your studies?\n:")
if q8 == "yes":
    print("That's great!")
    count +=2
q9 = input("Q9. Have you felt overwhelmed by schoolwork recently?\n:")
if q9 == "no":
    print("That's great!")
    count +=2
q10 = input("Q10. Do you feel confident in achieving your goals?\n:")
if q10 == "yes":
    print("That's great!")
    count +=2

if count <=16:
    print("YOU HAVE Mentally balanced and motivated.",count)
elif 16>count>9:
    print("YOU HAVE Some areas of concern, but overall balanced.",count)
elif 10>count>4:
    print("YOU HAVE Signs of stress or emotional imbalance.",count)
elif 5>count>0:
    print("YOU HAVE High risk of mental or emotional strain; immediate counseling may be needed.",count)
else:
    print("404 somthing went wrong.")