#หาตัวเลขผสม
q = int(input(""))
if q > 10:
    q = int(input(""))
else:
    n = int(input(""))
check = 0
sum1 = 0
mix_number = [6,9,12,15,18,20,21,24,26,27,29,30]
while q<n:
    q += 1
    #normal case
    if q%mix_number[0]==0:
        sum1 += 1
    elif q%mix_number[1]==0:
        sum1 +=1
    elif q%mix_number[2]==0:
        sum1 +=1
    elif q%mix_number[2]==0:
        sum1 +=1
    elif q%mix_number[3]==0:
        sum1 +=1
    elif q%mix_number[4]==0:
        sum1 +=1
    elif q%mix_number[5]==0:
        sum1 +=1
    elif q%mix_number[6]==0:
        sum1 +=1
    elif q%mix_number[7]==0:
        sum1 +=1
    elif q%mix_number[8]==0:
        sum1 +=1
    elif q%mix_number[9]==0:
        sum1 +=1
    elif q%mix_number[10]==0:
        sum1 +=1
    elif q%mix_number[11]==0:
        sum1 +=1
    #special case
    elif q%mix_number[3]+mix_number[4]==0:
        sum1 +=1
    elif q%mix_number[3]+mix_number[5]==0:
        sum1 +=1
    elif q%mix_number[3]+mix_number[6]==0:
        sum1 +=1
    elif q%mix_number[3]+mix_number[8]==0:
        sum1 +=1
    elif q%mix_number[3]+mix_number[9]==0:
        sum1 +=1
    elif q%mix_number[3]+mix_number[10]==0:
        sum1 +=1
    elif q%mix_number[4]+mix_number[5]==0:
        sum1 +=1
    elif q%mix_number[4]+mix_number[6]==0:
        sum1 +=1
    elif q%mix_number[4]+mix_number[7]==0:
        sum1 +=1
    elif q%mix_number[4]+mix_number[8]==0:
        sum1 +=1
    elif q%mix_number[4]+mix_number[9]==0:
        sum1 +=1
    elif q%mix_number[4]+mix_number[10]==0:
        sum1 +=1
    elif q%mix_number[5]+mix_number[6]==0:
        sum1 +=1
    elif q%mix_number[5]+mix_number[7]==0:
        sum1 +=1
    elif q%mix_number[5]+mix_number[8]==0:
        sum1 +=1
    elif q%mix_number[5]+mix_number[9]==0:
        sum1 +=1
    elif q%mix_number[5]+mix_number[10]==0:
        sum1 +=1
    elif q%mix_number[5]+mix_number[11]==0:
        sum1 +=1
    elif q%mix_number[6]+mix_number[7]==0:
        sum1 +=1
    elif q%mix_number[6]+mix_number[8]==0:
        sum1 +=1
    elif q%mix_number[6]+mix_number[9]==0:
        sum1 +=1
    elif q%mix_number[6]+mix_number[10]==0:
        sum1 +=1
    elif q%mix_number[6]+mix_number[11]==0:
        sum1 +=1
    elif q%mix_number[7]+mix_number[7]==0:
        sum1 +=1
    elif q%mix_number[7]+mix_number[8]==0:
        sum1 +=1
    elif q%mix_number[7]+mix_number[9]==0:
        sum1 +=1
    elif q%mix_number[7]+mix_number[10]==0:
        sum1 +=1
    elif q%mix_number[7]+mix_number[11]==0:
        sum1 +=1
    elif q%mix_number[8]+mix_number[8]==0:
        sum1 +=1
    elif q%mix_number[8]+mix_number[9]==0:
        sum1 +=1
    elif q%mix_number[8]+mix_number[10]==0:
        sum1 +=1
    elif q%mix_number[8]+mix_number[11]==0:
        sum1 +=1
    elif q%mix_number[9]+mix_number[9]==0:
        sum1 +=1
    elif q%mix_number[9]+mix_number[10]==0:
        sum1 +=1
    elif q%mix_number[9]+mix_number[11]==0:
        sum1 +=1
    elif q%mix_number[10]+mix_number[10]==0:
        sum1 +=1
    elif q%mix_number[10]+mix_number[11]==0:
        sum1 +=1
print(sum1)

