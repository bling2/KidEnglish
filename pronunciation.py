#!/cisco/Anaconda/anaconda3/bin/python
# v1.0
#/ɑ:/ /ʌ/ /ɔ:/ /ɒ/ /ə/ /ɜ:/ /i:/ /ɪ/ /u:/ /ʊ/ /e/ /æ/
# 1    2  3    4   5    6    7    8   9   10  11  12
#/eɪ/ /aɪ/ /ɒɪ/ /ɪə/ /eə/ /ʊə/ /əʊ/ /aʊ/
# 13  14   15    16   17   18   19   20
#/p/ /t/ /k/ /f/ /θ/ /s/ /ʃ/ /h/ /tʃ/ /ts/ /tr/
# 21 22  23   24  25  26  27 28  29    30   31
# /b/ /d/ /g/ /v/ /ð/ /z/ /ʒ/ /r/ /dʒ/ /dz/ /dr/ /j/ /w/ /m/ /n/ /ŋ/ /l/
# 32  33  34  35  36  37  38  39  40   41   42   43  44  45  46  47  48
# /ju:/ /aʊə/ / / / /
# 49     50   98  99
# a+100 e+200 i+300 o+400 u+500
import random
dict = {'l(a)ke':13, 'c(a)ke':13, 'm(a)ke':13, 't(a)ke':13, 'b(a)ke':13,
'b(a)d':12, 's(a)d':12, 'm(a)d':12, 'c(a)t':12,
'h(e)':7, 'sh(e)':7,
'dr(e)ss':11, 'b(e)t':11, 't(e)st':11,
'dr(i)ve':14, 'n(i)ne':14, 'm(i)ne':14, 'h(i)gh':14, 'l(i)ke':14, 'l(i)ne':14,
'l(i)ve':8, 'l(i)ttle':8,'b(i)g':8,'t(i)ck':8,'s(i)ck':8,'f(i)t':8,
'n(o)':19, 'g(o)':19,'s(o)':19,
'n(o)t':4,'h(o)t':4,'f(o)x':4,'b(o)x':4,'t(o)p':4, 
'n(o)thing':2,'l(o)ve':2,'m(o)ther':2,'gl(o)ve':2,
'c(u)be':49,'(u)se':49,
'b(u)sy':8,
'h(u)sband':2,'b(u)s':2,'c(u)t':2,'(u)mbrella':2,'h(u)ndred':2,
'(y)es':43,'(y)ellow':43,
'bab(y)':8, 'quickl(y)':8,'slowl(y)':8,'friendl(y)':8,
'br(ai)n':13,'m(ai)n':13, 's(ai)l':13,
'l(au)gh':1,
'n(au)ghty':3,
't(al)k':3, 'f(al)se':3, 't(al)l':3, '(al)l':3, 'f(al)l':3,
'c(al)m':1,'h(al)f':1,
'r(ea)d':7,'(ea)st':7,'m(ea)t':7,'s(ea)t':7,'(ea)t':7,'t(ea)':7,
'h(ea)d':11, 'd(ea)d':11, 
'm(ee)t':7,'f(ee)d':7,'b(ee)':7,'s(ee)':7,'f(ee)t':7,
'coff(ee)':21,
'(ei)ght':13,
'h(ei)ght':14,
'bel(ie)ve':7,
'l(ie)':14, 'd(ie)':14,
'c(oa)t':19,'g(oa)t':19,'fl(oa)t':19,'l(oa)f':19,'s(oa)p':19,
'b(oy)':15,'t(oy)':15,'n(oi)se':15,'j(oy)':15,'ch(oi)ce':15,
'bl(oo)d':2,'fl(oo)d':2,
'b(oo)k':410,'c(oo)k':410,'l(oo)k':410,'t(oo)k':410,
'm(oo)n':409,'s(oo)n':409,'f(oo)d':409,'b(oo)t':409,'r(oo)t':409,'f(oo)l':409,
'l(ou)d':20,
'fam(ou)s':5,'delici(ou)s':5,
'j(ui)ce':9,
'b(ui)ld':8,'bisc(ui)t':8,'min(u)te':8,

'air':17,'h(air)':17,'f(air)':17,'ch(air)':17,
'b(ar)':1,'c(ar)d':1,'c(ar)':1,'c(ar)d':1,'f(ar)':1,'h(ar)d':1,'j(ar)':1,'p(ar)t':1,
'w(ar)m':3,'w(ar)':3,
'l(aw)':3,'j(aw)':3,'s(aw)':3,
'are':1,
'c(are)':17,'b(are)':17,'d(are)':17,
'cl(ear)':16,'h(ear)':16,'b(ear)':16,'n(ear)':16,'d(ear)':16,'f(ear)':16,'p(ear)':16,'t(ear)':16,
'th(ea)tre':16,
'w(ear)':17,
'work(er)':5,'teach(er)':5,'bett(er)':5,
'h(ere)':16,'th(ere)':16,
'ch(eer)':16, 'd(eer)':16,
'f(ew)':2049,'n(ew)':2049, 'd(ew)':2049,
'bl(ew)':2009,
'b(ir)d':6,'g(ir)l':6,'b(ir)thday':6,
'doct(or)':5,'act(or)':5,
'w(or)k':6,
'sw(or)d':3,'h(or)se':3,'c(or)d':3,'n(or)th':3,
'br(ow)n':420,'c(ow)':420,'n(ow)':420,'(ow)l':420,'br(ow)':420,'cl(ow)n':420,
'bl(ow)':419,'borr(ow)':419,'sh(ow)':419,'gr(ow)':419,'l(ow)':419,'fl(ow)':419,'kn(ow)':419,'r(ow)':419,'wind(ow)':419,'b(ow)l':419,
'f(our)':403,'f(our)teen':403,
'our':50,'h(our)':50,'fl(our)':50,
'ch(ur)ch':6,'h(ur)t':6,

'(th)ank':25,'nin(th)':25,'bir(th)day':25,
'(th)is':36,'(th)at':36,'(th)ose':36,'(th)ese':36,

'(ch)ild':29,'(ch)air':29,'(ch)eck':29,'(ch)eer':29,'(ch)urch':29,
'(Ch)ristmas':23,
'(sh)ip':27,'engli(sh)':27,'(sh)eep':27,

'(m)ap':45,'cli(m)b':45,'(m)ake':45,'na(m)e':45,'co(m)e':45,

'(b)oy':32,'ru(bb)er':32,'(b)us':32,'(b)ath':32,
'clim(b)':932,
'(wh)o':28,'(wh)ose':28,
'(wh)ere':44,'(wh)en':44,'(wh)atever':44,'(wh)ich':44,
'prepara(tion)':98,'na(tion)':98,'dicta(tion)':98,'sta(tion)':98,
'ques(tion)':99, 
'fa(ces)':1010,'bu(ses)':1010,
'appl(es)':37,'piano(s)':37,'toy(s)':37,'egg(s)':37,'kniv(es)':37,'pear(s)':37,'orang(es)':37,
'rock(s)':26,'map(s)':26,'giraff(es)':26,'cliff(s)':26,'bank(s)':26,'thank(s)':26,'month(s)':26,
}

def get_keys(d, value):
    return [k for k,v in d.items() if v == value]

def pick_q(value1, value2):
    list_a=get_keys(dict, value1)
    list_b=get_keys(dict, value2)
    list_ans=[1,2,3,4]
    list_choice=[]
    ans=random.choice(list_ans)
    for i in list_ans:
        if ans==i:
            list_choice.append(random.choice(list_b))
        else:
            list_choice.append(random.choice(list_a))

    print("A", end=".")
    print(list_choice[0], end="     ")
    print("B", end=".")
    print(list_choice[1], end="     ")
    print("C", end=".")
    print(list_choice[2], end="     ")
    print("D", end=".")
    print(list_choice[3])

list_type_must=((26,37),(2049,2009),(37,26),(419,420),(420,419),(409,410),(410,409))

list_type=((3,1),(4,2),(2,4),(8,9),(12,13),(13,12),(7,11),(11,7),(8,14),(14,8),
(4,19),(19,4),(409,410),(410,409),(16,17),(17,16),(26,37),(37,26),
(29,23),(25,36),(36,25),(98,99), (32,932),(44,28),(8,43),
(50,403))
print("=================================")
print("select a different pronunciation:")
print("=================================")
print("")
for j in range (1,6):
    print(j, end=". ")
    list=list_type_must[j]
    pick_q(list[0], list[1])
for j in range (7,21):
    print(j, end=". ")
    list=random.choice(list_type)
#    print(list[0],list[1],end=" ")
    pick_q(list[0], list[1])


