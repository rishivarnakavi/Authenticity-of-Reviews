import ast
import re
def main():
    file1 = open("train-text.txt", "r")
    file2 = open("train-labels.txt", "r")
    file3 = open("nbmodel.txt", "w")
    file4 = open("prior.txt", "w")

    dict1={}
    for line in file2:
        items = line.split()
        dict1[items[0]]=[items[1],items[2]]
    dict2={}
    dict3={}
    counts=0
    dp, dn, tp, tn, tn1, dn1, tp1, dp1 = 0, 0, 0, 0, 0, 0, 0, 0
    for line in file1:
        word_list=line.split()
        id = word_list.pop(0)
        items = dict1[id]
        element = [items[0], items[1]]
        if id in dict1.keys():
            for word in word_list:
                if word in dict2.keys(): 
                    if element == ['truthful', 'negative']:
                        dict2[word][0]+=1
                        tn1+=1
                    elif element == ['deceptive', 'positive']:
                        dict2[word][1]+=1
                        dp1+=1
                    elif element == ['deceptive', 'negative']:
                        dict2[word][2]+=1
                        dn1+=1
                    elif element == ['truthful', 'positive']:
                        dict2[word][3]+=1
                        tp1+=1
                else:
                    if element == ['truthful', 'negative']:
                        dict2[word]=[1,0,0,0]
                        tn1+=1
                    elif element == ['deceptive', 'positive']:
                        dict2[word]=[0,1,0,0]
                        dp1+= 1
                    elif element == ['deceptive', 'negative']:
                        dict2[word]=[0,0,1,0]
                        dn1+= 1
                    elif element == ['truthful', 'positive']:
                        dict2[word]=[0,0,0,1]
                        tp1+= 1
    print(tn1,dp1,dn1,tp1)
    file4.write(str(tn1))
    file4.write(' ')
    file4.write(str(dp1))
    file4.write(' ')
    file4.write(str(dn1))
    file4.write(' ')
    file4.write(str(tp1))
    file4.write(' ')
    for word in dict2.keys():
        length = len(dict2)
        dict2[word][0]=((dict2[word][0]+1)/float(tn1+length))
        dict2[word][1]=((dict2[word][1]+1)/float(dp1+length))
        dict2[word][2]=((dict2[word][2]+1)/float(dn1+length))
        dict2[word][3]=((dict2[word][3]+1)/float(tp1+length))

        file3.write(word)
        file3.write(' ')
        file3.write(str(dict2[word][0]))
        file3.write(' ')
        file3.write(str(dict2[word][1]))
        file3.write(' ')
        file3.write(str(dict2[word][2]))
        file3.write(' ')
        file3.write(str(dict2[word][3]))
        file3.write('\n')




    file3.close()
    file4.close()


main()
