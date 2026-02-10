import string
import re

def punctuation_remove(text_data):
	punctuation ="".join([t for t in text_data if t not in string.punctuation])
	return punctuation


def tokenization(text_data,i):
    tokens_text = re.split(' ',text_data)
    return tokens_text[i]

def uyir(u):
    uyir=list(map(chr,u))
    return uyir

def uyir_kuril(uyir):
    uyir_kuril=[]
    for i in range(0,12,2):
        uk=uyir[i]
        uyir_kuril.append(uk)
    return uyir_kuril

def uyir_nedil(uyir):
    uyir_nedil=[]
    for i in range(1,12,2):
        un=uyir[i]
        uyir_nedil.append(un)
    return uyir_nedil

def uyir_mei18(uyirmei):
    uyir_mei=list(map(chr,u))
    return uyir_mei

def mei(uyirmei):
    mei=[]
    for i in uyirmei:
        a=chr(i)+chr(3021)
        mei.append(a)
    return mei

def uyir_mei247(uyirmei,w):
    uyir_meiall=[]
    for i in uyirmei:
        for j in w:
            b=chr(i)+chr(j)
            uyir_meiall.append(b)
        
def kuril(uyirmei,w,uyir_kuril):
    kuril=[]
    for i in range(1,11,2):
        for j in uyirmei:
            c=chr(j)+chr(w[i])
            kuril.append(c)
    h=list(map(chr,uyirmei))
    kuril.extend(h)
    kuril.extend(uyir_kuril)
    return kuril

def nedil(uyirmei,w,uyir_nedil):
    nedil=[]
    for i in range(0,11,2):
        for j in uyirmei:
            d=chr(j)+chr(w[i])
            nedil.append(d)
    nedil.extend(uyir_nedil)
    return nedil

def tamil_to_unicode(tamil_word):
    unicode_numbers = []
    for char in tamil_word:
        unicode_numbers.append(ord(char))
    return unicode_numbers

def letter_splitting(unicode_numbers):
    y=[]
    count=0

    for i in range(len(unicode_numbers)):
        if unicode_numbers[i] in w:
            count+=1

    if count != 0:
        i=0
        while(i<=len(unicode_numbers)-1):
            if i<=len(unicode_numbers)-2 and unicode_numbers[i+1] in w:
                f=chr(unicode_numbers[i])+chr(unicode_numbers[i+1])
                y.append(f)
                i+=2
            else:
                y.append(chr(unicode_numbers[i]))
                i+=1

    else:
        y=list(map(chr,unicode_numbers))
        
    return y

def asai1(kuril,nedil,mei,y):
    asai=[]

    a= "நிரை"
    b= "நேர்"

    i=0
    while i<= len(y)-1:
        
        if y[i] in kuril:
            if i<=len(y)-3 and y[i+1] in mei:
                if i<=len(y)-4 and y[i+2] in mei:
                    asai.append(b)
                    i+=3
                    y.insert(i,'/')
                    i=i+1
                    
                else:
                    asai.append(b)
                    i=i+2
                    y.insert(i,'/')
                    i=i+1


            elif i<=len(y)-3 and y[i+1] in kuril:
                if i<=len(y)-4 and y[i+2] in mei:
                    asai.append(a)
                    i+=3
                    y.insert(i,'/')
                    i=i+1
                else:
                    asai.append(a)
                    i=i+2
                    y.insert(i,'/')
                    i=i+1
                    

            elif i<=len(y)-3 and y[i+1] in nedil:
                if i<=len(y)-4 and y[i+2] in mei:
                    asai.append(a)
                    i+=3
                    y.insert(i,'/')
                    i=i+1
                else:
                    asai.append(a)
                    i=i+2
                    y.insert(i,'/')
                    i=i+1
                    
            else:
                asai.append(b)
                i+=1
                y.insert(i,'/')
                i=i+1

        else:
            if i<=len(y)-3 and y[i+1] in mei:
                if i<=len(y)-4 and y[i+2] in mei:
                    asai.append(b)
                    i=i+3
                    y.insert(i,'/')
                    i=i+1
                else:
                    asai.append(b)
                    i=i+2
                    y.insert(i,'/')
                    i=i+1

        
            else:
                asai.append(b)
                i+=1
                y.insert(i,'/')
                i=i+1
    return asai,y

def asai2(kuril,nedil,mei,y):
    asai=[]

    a= "நிரை"
    b= "நேர்"

    i=0
    while i<len(y):
        if y[i] in kuril:
            if i<=len(y)-2 and y[i+1] in mei:
                if i<=len(y)-3 and y[i+2] in mei:
                    asai.append(b)
                    i+=3
                    y.insert(i,'/')
                    i=i+1
                else:
                    asai.append(b)
                    i=i+2
                    y.insert(i,'/')
                    i=i+1
                    


            elif i<=len(y)-2 and y[i+1] in kuril:
                if i<=len(y)-3 and y[i+2] in mei:
                    asai.append(a)
                    i+=3
                    y.insert(i,'/')
                    i=i+1
                else:
                    asai.append(a)
                    i=i+2
                    y.insert(i,'/')
                    i=i+1

            elif i<=len(y)-2 and y[i+1] in nedil:
                if i<=len(y)-3 and y[i+2] in mei:
                    asai.append(a)
                    i+=3
                    y.insert(i,'/')
                    i=i+1
                else:
                    asai.append(a)
                    i=i+2
                    y.insert(i,'/')
                    i=i+1
            else:
                asai.append(b)
                i+=1
                y.insert(i,'/')
                i=i+1

        else:
            if i<=len(y)-2 and y[i+1] in mei:
                if i<=len(y)-3 and y[i+2] in mei:
                    asai.append(b)
                    i=i+3
                    y.insert(i,'/')
                    i=i+1
                else:
                    asai.append(b)
                    i=i+2
                    y.insert(i,'/')
                    i=i+1

        
            else:
                asai.append(b)
                i+=1
                y.insert(i,'/')
                i=i+1
    
    return asai,y

def asai3(kuril,nedil,mei,y,unicode_numbers):
    i=0
    asai=[]
    a="நேர்"
    b="நிரை"
    c='நேர்பு'
    d='நிரைபு'
    if(unicode_numbers[len(unicode_numbers)-1]==3009):
        if y[i] in nedil:
            if y[i+1] in mei:
                asai.append(c)
                #print("காசு")

        elif y[i] in kuril:
            if y[i+1] in mei:
                asai.append(c)
                #print("காசு")
            else:
                asai.append(d)
                #print("பிறப்பு")


    else:

        if y[i] in nedil:
        

            if y[i+1] in mei:
                asai.append(a)
                #print("நாள்")

        elif y[i] in kuril:

            if y[i+1] in mei:
                asai.append(a)
                #print("நாள்")
            else:
                asai.append(b)
                #print("மலர்")
            
    return asai[0]


def vaipadu1(asai,o=0):
    vaipadu=""
    
    if len(asai)==2:
        if asai[o]=="நேர்":
            if asai[o+1]=="நேர்":
                return "தேமா"
            else:
                return "கூவிளம்"
        else:
            if asai[o+1]=="நிரை":
                return "கருவிளம்"
            else:
                return "புளிமா"
    else:
        if asai[o]=="நேர்":
            if asai[o+1]=="நேர்":
                if asai[o+2]=="நேர்":
                    return "தேமாங்காய்"
                else:
                    return "தேமாங்கனி"
            else:
                if asai[o+2]=="நேர்":
                    return "கூவிளங்காய்"
                else:
                    return "கூவிளங்கனி"


        else:
            if asai[o+1]=="நிரை":
                if asai[o+2]=="நிரை":
                    return "கருவிளங்கனி"
                else:
                    return "கருவிளங்காய்"
            else:
                if asai[o+2]=="நிரை":
                    return "புளிமாங்கனி"
                else:
                    return "புளிமாங்காய்"
                    
    
def vaipadu2(asai):
    
    a="நேர்"
    b="நிரை"
    c='நேர்பு'
    d='நிரைபு'
    if asai==a:
        return "நாள்"
    elif asai==b:
        return "மலர்"
    elif asai==c:
        return "காசு"
    else:
        return "பிறப்பு"

def list_to_string(Y):
    y=""
    for i in Y:
        y+=i
    return y

        
        
        

def alagitu_vaipadu(a):
    punctuation_removed = punctuation_remove(a)
    import pandas as pd
    from collections import defaultdict
    kural=defaultdict()
    kural['சீர்']=[]
    kural['அசை']=[]
    kural['வாய்ப்பாடு']=[]
    
    for i in range(7):
    
        tamil_word = tokenization(punctuation_removed,i)
    
        unicode_numbers = tamil_to_unicode(tamil_word)
        y=letter_splitting(unicode_numbers)
    
        if i<6:
        
            if y[-1] in mei:
                aasai,Y=asai2(kuril,nedil,mei,y)
                kural['அசை'].append(aasai)
                Y=list_to_string(Y)
                kural['சீர்'].append(Y)
            else :
                aasai,Y=asai1(kuril,nedil,mei,y)
                kural['அசை'].append(aasai)
                Y=list_to_string(Y)
                kural['சீர்'].append(Y)
    
            vvaipadu=vaipadu1(aasai)
            kural['வாய்ப்பாடு'].append(vvaipadu)
        
        else:
            kural['சீர்'].append(tamil_word)
            aasai=asai3(kuril,nedil,mei,y,unicode_numbers)
            kural['அசை'].append(aasai)
        
            vvaipadu=vaipadu2(aasai)
            kural['வாய்ப்பாடு'].append(vvaipadu)
        

    return pd.DataFrame(kural,index=[1,2,3,4,5,6,7])
    
    


u = [2949,2950,2951,2952,2953,2954,2958,2959,2962,2963,2960,2964]
uyirmei = [2965,2969,2970,2974,2975,2979,2980,2984,2985,2986,2990,2991,2992,2993,2994,2995,2996,2997]
w=[3006,3007,3008,3009,3010,3014,3015,3018,3019,3016,3020,3021]

uyir=uyir(u)
uyir_kuril=uyir_kuril(uyir)
uyir_nedil=uyir_nedil(uyir)
mei=mei(uyirmei)
uyir_mei18=uyir_mei18(uyirmei)
uyir_mei247=uyir_mei247(uyirmei,w)
kuril=kuril(uyirmei,w,uyir_kuril)
nedil=nedil(uyirmei,w,uyir_nedil)


a="கற்றதனால் ஆய பயனென்கொல் வாலறிவன் நற்றாள் தொழாஅர் எனின்" #example Input 
thirukural=input('Thirukuralai ullidavum :')
table=alagitu_vaipadu(thirukural)

print(table)
