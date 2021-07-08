import math 
spamwordfreq={}
notspamwordfreq={}
notspam=0
spam=0
countspam=0
countnotspam=0
finalmailwordfreq={}
probnotspamwords={}
probspamwords={}            
ps=0.0
pns=0.0
def freq(mailcont,n):
    global countspam
    global countnotspam
    global spamwordfreq
    global notspamwordfreq
    if n==1:
        for word in mailcont.split():
            if word not in spamwordfreq:
                spamwordfreq[word]=0
            spamwordfreq[word]+=1
            countspam+=1
            
    else:
        for word in mailcont.split():
            if word not in notspamwordfreq:
                notspamwordfreq[word]=0
            notspamwordfreq[word]+=1
            countnotspam+=1  

def read():
    global notspam
    global spam
    f=open("datasets.csv","r")
    for l1 in f:
        line=l1.strip()
        listt=line.split(',')
        if(int(listt[2])==0):
            notspam+=1
        elif(int(listt[2])==1):
            spam+=1
        freq(listt[1],int(listt[2]))
def probabilitycalculator():
    global ps
    global pns
    global probnotspamwords
    global probspamwords
    ps=(spam/(spam+notspam))
    pns=(notspam/(spam+notspam))
    for i,j in spamwordfreq.items():
        probspamwords[i]=j/countspam
        
    for l,n in notspamwordfreq.items():
        probnotspamwords[l]=n/countnotspam
def finalfreq(l1):
    global finalmailwordfreq
    for word in l1.split():
        if word not in finalmailwordfreq:
            finalmailwordfreq[word]=0
        finalmailwordfreq[word]+=1

def predict(fin):
    read()
    probabilitycalculator()
    spamprob=0.0
    notspamprob=0.0
    finalfreq(fin)
    for i,j in finalmailwordfreq.items():
        if i in probspamwords:
            spamprob+=math.log(probspamwords[i])
    for l,n in finalmailwordfreq.items():
        if l in probnotspamwords:
            notspamprob+=math.log(probnotspamwords[l])
    finalspam=math.log(ps)*spamprob/((math.log(ps)*spamprob)+(math.log(pns)*notspamprob))
    finalnotspam=math.log(pns)*notspamprob/((math.log(ps)*spamprob)+(math.log(ps)*notspamprob))
    if(finalspam>finalnotspam):
        print("THE GIVEN EMAIL IS A SPAM EMAIL")
    else:
        print("THE GIVEN EMAIL IS NOT A SPAM EMAIL")
st=input("Enter the mail content\n")
st=st.split()
seperator=' '
st=seperator.join(st)
st=st.split(',')
st=seperator.join(st)
predict(st)