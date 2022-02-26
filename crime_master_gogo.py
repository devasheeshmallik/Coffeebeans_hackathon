occupied,empty = 1,2
unknown = 0 
pos = [[[0 for col in range(50)] for col in range(50)] for row in range(50)]

W_H_T = []
ti_Li_Ti_Ri_Bi =[[]]

def solve(x,y,time):
    if x <1 or y<1 or x > W_H_T[0] or y > W_H_T[1]:
        return occupied
    if pos[x][y][time] != unknown:
        return pos[x][y][time]
    if time == 1 :
        pos[x][y][time] = empty
        return empty

    a = solve(x,y,time-1)
    b = solve(x-1,y,time-1)
    c = solve(x+1,y,time-1)
    d = solve(x,y-1,time-1)
    e = solve(x,y+1,time-1)

    if a == empty or b == empty or c == empty or d == empty or e == empty:
        pos[x][y][time] = empty
    else:
        pos[x][y][time] = occupied
    
    return pos[x][y][time]



if __name__ == "__main__":
    c = 0
    
    while True:
        wht = input().split()

        for i in range(len(wht)):

            W_H_T.append(int(wht[i]))

        
        if int(W_H_T[0]) == 0:
            quit()
        c+=1

        for i in range(W_H_T[0]):
            for j in range((W_H_T[1])):
                for k in range((W_H_T[2])):
                    pos[i][j][k]= unknown
        
        
        n = int(input())
        for i in range(n):
            temp = list(map(int, input().split()))
            
        
           
        #print("ti_Li_Ti_Ri_Bi : ",ti_Li_Ti_Ri_Bi)
            for a in range(temp[1],temp[3]+1):
                for b in range(temp[2],temp[4]+1):
                    pos[a][b][temp[0]] = occupied
            ti_Li_Ti_Ri_Bi.append(temp)
        ok =0
        w = W_H_T[0]+1
        h = W_H_T[1]+1
        for i in range(1,w):
            for j in range(1,h):
                if solve(i,j,W_H_T[2]) == empty :
                    ok =1 
        print("Robbery #{}:".format(c))
        if not(ok):
           print("Robber has escaped")
        else:
            ok = 0
            ti = W_H_T[2]+1
            for i in range(1,ti):
                x = 0
                y = 0
                wi = W_H_T[0]+1
                hi = W_H_T[1]+1
                for j in range(1,wi):
                    for k in range(1,hi):
                        if pos[j][k][i] == empty:
                            if x == 0 and y == 0:
                                x =j
                                y =k
                            else:
                                x = -1
                                y = -1
                if x > 0 and y > 0:
                    ok = 1
                    print("Time step {} : The robber has been at ({},{})".format(i,x,y))
            if ok == 0:
                print("Nothing known.\n ")
            
