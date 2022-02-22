import random

def gameshow(doors,door_d,user_d):
    count = 0
    for i in door_d[1] :
        if i == user_d[0][0]:
            open =  list(door_d[1].difference(user_d[0]))
            
        else:
            open = random.sample(door_d[1],1)
    
    d = doors
    d.difference(open)
    
    if user_d[1] == 'y':
        d.difference(user_d[0])
        count = 1
    return count


if __name__ == "__main__":
    iter,it = 1000,1000#iteration and its duplicate for finding percentage
    doors = {101,102,103}
    switch_choice  = ['y','n'] 
    switch,stay = 0,0
    while(iter > 0):
        car = random.sample(doors,1)#door with car (list)
        goat =  doors.difference(car)#Doors consisting goat (set)
        
        door_d = [car,goat]#list of door details ( car= int , goat = list)
        
        user_s_door = random.sample(doors,1) #user's 1st choosen door (list)
        select_switch_choice = random.choice(switch_choice) #Want to change your choice y or n 
        
        user_d = [user_s_door,select_switch_choice] #list of user details (user_s_door = int,s_s_c = str) 
        
        switch += gameshow(doors,door_d,user_d)
        iter -= 1
    stay = it - switch
    print("Switch : count {} = {h:.2f}% ".format(switch, h = (switch * (100/it))))
    print("Stay : count {} = {hh:.2f}% ".format(stay, hh = (stay * (100/it)) ))




    
