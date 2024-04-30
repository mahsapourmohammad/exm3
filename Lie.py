from random import choice

def find_thief(a1, a2, a3, b1, b2, b3, c1, c2, c3, d1, d2, d3):

    #A
    if c1 is True:
        a1= False
    if b3 is False:
        a2= True
    if a3 is False:
        a3= True

    #B
    if d1 is False:
        b1= True
    if d3 is True:
        b2= False
    if a2 is True:
        b3= False
    #C
    if a1 is True:
        c1= False
    if c2 is False:
        c2= True
    if d2 is True:
        c3= False
    #D
    if b1 is True:
        d1= False
    if c3 is False:
        d2= True
        d3= True

    suspects = ['A', 'B', 'C', 'D']
    thief = None
    for i , suspect in enumerate([a3, b1, c1, d1]):
        if not suspect:
            thief = suspects[i]
            break
    print(f'thief is : {thief}')

    suspect_list = [a1, a2, a3, b1, b2, b3, c1, c2, c3, d1, d2, d3]
    true_count = suspect_list.count(True)
    false_count = suspect_list.count(False)
    
    
    while true_count != 6 or false_count != 6:
        for i in range(len(suspect_list)):
            if true_count > 6 and suspect_list[i] is True:
                suspect_list[i] = False
                true_count -= 1
                false_count += 1
            elif false_count > 6 and suspect_list[i] is False:
                suspect_list[i] = True
                false_count -= 1
                true_count += 1
                

    a1, a2, a3, b1, b2, b3, c1, c2, c3, d1, d2, d3 = suspect_list
    
    print(f"truth={true_count}, lie={false_count}")
    print(a1,a2,a3,b1,b2,b3,c1,c2,c3,d1,d2,d3)

a1 = choice([True, False])
a2 = choice([True, False])
a3 = choice([True, False])
b1 = False  
b2 = choice([True, False])
b3 = choice([True, False])
c1 = choice([True, False])
c2 = choice([True, False])
c3 = choice([True, False])
d1 = True  
d2 = choice([True, False])
d3 = choice([True, False])

find_thief(a1, a2, a3, b1, b2, b3, c1, c2, c3, d1, d2, d3)
   