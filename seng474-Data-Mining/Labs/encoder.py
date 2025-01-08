import sys
import math

dict = {}
def main():
    decode(sys.argv[1])
    print_dict()
    

def decode(l):
    with open(l, 'r') as file_list:
        for line in file_list:
            l = line.strip().split('\n')
            for m in l:
                sub_m = m.split(',')
                #print(sub_m[0])
                k = int(sub_m[0])
                v = [sub_m[1],sub_m[2],sub_m[3],sub_m[4]]
                #print(k,v)
                #if(cumulative_sum(k) == True):
                dict[k] = v
    return dict

def print_dict():
    firstY = 0
    firstN = 0 
    secondY = 0
    secondN = 0
    thirdY = 0
    thirdN = 0
    crewY = 0
    crewN=0
    adultY=0
    adultN=0
    childY=0
    childN=0
    maleY=0
    maleN=0
    femaleY=0
    femaleN=0
    #for key,value in sorted(dict.items()):
        #print(key,value)
    #here we will count everything required
    print("------1st pclass----")
    for key,value in sorted(dict.items()):
        if(value[0] =='1st' and value[3] == 'yes'):
            firstY += 1
        if(value[0] =='1st' and value[3] == 'no'):
            firstN += 1
        if(value[0] =='2nd' and value[3] == 'yes'):
            secondY +=  1
        if(value[0] =='2nd' and value[3] == 'no'):
            secondN += 1
        if(value[0] =='3rd' and value[3] == 'yes'):
            thirdY +=  1
        if(value[0] =='3rd' and value[3] == 'no'):
            thirdN += 1
        if(value[0] =='crew' and value[3] == 'yes'):
            crewY +=  1
        if(value[0] =='crew' and value[3] == 'no'):
            crewN += 1
        if(value[1] =='adult' and value[3] == 'yes'):
            adultY += 1
        if(value[1] =='adult' and value[3] == 'no'):
            adultN += 1
        if(value[1] =='child' and value[3] == 'yes'):
            childY += 1
        if(value[1] =='child' and value[3] == 'no'):
            childN += 1
        if(value[2] =='male' and value[3] == 'yes'):
            maleY += 1
        if(value[2] =='male' and value[3] == 'no'):
            maleN += 1
        if(value[2] =='female' and value[3] == 'yes'):
            femaleY+= 1
        if(value[2] =='female' and value[3] == 'no'):
            femaleN += 1

    
    
    
    print(firstY,firstN)
    print(secondY,secondN)
    print(thirdY,thirdN)
    print(crewY,crewN)
    print(adultY,adultN)
    print(childY,childN)
    print(maleY,maleN)
    print(femaleY,femaleN)

    print(firstY+firstN+secondY+secondN+thirdY+thirdN+crewY+crewN)


    firstY = 0
    firstN = 0 
    secondY = 0
    secondN = 0
    thirdY = 0
    thirdN = 0
    crewY = 0
    crewN=0
    adultY=0
    adultN=0
    childY=0
    childN=0
    maleY=0
    maleN=0
    femaleY=0
    femaleN=0
    r = 0
    
    for key,value in sorted(dict.items()):
        if(value[2] =='female'):
            print(key,value)
            if(value[1] =='adult' and value[3] == 'yes'):
                adultY += 1
            if(value[1] =='adult' and value[3] == 'no'):
                adultN += 1
            if(value[1] =='child' and value[3] == 'yes'):
                childY += 1
            if(value[1] =='child' and value[3] == 'no'):
                childN += 1
            if(value[0] =='1st' and value[3] == 'yes'):
                firstY += 1
            if(value[0] =='1st' and value[3] == 'no'):
                firstN += 1
            if(value[0] =='2nd' and value[3] == 'yes'):
                secondY +=  1
            if(value[0] =='2nd' and value[3] == 'no'):
                secondN += 1
            if(value[0] =='3rd' and value[3] == 'yes'):
                thirdY +=  1
            if(value[0] =='3rd' and value[3] == 'no'):
                thirdN += 1
            if(value[0] =='crew' and value[3] == 'yes'):
                crewY +=  1
            if(value[0] =='crew' and value[3] == 'no'):
                crewN += 1
            r+=1
    print(r)
    print(firstY,firstN)
    print(secondY,secondN)
    print(thirdY,thirdN)
    print(crewY,crewN)
    print(adultY,adultN)
    print(childY,childN)

if __name__=="__main__":
    main()