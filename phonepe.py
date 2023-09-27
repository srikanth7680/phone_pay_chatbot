Transaction_issue=input("Do you have any issue  \n 1.Yes \n 2.No \n Enter: ").lower()
if Transaction_issue=="yes":
    help=int(input("Enter your Help \n1.issues with failed payments\n2. having an issue a transaction pending\n3.issues with sucessful pyaments\n Enter :"))
    if help==1:
        failed=int(input("1.Why did my UPI payment fail ?\n2.Why is my money deducted for my failed payment ?\n3.Why is my money not refunded yet ?\n4.where can i find the UTR number for this payment ?\n enter any above option :"))
        if failed==1:
           print("Your UPI payment on Phonepe may have\nfailed due to any one of the below reasons:\n *UPI network issues \n * Wrong UPI PIN \n *Security reasons") 
        elif failed==2:
            print("if your money is detucted from your bank \n account for a failed payment,there is no need \n to worry as your money is absolutely safe with your bank")
        elif failed==3:
            print("if your money is detucted from your bank \n account for a failed payment,there is no need \n to worry as your money is absolutely safe with your bank")
        elif failed==4 :   
            print("1.Tap History on Phone Pe app home screen \n you will see the 12 digit UTRnumber in the Debited from section on the \n screen.")
        else : 
            print("Enter the valid number")
    elif help==2:
        pending=int(input("Enter your opinion \n 1.Why is my UPI payment pending ?\n 2.What do i do if my UPI payment is pending ?\n 3.Why do i have to wait for 48 hours to know the final payment status ?\n 4.How do i cancel my pending payment ?\n 5.What if my payment is pending for more than 48 hours ?\n which is your above problem :"))
        if pending==1:
            print("banks usually complete UPI payments \n instantly.In rare cases, due to technical\n  issues, bank may take additional time to \n deposit the payment money into the \n reciver's account.")
        elif pending==2:
            print("If your UPI payment is pending, you will need \n to wait for 48 hours for your bank to update \n the final status of the payment.")
        elif pending==3:
            print("as per current banking timelines, for pending\n payments , banks can anywhere between \n 2 minutes and 48 hours from the time of payment to to confirm the final status.")   
        elif pending==4:
            print("You can't cancel UPI payment once initiated \n as they are direct bank-to-bank transfers.") 
        elif pending==5:
            print("Banks usually confirm the final payment status within 48 hours from the time you made the payment.")
        else:
            print ("Enter the number")
    elif help==3:
        money_didnot_reach=int(input("Enter your opinoin \n 1.Payments made to a phone number or UPI ID (VPA) \n2.Payment made to a bank account \n Enter the issue :"))
        if money_didnot_reach==1:
           pay_made_to_phone=int(input("Enter your opinion \n 1. what if I've sent money to a Wrong phone number or UPI ID(VPA)?\n 2.what if my payment is successful but the money has not reached the reciver? \n Enter the issue :"))
           if pay_made_to_phone==1:
               print("In the Unfortunate event that you've sent money to a wrong phone number or UPI ID(VPA),We request you to contact your bank directly")
           elif pay_made_to_phone==2:
               print("A payment is marked successful on Phone PE only after we recive a confirmation from thr reciver's bank that the money has reached them.")
           else:
               print("Enter the valid Number")
        elif money_didnot_reach==2:
            pay_made_to_bank=int(input("Enter your opinoin \n 1.What if i have sent money to wrong bank account?\n 2.Why do bank take upto 5 days to deposite the money ?"))
            if pay_made_to_bank==1:
                print("In the Unfortunate event that you've sent money to a wrong phone number or UPI ID(VPA),We request you to contact your bank directly and raise a wrong credit chargeback with (UTR)")
            elif pay_made_to_bank==2:
                print("Bank usally deposite the money for UPI payments instantly")  
            else:
                print("Enter the valid number")  
    else :
        print("enter the valid number")  
elif Transaction_issue=="no" :
    print("Thank you for your concern")     
else :
    print("Enter the valid number")