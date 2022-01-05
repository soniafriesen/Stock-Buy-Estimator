import spacy
import re
import itertools
import os
nlp = spacy.load('en_core_web_md')

# Method: get_stock_investment
# Purpose: A Function used to get each email, amounts, and total. It also displays email with the correlated amounts
# Parameters: Each email and its investment amounts
# Returns: A total amount invested for each email customer
def get_stock_investment(data):
    doc = nlp(data)

    emails = []
    amounts = []
    company = []    

    d = list(doc)

    for i in range(len(doc)):
        if(i+1 == len(doc)):
            break      

        #checking for emails
        if re.match(r"[^@]+@[^@]+\.[^@]+", doc[i].text):
            emails.append(doc[i])

         #checking for dollar amounts
        if(doc[i].pos_ == "SYM" and doc[i].tag_ == "$"):
            for k in range(len(d)):
                if(d[k] == doc[i+1]): 
                    if(d[k+1].text.lower() == "hundred" or d[k+1].text.lower() == "hundreds"):
                        amounts.append(
                            str(int(doc[i+1].text) * 100))
                    elif(d[k+1].text.lower() == "thousand" or d[k+1].text.lower() == "thousands"):
                        amounts.append(
                            str(int(doc[i+1].text) * 1000))
                    elif(d[k+1].text.lower() == "million" or d[k+1].text.lower() == "millions"):
                        amounts.append(
                            str(int(doc[i+1].text) * 1000000))
                    else:
                        amounts.append(doc[i+1].text)

        #checking for the companies
        if(doc[i].pos_ == "PROPN" and doc[i].tag_ == "NNP"):
            if(doc[i].dep_ == "compound" and doc[i+1].dep_ == "pobj"):
                company.append(f'{doc[i]} {doc[i+1]}')
            else:
                if(doc[i].dep_ == "pobj" and doc[i-1].dep_ != "compound"):
                    company.append(f'{doc[i]}')

    #for each email, get the amounts and the companies
    for i in range(len(emails)):
        print(f'{emails[i]}:', end="")
        for c in range(len(company)):
            temp = "{:,}$".format(
                int(amounts[c].replace(',', '')), 'USD', locale='en_US')
            print(f' {temp} to {company[c]}', end="")
            if(len(company)-c > 1):
                print(',', end="")
        print()

    total = 0.0
    temp = ""

    #get the total amount for each email
    for i in range(len(amounts)):
        temp = amounts[i].replace(',', '')
        total += float(temp)

    return total

# Method: ReadFile
# Purpose: A Function used to read the EmailLog.txt
# Parameters: filename
# Returns: array 
def ReadFile():
    # read the EmailLog.txt data from a text file
    f = open('EmailLog.txt', mode='r', encoding='utf-8')
    sentences = []  
    for line in f:
        line = line.strip('\n')
        sentences.append(line)
    # close the file stream
    f.close()
    return sentences

