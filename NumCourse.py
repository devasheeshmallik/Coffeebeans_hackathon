def course_analysis(numCourse,prerequisites):
    out = True
    for i in prerequisites:
        if i[0] == i[1]:
            print("False")
            quit()
    for i in range(len(prerequisites)):
        for j in range(len(prerequisites)):
            if i != j and (prerequisites[i][0] == prerequisites[j][1]) and (prerequisites[i][1] == prerequisites[j][0]):
                print("False")
                quit()
    print(out)
 
if __name__ == '__main__':
    numCourse = int(input("Enter NumCourse : ")) 
    n = int(input("Enter the number of prerequisites: "))
    print("Enter prerequisites seperated by space")
    prerequisites = [input().split() for _ in range(n)]
    print("\nOutput")
    course_analysis(numCourse,prerequisites)
