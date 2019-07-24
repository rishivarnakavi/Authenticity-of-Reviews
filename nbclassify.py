import ast
import re
import math
def main():
    file1=open("nbmodel.txt", "r")
    file2=open("train-text.txt", "r")
    file3=open("prior.txt", "r")
    file4=open("nboutput.txt", "w")

    for line in file3:
        values=line.split()

    total=(float(values[0])+float(values[1])+float(values[2])+float(values[3]))
    prior_tn=float(values[0])/total
    prior_dp=float(values[1])/total
    prior_dn=float(values[2])/total
    prior_tp=float(values[3])/total

    dict3={}
    word_tn, word_dp, word_dn, word_tp = float(0), float(0), float(0), float(0)
    for line in file1:
        words = line.split()
        dict3[words[0]] = [words[1], words[2], words[3], words[4]]
    for l in file2:
        w=l.split()
        id = w.pop(0)
        for word in w:
            if word in dict3.keys():
                word_tn+=math.log(float(dict3[word][0]), 2)
                word_dp+=math.log(float(dict3[word][1]), 2)
                word_dn+=math.log(float(dict3[word][2]), 2)
                word_tp+=math.log(float(dict3[word][3]), 2)
        prob_tn=math.log(prior_tn, 2)+word_tn
        prob_dp=math.log(prior_dp, 2)+word_dp
        prob_dn=math.log(prior_dn, 2)+word_dn
        prob_tp=math.log(prior_tp, 2)+word_tp
        word_tn, word_dp, word_dn, word_tp=0, 0, 0, 0
        file4.write(id)
        file4.write(' ')
        maxvalue=max(prob_tn,prob_dp,prob_dn,prob_tp)
        if maxvalue==prob_tn:
            file4.write('truthful')
            file4.write(' ')
            file4.write('negative')
            file4.write('\n')
        elif maxvalue==prob_dp:
            file4.write('deceptive')
            file4.write(' ')
            file4.write('positive')
            file4.write('\n')
        elif maxvalue==prob_dn:
            file4.write('deceptive')
            file4.write(' ')
            file4.write('negative')
            file4.write('\n')
        elif maxvalue==prob_tp:
            file4.write('truthful')
            file4.write(' ')
            file4.write('positive')
            file4.write('\n')


main()