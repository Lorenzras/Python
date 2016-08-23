

def palindrome(goiOut):
    if len(goiOut) <= 1:
        return True
    return goiOut[0] == goiOut[-1] and palindrome(goiOut[1:-1])


goiIn = input('Enter word:')


kekka = "is" if palindrome(goiIn) else "IS NOT"
print ("{0} {1} a palindrome.".format(goiIn, kekka))



subPalindromes = []

for iM in range(1,len(goiIn)):
    if (len(goiIn)-iM) <= 1:
        break

    if palindrome(goiIn[0:len(goiIn)-iM]):
        subPalindromes.append("[" + goiIn[0:len(goiIn)-iM] + "]" + goiIn[len(goiIn)-iM:len(goiIn)])
        
    if palindrome(goiIn[iM:len(goiIn)]):
        subPalindromes.append(goiIn[0:iM] + "[" + goiIn[iM:len(goiIn)] + "]")

    subTemp = goiIn[iM:len(goiIn)-iM]
    if len(subTemp) > 1 and palindrome(subTemp):
        subPalindromes.append(goiIn[0:iM] + "[" + subTemp + "]" + goiIn[len(goiIn)-iM:len(goiIn)])


if subPalindromes:
    print ("Other palyndromes found in your input:")
    for i in subPalindromes:
        print (": %s" % i)
