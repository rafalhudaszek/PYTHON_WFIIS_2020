def task_1(l):
    flagThree = True
    flagFour = True
    try:
        if(len(l) < 3):
            raise ValueError
        for i in range(0,len(l)-2):
            a = l[i] * l[i]
            b = l[i+1] * l[i+1]
            c = l[i+2] * l[i+2]
            if (a + b) == c:
                flagThree = False
                even = 0
                notEven = 0
                for j in range(0, 3):
                    if(l[i+j] % 2 == 0):
                        even += 1
                    else:
                        notEven += 1
                print("Pythagorean three:", l[i], l[i+1], l[i+2], ". Even numbers:", even, ". Noteven numbers:", notEven)
        
        for i in range(0,len(l)-3):
            a = l[i] * l[i]
            b = l[i+1] * l[i+1]
            c = l[i+2] * l[i+2]
            d = l[i+3] * l[i+3]
            if (a + b + c) == d:
                flagFour = False
                even = 0
                notEven = 0
                for j in range(0, 3):
                    if(l[i+j] % 2 == 0):
                        even += 1
                    else:
                        notEven += 1
                print("Pythagorean three", l[i], l[i+1], l[i+2], l[i+3], ". Even numbers:", even, ". Noteven numbers:", notEven)
        if flagThree and flagFour:
            raise 
    except ValueError:
        print("tuple is to short")
    except:
        print("tuple doesn't have Pythagorean three/four")


def task_3(fun, xp, xk, n):
    try:
        if type(fun) != type(task_3) or (xk <= xp) or type(n) != type(int(1)):
            raise ValueError
        h =(xk - xp)/(2*n)
        s =(h/3) * sum([fun(x) for x in range(xp, xk, int(h))])
        print(s) 
    except ValueError as ex1:
        print("Wrong data")


def task_2(list, tuple):
    try:
        for i in range(0, len(list)-1):
            if not (list[i] <= list[i+1]) and ((type(list[i]) != type(int(1))) or ((type(list[i]) != type(float(1))))):
                raise ValueError
        for i in range(0, len(tuple)-1):
            if tuple[i] > tuple[i+1] and ((type(tuple[i]) != type(int(1))) or ((type(tuple[i]) != type(float(1))))):
                raise ValueError

        listRange = list[len(list)-1] - list[0]
        if len(list) % 2 == 0:
            listMedian = (list[int(len(list)/2)] + list[int(len(list)/2 + 1)]) / 2
        else:
            listMedian =  list[int(len(list)/2 )]

        tupleRange = tuple[len(list) - 1] - tuple[0]
        if len(tuple) % 2 == 0:
            tupleMedian = (tuple[int(len(tuple)/2)] + tuple[int(len(tuple)/2 + 1)]) / 2
        else:
            tupleMedian =  tuple[int(len(tuple)/2 )]

        print("List, median = ", listMedian, "range = ", listRange)
        print("Tuple, median = ", tupleMedian, "range = ", tupleRange)

    except ValueError as ex1:
        print("Data isn't sorted")
            

task_2([1,3,5,6,7,8], (1,3,5,6,7,8))

#task_3(lambda x: x * x, 0, 100 , 50)
#l=(3,4,5,5,12,13,7,24,25,9,40,41,6,8,10,60,80,100,18,24,30,15,8,17)
#task_1(l)
