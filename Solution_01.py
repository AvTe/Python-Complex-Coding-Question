# Answer 1: #program which will find all such numbers which are divisible by 7 
# # but are not a multiple of 5, between 2000 and 320

nl=[]
for x in range(1500, 2701):
    if (x%7==0) and (x%5==0):
        nl.append(str(x))
print (','.join(nl))
