from random import randrange

subjects=['地主阶级','农民阶级','原始社会']
objects=['资本主义经济制度','封建土地所有制','原始社会的劳动关系']
effects=['影响了','断绝了','取消了','确立了']
adjective=['伟大的','严重地','具有历史意义的']

sul=len(subjects)
obl=len(objects)
efl=len(effects)
adl=len(adjective)



ret=[]
for i in range(5):
        while True:
                subkey=randrange(0,sul)
                objkey=randrange(0,obl)
                effkey=randrange(0,efl)
                adjkeyO=randrange(0,adl)
                adjkeyT=randrange(0,adl)
                break
        allword=adjective[adjkeyO]+subjects[subkey]+effects[effkey]+adjective[adjkeyT]+objects[objkey]
        ret.append(allword)
        
	

index=len(ret)
c=0
retur=''
for e in range(index):
   retu=ret[c]
   c+=1
   print(retu,sep=',')

   
        


