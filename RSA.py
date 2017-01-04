#imports
import random
import math

def ExtendedEuclid(a,b):
    if b==0:
        return [1,0,a]
    else:
        x,y,d = ExtendedEuclid(b,a % b)
        return y,x-((a//b)*y),d


def Euclid(a,b):
    if b ==0:
        return a
    else:
        return Euclid(b,a%b)


def modInverse(e,phi):
    gcdForm = ExtendedEuclid(e,phi) #phi first then e
    #Ensuring it does not go over phi
    #Maybe remove
    return gcdForm[0]%phi


def GeneratePublicPrivate(e,BigPrimeOne,BigPrimeTwo):

    #Returns list of [d,n] d being the mod inverse
    return [modInverse(e,(BigPrimeOne-1)*(BigPrimeTwo-1)),(BigPrimeOne*BigPrimeTwo)]

    



#test for fermats little theorem
def fermat(BigPrime):

    is_Prime = True  #test flag for the loop

    #tests four different a's to ensure security
    for x in range(0,4):
        a = random.randint(1,BigPrime-1)
        test = pow(a,BigPrime-1,BigPrime)

        if ((test % BigPrime) != 1):
            return False
        
    return True

    
    

# function for generating the prime
def GeneratePrime(size):
    # List of random dits size long
    is_Prime = False
    while is_Prime == False:
        #pList must be initalized to empty list
        pList = []
        for i in range(size):
            pList.append(random.randrange(0,10,1))
        #if first number is 0 change it
        if pList[0] == 0:
            pList[0] = random.randint(1,10)

        if fermat(int(''.join(str(i) for i in pList))) == True:
            is_Prime = True
            

    return int(''.join(str(i) for i in pList))

#Encrypt the message
def Encrypt(message,e,n):
    #transforming the message to an int
    M = int(message.encode("hex"),16)
    return pow(M,e,n)

#decryption function
def decrypt(d,n,C):
    #decrypting the message
    Dmessage = pow(C,d,n)
    hexValue = hex(Dmessage).rstrip("L").lstrip("0x") or "0" #striping L and 0x off of the hex form
    return hexValue.decode("hex")
    
    
    
    
    
    
        
    

