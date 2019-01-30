# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 21:20:14 2017

@author: sselv
"""
#==========================================================#

#Import libraries
import re
import os
import linecache
import xlrd

#==========================================================#

#Remove HTML Tags
def removehtmltag (line):
    
    #Remove HTML tags
    i = newline.find('<')
    if(i != -1):
        j = newline.find('>')
        for i in range (i,j+1):
            newline = newline.replace(newline[i], " ")

    
    
    newline = newline.replace("-", " ")
    
    if not newline is None:
        return newline;

#==========================================================#

#Stemming of tokens
def stemming (templist):

    nloc=0
    for i in templist:
        
        flag=True
                
        if(len(i) >=4 and flag):
            if(not(i[-4:] == 'eies' or i[-4:] == 'aies')):
                if(i[-3:] == 'ies'):
                    loc = templist.index(i)
                    #templist[loc][-3] = 'y'
                    #print(templist[loc][-3:])
                    templist[loc]=templist[loc].replace(templist[loc][-3:], "y")
                    flag=False
                    #print("stem1: "  + templist[loc])
                            
        if(len(i) >=3 and flag):                    
            if(not(i[-3:] == 'aes'  or i[-3:] == 'ees'  or i[-3:] == 'oes')):
                if(i[-2:] == 'es'):
                    loc = templist.index(i)
                    templist[loc]=templist[loc].replace(templist[loc][-2:], "e")
                    flag=False
                    #print("stem2: " + templist[loc])
                            
        if(len(i) >=2 and flag):  
            if(not(i[-2:] == 'us' or i[-2:] == 'ss')):
                if(i[-1:] == 's'):
                    loc = templist.index(i)
                    templist[loc]=templist[loc][:-1]
                    #templist[loc]=templist[loc].replace(templist[loc][-1:], "")
                    flag=False
                    #print("stem3: " + templist[loc])
                
        #if(len(i) >=3):  
            #if(i[-1] == singleqte and i[-2] == 's'):
                #templist[nloc]=templist[nloc].replace(templist[nloc][-2:], "")
                #print(nloc)
                #print(i)
                #print("stem4: " + templist[nloc])
                             
                
            #if(i[-1] == 's' and i[-2] == singleqte):
                #templist[nloc]=templist[nloc].replace(templist[nloc][-1:], "")
                #print(nloc)
                #print(i)
                #print("stem4: " + templist[nloc])
        
        #nloc=nloc+1   
                                 
            
        
        
    #Remove empty string from the list        
    while '' in templist:
        templist.remove('')            


#==========================================================#

#Split the words and apply the other logic (Stemming, Remove Quotes, etc..)
def splitwords (newline):
    
    #Define the list of stop words
    #stopwords = ['and', 'a', 'the', 'an', 'by', 'from', 'for', 'hence', 'of', 
                 #'the', 'with', 'in', 'within', 'who', 'when', 'where', 'why', 
                 #'how', 'whom', 'have', 'had', 'has', 'not', 'for', 'but', 
                 #'do', 'does', 'done' ]
    
    splcharfirst = [ '"', '(', '[' ]
    splcharlast  = [ '"', ')', ']', ',', '.', '?', ':', ';', '!']
    singleqte = "'"
        
    templist = newline.split()
    
    
#----------------------------------#    
    #Remove the stop list words
    for i in range(len(templist)):
        #loc = templist.index(i)
        for j in range(len(stopwords)):
            if templist[i] == stopwords[j]:
                #print("matched: %s" %templist[i])
                templist[i] = ''
                #loc = templist.index(i)
                #templist.remove(templist[loc])
                #templist.remove[i]
                #del templist.[i]
                #templist.replace(templist[i], "")
                #k = 0
                #for k in range(len(templist[i])):
                    
   
    #Remove empty string from the list        
    while '' in templist:
        templist.remove('')   

#----------------------------------#
    
    #Stemming <word>'s or <word>s' to <word>   
    nloc = 0
    for i in templist:
        if(len(i) >=3):  
            if(i[-1] == singleqte and i[-2] == 's'):
                templist[nloc]=templist[nloc].replace(templist[nloc][-2:], "")
                #print(nloc)
                #print(i)
                #print("stem4: " + templist[nloc])                            
                
            if(i[-1] == 's' and i[-2] == singleqte):
                templist[nloc]=templist[nloc].replace(templist[nloc][-2:], "")
            
        nloc = nloc + 1

    #Remove empty string from the list        
    while '' in templist:
        templist.remove('')   

#----------------------------------#                 
                     
    #Remove the fisrt character if it is a special character except single quote
    for i in templist:
        for j in splcharfirst:
            if(i[0] == j[0]):
                loc = templist.index(i)
                templist[loc] = templist[loc].replace(templist[loc][0], "")
            

    #Remove empty string from the list        
    while '' in templist:
        templist.remove('')   

#----------------------------------#                 

    #Remove the last character if it is a special character
    for i in templist:
        for j in splcharlast:
            if(i[-1] == j[0]):
                loc = templist.index(i)
                templist[loc] = templist[loc].replace(templist[loc][-1], "")    

                
                
     #Remove empty string from the list        
    while '' in templist:
        templist.remove('')                  
                
#----------------------------------#                 
                                    
    #Stemming of tokens

    #stemming(templist)

#----------------------------------#           
    
    #Remove single quotes from the string if found in FIRSR or LAST position
    nloc=-1 
    for i in templist: 
        
        nloc = nloc + 1  
        if(i[0] == singleqte): 
                #print("before:" + i)
                templist[nloc]=templist[nloc].replace(templist[nloc][0], "")  
                #print("After:" + i)
        
        #if(i[-1] == singleqte):
            #templist[nloc]=templist[nloc].replace(templist[nloc][-1], "") 
            #print(i)
        
        #nloc = nloc + 1
                    
    
    #Remove empty string from the list        
    while '' in templist:
        templist.remove('')    


#----------------------------------#       

#Remove single quote from the word 
    nloc = -1
    for i in templist:
        nloc = nloc + 1
        #templist[nloc] = templist[nloc].replace("'", "")
        #templist[nloc] = templist[nloc].replace("*", "")
        #templist[nloc] = templist[nloc].replace("(", "")
        #templist[nloc] = templist[nloc].replace(")", "")
        #templist[nloc] = templist[nloc].replace(",", "")
        templist[nloc] = templist[nloc].replace(".", "")        
        
        
#----------------------------------#       

#Remove other special character  
    #nloc = -1
    #for i in templist:
        #nloc = nloc + 1
        #if i.isalpha():
            #print('success')
            #templist[nloc] = templist[nloc].replace("*", "")
            #templist[nloc] = templist[nloc].replace("(", "")
            #templist[nloc] = templist[nloc].replace(")", "")
            #templist[nloc] = templist[nloc].replace(",", "")
            #templist[nloc] = templist[nloc].replace(".", "")
                        

#----------------------------------#        
        
    #Remove single character word *** check for Numeric  
    for i in templist:
        if(len(i.strip()) == 1 and not i.isdigit()):
            loc=templist.index(i)
            #print(i)
            templist.remove(templist[loc])

     
    #Remove empty string from the list        
    while '' in templist:
        templist.remove('')           
        
 
#----------------------------------#   
        
    return templist;
#==========================================================#

#Make Dictionary & Postings
def make_dict_posting():


    #Make Dictionary
    dictionary = 'Dictionary.csv'
    filedict = open(dictionary, "w+")    
    dict_txt = 'Dictionary.txt'
    filedict_txt = open(dict_txt, "w+")
    
    filedict.write('Term')
    filedict.write(',')
    filedict.write('DocFreq')
    filedict.write(',')
    filedict.write('Offset')
    filedict.write('\n')

    #Make posting list
    postings = 'Postings.csv'
    filepost = open(postings, "w+")    
    post_txt = 'Postings.txt'
    filepost_txt = open(post_txt, "w+")
    
    filepost.write('Term')
    filepost.write(',')    
    filepost.write('DocID')
    filepost.write(',')
    filepost.write('TermFreq')
    filepost.write('\n')



    offset = 0
    for i in indexlist:
        filedict.write(i)
        filedict.write(',')
        filedict_txt.write(i)
        filedict_txt.write(',')
        #filedict.write(num)
    
    
        dcid = 1
        df = 0
    
        for file in filenames:
        
            if file in ('positive.txt', 'negative.txt'):
                continue
    
            filename = dirname + slash + file +'_temp.txt'
            tempptr = open(filename, "r")
            tmpdata = tempptr.read();
            tmpdata = tmpdata.lower()
            count = tmpdata.count(i)
        
        
            if count>0:
                filepost.write(i)
                filepost.write(',')
                filepost_txt.write(i)
                filepost_txt.write(',')
                
                filepost.write(str(dcid))
                filepost.write(',')
                filepost_txt.write(str(dcid))
                filepost_txt.write(',')
                
                filepost.write(str(count))
                filepost.write('\n')
                filepost_txt.write(str(count))
                filepost_txt.write('\n')
                
                
                df = df+1
        
            tempptr.seek(0,0)
            tempptr.close()
            dcid = dcid + 1    
    
        #if df==0:
            #df=1
        
        filedict.write(str(df))
        filedict.write(',')
        filedict_txt.write(str(df))
        filedict_txt.write(',')
        
        filedict.write(str(offset))
        filedict.write('\n')
        filedict_txt.write(str(offset))
        filedict_txt.write('\n')
        
        offset = offset + df    

    filedict.close()
    filepost.close()

    filedict_txt.close()
    filepost_txt.close()

#==========================================================#

#Write Review for the file selected
def write_review(file):
    
    #Document table
    doctable = 'TempDocsTable.txt'
    filetable = open(doctable, "w+")
    filetable.write('-------------------------------------------------')    
    
    filename = dirname + slash + file +'_temp.txt'
    #print(filename)
    #print('\n')
    tempptr = open(filename, "r")
    tmpdata = tempptr.readlines()
    #print(tmpdata)
    tempptr.seek(0,0)
    
    filetable.write('\n')
    filetable.write('Doc Name: ')
    filetable.write(file)
    #filetable.write('<Yet to decide>')
    filetable.write('\n')
    
    filetable.write('Title: ')
    tmp=tmpdata[5]
    tmpstr = tmp.split("reviewed by")    
    #print(tmpstr[0])
    filetable.write(tmpstr[0])
    title = tmpstr[0]
    #print('SELVA')
    #print(tmpstr)
    filetable.write('\n')
    
    filetable.write('Reviewer: ')
    #print(tmpstr[1])
    filetable.write(tmpstr[1])
    filetable.write('\n')
    
    filetable.write('Snippet: ')
    #Capsule review:
    
    i = 0
    j = 0
    for line in tmpdata:
        if 'Capsule review:' in line:
            j=i
        i = i+1
        
    if j > 0:
        for j in range(j, j+4):
            filetable.write(tmpdata[j])
            #print(tmpdata[j])
        
    if j==0:
        j = 10
        for j in range(j, j+4):
            filetable.write(tmpdata[j])
            #print(tmpdata[j])
                
    filetable.write('\n')
    
    filetable.write('Rate: ')
    
    flg_rated=0
    flg_rate = ' '
    #Check 1: "-4 to +4 scale"
    i=0
    j=0
    for line in tmpdata:
        if '-4 to +4 scale' in line:
            j=i
        i = i+1
    #print(j)
    if j>0:
        string=tmpdata[j]
        #print(string)
        splstr = string.split()
        for i in splstr:
            if flg_rated ==0:
            #print(i)
                try:
                    n=int(i)
                except Exception:
                    k = j
                    #print('exception')
                else:
                    if n >= 0:
                        #print(n)
                        value = "P"
                        flg_rate = "P"
                        #print("P")
                    else:
                        value = "N"
                        flg_rate = "N"
                        #print("N")
                    flg_rated = 1
        
    if flg_rated ==1:
        filetable.write(value)
        
  
    #Check 2: "Tally Negative words with Positive words"
    pos = 0
    neg = 0    
    i = 0
    j = 0
    
    if flg_rated == 0:
        for line in tmpdata:
            if 'Capsule review:' in line:
                j=i
            i = i+1
        
        if j == 0:
            j = 10

        for j in range(j, j+4):
            if 'best' in tmpdata[j]:
                pos = pos+1
            if 'exciting' in tmpdata[j]:
                pos = pos + 1
            if 'outstanding' in tmpdata[j]:
                pos = pos + 1
            if 'dull' in tmpdata[j]:
                neg = neg + 1
            if 'boring' in tmpdata[j]:
                neg = neg + 1
            if 'disappointing' in tmpdata[j]:
                neg = neg + 1
            if 'failure' in tmpdata[j]:
                neg = neg + 1
      
        if pos==0 & neg == 0:
            flg_rated = 0
        else:
            if pos > neg:
                value = "P"
                flg_rate = "P"
            if neg > pos:
                value = "N"
                flg_rate = "N"
            if pos == neg:
                value = "NA"
                flg_rate = "NA"
            flg_rated = 1
    
    
        if flg_rated ==1:
            filetable.write(value)     
        
        
    
    #Check 3: "Check word Rate with Movie name"
    term = ' rate ' + title            
    i = 0
    j = 0
    
    if flg_rated ==0:
        for line in tmpdata:
            if term in line:
                j=i
            i = i+1
        
        if j > 0:
            for j in range(j, j+1):
                string = tmpdata[j]
                splstring = string.split()
                for k in splstring:
                    if flg_rated ==0:
                
                        if 'best' in k:
                            value = "P"
                            flg_rated =1
                        if 'exciting' in k:
                            value = "P"
                            flg_rated =1
                        if 'outstanding' in k:
                            value = "P"
                            flg_rated =1
                        if 'dull' in k:
                            value = "N"
                            flg_rated =1
                        if 'boring' in k:
                            value = "N"
                            flg_rated =1                    
                        if 'disappointing' in k:
                            value = "N"
                            flg_rated =1
                        if 'failure' in k:
                            value = "N"
                            flg_rated =1
                    
        if flg_rated ==1:            
            filetable.write(value)
            flg_rate = value

        
    #Check 4: ""
    if flg_rated ==0:
        filetable.write("NA")
        flg_rate = "NA"

    
    filetable.write('\n')
    #filetable.write('-------------------------------------------------')
    filetable.write('\n')
    
    #num = num + 1
    tempptr.close()

    #Close the Quey output Table
    filetable.close()
    
    return flg_rate
                            
    
    #print('*** File Processing Completed Successfully ***')

#==========================================================#
    
#Parse the input query
def parse_query(inp_qry):
    
    #print(inp_qry)
    global index_and 
    global index_and_not 
    global index_or 
    
    index_and = []
    index_and_not = []
    index_or = []    
    
    str_and = 'AND'
    str_and_not = 'AND NOT'
    str_or = 'OR'
                
    #while not(i==-1):
        #i = inp_qry.find('(', i+1, len(inp_qry))
        #index_opn = index_opn + i
    
    #while not(j==-1)        
        #j = inp_qry.find(')', j+1, len(inp_qry))
        #index_cls = index_cls + j
        
    inp_qry = inp_qry.replace('(', ' ')
    inp_qry = inp_qry.replace(')', ' ')
        
    qry_len = len(inp_qry)
    i = inp_qry.find(str_and)    
    j = inp_qry.find(str_and_not)
    k = inp_qry.find(str_or)
    #print(i)
    #print(k)
    
    #Query has AND && AND NOT condition
    if (i>-1 and j>-1):
        temp_str = inp_qry[j+7:].lower()        
        index_and_not = temp_str.split()
        temp_str = inp_qry[i+4:-(qry_len-j)].lower()
        index_and = temp_str.split()                     
    
    
    #Query has only AND condition
    if (i>-1):
        temp_str = inp_qry[i+4:].lower()
        #print(temp_str)
        index_and = temp_str.split()
        #print('selva')
        #print(index_and)
    
    #Query has only OR condition
    if (k>-1):
        temp_str = inp_qry[k+3:].lower()
        index_or = temp_str.split()
    
    #Delete stop words for AND Query
    for i in index_and:
        if i in stopwords:            
            k=index_and.index(i)
            #print(i)
            del index_and[k]

    #Delete stop words for AND NOT Query
    for i in index_and_not:
        if i in stopwords:
            k=index_and_not.index(i)
            #print(i)
            del index_and_not[k]
                
        #Delete stop words for AND Query
    for i in index_or:
        if i in stopwords:
            k=index_or.index(i)
            #print(i)
            del index_or[k]                


    #print('AND')
    #print(index_and)
    #print('AND NOT')
    #print(index_and_not)
    #print('OR')
    #print(index_or)    

#==========================================================#

#Find the matching files for the Query input    
def get_matching_files():

    global index_and 
    global index_and_not 
    global index_or     
    global index_match_file
    
    
    index_match_file = []
    idx_match_file_id = []
    idx_match_file_name = []
    
    len_and = len(index_and)
    len_and_not = len(index_and_not)
    len_or = len(index_or)
    #print('selva')
    #print(index_and)
    
    #filedict = open(dictionary, "r")
    #filepost = open(postings, "r")
    
    #global index_and
        
#------
    
    #Get list of file id for AND 
    dict_dtail = []
    tmp_match_file = []
    docfreqn = 0
    offsetn = 0
    if len_and>0:
        for qry_word in index_and:
            #print(qry_word)
            for line in data_dict:
                str_tmp = line.split(',')
                if qry_word in str_tmp:
                    line = line.replace('\n', "")
                    dict_dtail = line.split(',')                                   
                    docfreqn = int(dict_dtail[1])
                    offsetn = int(dict_dtail[2])
    
                    i=1
                    tmp_post = []
                    for i in range (0,docfreqn):
                        post_dtail = data_post[offsetn+i]
                        tmp_post = post_dtail.split(',')
                        tmp_match_file.append(tmp_post[1])
                        i+=1
    
    #print(tmp_match_file)
    tmp_match_file.sort()
    templist = list(set(tmp_match_file))
    
    for i in templist:
        if tmp_match_file.count(i) == len_and:
            index_match_file.append(i)
            
    #print(index_match_file)

 
#------
           
    #Get list of file id for AND NOT and Remove the file.
    if len(index_match_file)>0:
        dict_dtail = []
        docfreqn = 0
        offsetn = 0    
        if len_and_not>0:
            for qry_word in index_and_not:
                for line in data_dict:
                    tmp_str = line.split(',')
                    if qry_word in tmp_str:                    
                        line = line.replace('\n', "")
                        dict_dtail = line.split(',')                                   
                        #print(dict_dtail)
                        docfreqn = int(dict_dtail[1])
                        offsetn = int(dict_dtail[2])
    
                        i=1
                        tmp_post = []
                        for i in range (0,docfreqn):
                            post_dtail = data_post[offsetn+i]
                            #print(post_dtail)
                            tmp_post = post_dtail.split(',')
                            k=index_match_file.index(tmp_post[1])
                            del index_match_file[k]          
                            i+=1
        
        #print(index_match_file)            
    
#------
    #Get list of file id for OR 
    dict_dtail = []
    tmp_match_file = []
    docfreqn = 0
    offsetn = 0
    if len_or>0:
        for qry_word in index_or:
            for line in data_dict:
                str_tmp = line.split(',')
                if qry_word in str_tmp:
                    line = line.replace('\n', "")
                    dict_dtail = line.split(',')                                   
                    docfreqn = int(dict_dtail[1])
                    offsetn = int(dict_dtail[2])
    
                    i=1
                    tmp_post = []
                    for i in range (0,docfreqn):
                        #print(i)
                        post_dtail = data_post[offsetn+i]
                        tmp_post = post_dtail.split(',')
                        index_match_file.append(tmp_post[1])
                        i+=1
    
    index_match_file = list(set(index_match_file))
    #print(index_match_file)

 
#------

            
        
        
    #filedict.close()
    #filepost.close()
    
    
    
    
#==========================================================#
#        MAIN PROGRAM
#==========================================================#

slash = '\\'
dirname = input("Enter Folder Name :")

#Define the list of stop words
stopwords = ['and', 'a', 'the', 'an', 'by', 'from', 'for', 'hence', 'of', 
             'the', 'with', 'in', 'within', 'who', 'when', 'where', 'why', 
             'how', 'whom', 'have', 'had', 'has', 'not', 'for', 'but', 
             'do', 'does', 'done' ]



filenames = os.listdir(dirname)

index_fileno = []
index_filename = []

index_fileno = []
index_filename = []
nmbr = 0

#num = 0
indexlist = []

for file in filenames:
    
    #print(file)
    if file in ('positive.txt', 'negative.txt'):
        continue
    
    nmbr = nmbr + 1
    index_fileno.append(nmbr)
    index_filename.append(file)
    
    filepath = dirname + slash + file
    fp = open(filepath, "r")
    data = fp.read()
    data = re.sub(r'<.*?>', '', data)
    fp.close()

    fileptr = dirname + slash + file +'_temp.txt'
    tempfile = open(fileptr, "w+")
    tempfile.write(data)
    tempfile.close()

    fo = open(fileptr, "r")
    fo.seek(0,2)
    eof = fo.tell()
    fo.seek(0,0)

    #indexlist = []

    while(fo.tell() != eof):
        newline = fo.readline()
    
        if not newline is None:        
            #print(newline)
            newline = newline.replace("-", " ")
            newline = newline.replace("*", " ")
            newline = newline.replace("(", " ")
            newline = newline.replace(")", " ")
            newline = newline.replace(",", " ")
            newline = newline.replace("}", " ")
            newline = newline.replace("{", " ")
            newline = newline.replace("/", " ")
            newline = newline.replace("!", " ")
            newline = newline.replace(".", " ")
            newline = newline.lower()
            indexlist = indexlist + splitwords(newline) 
            #print(newline)
            
    fo.close()
    #fo.seek(0,0)

indexlist = list(set(indexlist))
indexlist.sort()

#print(index_fileno)
#print(index_filename)

#--------------

#Create Dictionary & Postings list    
make_dict_posting() 

dict_txt = 'Dictionary.txt'
filedict_txt = open(dict_txt, "r")
data_dict = filedict_txt.readlines()
filedict_txt.close()


post_txt = 'Postings.txt'
filepost_txt = open(post_txt, "r")
data_post = filepost_txt.readlines()
filepost_txt.close()



#--------------
#Get the input query

input_query = ''        
index_and = []
index_and_not = []
index_or = []
index_match_file = []


#Document table
tablename = 'Output.txt'
finaltbl = open(tablename, "w+")    
finaltbl.write("==================================================")
finaltbl.write('\n')



qryno = 0

while not (input_query == "EXIT"):
    input_query = input("Enter Query: ")    
    if not (input_query == 'EXIT'):

        qryno = qryno + 1
        name1 = 'PosTable.txt'
        postbl = open(name1, "w+")    
        name2 = 'NegTable.txt'
        negtbl = open(name2, "w+")            
        name3 = 'NaTable.txt'
        natbl = open(name3, "w+")                    
        
        
        parse_query(input_query)
        
        #finaltbl.write("-------------------------")
        
        
        get_matching_files()

        
        pos_rev = 0
        neg_rev = 0
        na_rev = 0
        index_match_file.sort()
        for i in index_match_file:
            k=index_fileno.index(int(i))
            name = index_filename[k]
            flg_rate = write_review(name)

            doctable = 'TempDocsTable.txt'
            filetable = open(doctable, "r")
            data = filetable.read()                                
            
            if flg_rate == "P":
                pos_rev = pos_rev + 1
                postbl.write(data)
                                
            if flg_rate == "N":
                neg_rev = neg_rev + 1
                negtbl.write(data)
                                
            if flg_rate == "NA":
                na_rev = na_rev + 1
                natbl.write(data)
            
            filetable.close()
            os.remove(doctable)
                            
        finaltbl.write('Query: ')
        finaltbl.write(str(qryno))
        finaltbl.write('\t')
        finaltbl.write(input_query)
        finaltbl.write('\n')
        
        if len(index_match_file)==0:
            finaltbl.write('*** NO RESULT ***')
            finaltbl.write('\n')
                    
        if pos_rev > 0:
            postbl.seek(0,0)
            data = postbl.read()
            finaltbl.write(data)
            
        if neg_rev > 0:
            negtbl.seek(0,0)
            data = negtbl.read()
            finaltbl.write(data)

        if na_rev > 0:
            natbl.seek(0,0)
            data = natbl.read()
            finaltbl.write(data)            
        
        
        postbl.close()
        negtbl.close()
        natbl.close()        
        
        os.remove(name1)
        os.remove(name2)
        os.remove(name3)                
        
        finaltbl.write("==================================================")
        finaltbl.write('\n')
        print('Query Processing Completed')        
           

finaltbl.close()

#--------------

#Delete all the intermediate files.
filenames1 = os.listdir(dirname)
for file in filenames1:
    if file.endswith("_temp.txt"):
        os.remove(dirname + slash +file)

#--------------

print('*** Results generated in Output.txt  ***')

#==========================================================#
#last saved
