import jnius_config;
jnius_config.add_classpath('jedai-core-3.2.1-jar-with-dependencies.jar')

from jnius import autoclass

def Readfile(filePath):
    SerReaderClass = autoclass('org.scify.jedai.datareader.entityreader.EntitySerializationReader')
    # lst = autoclass('java.util.List')
    # EntityProfile = autoclass('org.scify.jedai.datamodel.EntityProfile')
    # Attribute = autoclass('org.scify.jedai.datamodel.Attribute')
    serReader = SerReaderClass(filePath)
    profiles = serReader.getEntityProfiles()
    return profiles

def ReadGtfile(filePath):
    GtSerReaderClass=autoclass('org.scify.jedai.datareader.groundtruthreader.GtSerializationReader')  
    gtserReader=GtSerReaderClass(filePath)
    gtprofiles=gtserReader.getDuplicatePairs(None)     
    return gtprofiles

def makeuplst(count,val):
    res=[]
    for i in range(0,count):
        res.append('')
    res.append(val)
    return res

def Dictionary_file(profiles):
    res={}
    res['id']=[i for i in range(1,len(profiles)+1)]
    count=0
    profilesIterator=profiles.iterator()
    while profilesIterator.hasNext():
        curkeylst=[]
        profile = profilesIterator.next()
        attributesIterator = profile.getAttributes().iterator()
        while attributesIterator.hasNext() :
            entity=str(attributesIterator.next().toString())
            attr=entity[(entity.find(':\t')+2):entity.find(',')]
            val=entity[(entity.find('value\t:\t')+8):]
            if attr in res:
                res[attr].append(val)
            else:
                res[attr]=makeuplst(count,val)
            curkeylst.append(attr)
        keylst=list(res.keys())
        for i in curkeylst:
            if i in keylst:
                keylst.remove(i)
        for i in keylst:
            if i!='id':res[i].append('') 
        count+=1
    return res
    

def Dictionary_Gt_file(profiles):
    res={'D1':[],'D2':[]}
    profilesIterator = profiles.iterator()
    while profilesIterator.hasNext() :
        profile = profilesIterator.next()
        res['D1'].append(str(profile.getEntityId1()))
        res['D2'].append(str(profile.getEntityId2()))
    return res


# def printGtFile(profiles):
#     profilesIterator = profiles.iterator()
#     while profilesIterator.hasNext() :
#         profile = profilesIterator.next()
#         print(str(profile.getEntityId1())+' | '+str(profile.getEntityId2()))
# def printFile(profiles,i=0,j=-1):
#     profilesIterator = profiles.iterator()
#     counter =0
#     flag=j
#     # print(len(profiles))
#     while profilesIterator.hasNext() :
#         profile = profilesIterator.next()
#         if (counter>=i) or flag==-1:
#             print("\n\n" + profile.getEntityUrl())
#             attributesIterator = profile.getAttributes().iterator()
#             while attributesIterator.hasNext() :
#                 print(attributesIterator.next().toString())
#         counter+=1
#         if counter>=j and flag!=-1:
#             break
