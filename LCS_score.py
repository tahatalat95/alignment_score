#!/usr/bin/env python
# coding: utf-8

# In[1]:


# the function takes 5 values 
# seq1      -> the first sequence 
# seq2      -> the second sequence 
# mismatch  -> mismatch score
# match     -> match score
# gap       -> gab benality 

def LCS_score(Seq1, Seq2, mismatch, match, gap):
    
    
    L = [[0 for x in range(len(Seq2)+1)] for x in range(len(Seq1)+1)]
    prev_1=0
    prev_2=0

    # intialize 1st row by gap incremental value 
    for i in range(len(Seq1)+1):
        L[i][0] =prev_2
        prev_2=gap+prev_2 
    
    # intialize 1st colomn by gap incremental value 
    for j in range(len(Seq2)+1):
        L[0][j] =prev_1
        prev_1=gap+prev_1
        
    # Building the scoring matrix
    for i in range(1,len(Seq1)+1):
        for j in range(1,len(Seq2)+1):
        

                
            if ((L[i-1][j]  == L[i][j-1]) and (Seq1[i-1] == Seq2[j-1])) :
                L[i][j] = L[i-1][j-1] + match
                
            elif  (Seq1[i-1] == Seq2[j-1]) and  (L[i-1][j]  != L[i][j-1]):
                L[i][j] = L[i-1][j-1] + match
                
            elif  (Seq1[i-1] != Seq2[j-1]) and  (L[i-1][j]  == L[i][j-1]):
                L[i][j] = L[i-1][j-1] + mismatch 
                
            else :
                L[i][j] = max(L[i-1][j], L[i][j-1])+gap
                  
                
    return L   


# In[2]:


Seq1 = input('Enter first string : ')
Seq2 = input('Enter second string: ')
match = int(input('Enter match score: '))
mismatch = int(input('Enter mismatch score: '))
gap = int(input('Enter gap score: '))

result = LCS_score( Seq1, Seq2, mismatch, match, gap)


# In[3]:


result


# In[4]:


print(result[3][5]) # the value in the slides is 4 

