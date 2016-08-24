

def palindrome(goiOut):
    if len(goiOut) <= 1:
        return True
    return goiOut[0] == goiOut[-1] and palindrome(goiOut[1:-1])




def substrings(goiIn):

    subPalindromes = []

    for iM in range(0,len(goiIn)):
        for iS in range(len(goiIn),iM, -1):
            if len(goiIn[iM:iS]) > 1 and len(goiIn[iM:iS]) != len(goiIn):
                if palindrome(goiIn[iM:iS]): 
                    subPalindromes.append(goiIn[0:iM] + " [" + goiIn[iM:iS] + "] " + goiIn[iS:len(goiIn)])
                    
    if subPalindromes:
        print ("\n\n\n:>Other palyndromes found in your input:" + str(len(subPalindromes)))
        for i in subPalindromes:
            print ("::> %s" % i)




def main():
    goi = input('Enter word:')
    kekka = "is" if palindrome(goi) else "IS NOT"
    print ("\n\n\n{0} {1} a palindrome.".format(goi, kekka))


    substrings(goi)



main()
