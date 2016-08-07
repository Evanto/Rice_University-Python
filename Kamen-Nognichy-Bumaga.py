import random  
  
def number_to_name(number):  
    # fill in your code below  
    if number==0:return "rock"  
    elif number==1:return "Spock"  
    elif number==2:return "paper"  
    elif number==3:return "lizard"  
    elif number==4:return "scissors"  
    else:  
        print('Error! Number is not in the correct range.')  
          
def name_to_number(name):   
    if name=="rock":return 0  
    elif name=="Spock":return 1  
    elif name=="paper":return 2  
    elif name=="lizard":return 3  
    elif name=="scissors":return 4  
    else:  
        print('Error! Name does not match.')  
  
def rpsls(name):    
    player_number=name_to_number(name)  
    comp_number=random.randrange(0,5)  
    difference=(player_number-comp_number)%5  
    if difference==0:results='Player and computer tie!'  
    elif difference>=3:results='Computer wins!'  
    elif difference<=2:results='Player wins!'  
    comp_name=number_to_name(comp_number)  
     
    # print results  
    print("Player chooses "+name)  
    print("Computer chooses "+comp_name)  
    print(results)
    print('\n')  
  
      
# test your code  
rpsls("rock")  
rpsls("Spock")  
rpsls("paper")  
rpsls("lizard")  
rpsls("scissors")  