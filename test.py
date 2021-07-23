def f(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return 9*f(n - 1) - 7*f(n - 2)

def is_part_of_series(list):
    found=False
    not_found=False
    for i in list:
        for j in range(6):
            if i==f(j):
                ch=1
                break
            else:
                ch=0
        if ch==1:
            found=True
        if ch==0:
            not_found=True
    if found==True and not_found==False:
        print(list,"-> this list is part of the series.")
    else:
        print(list,"-> this list is not a part of the series.")


is_part_of_series((0,1,9,603,4909))
is_part_of_series((0,1,9,603,4909,500))