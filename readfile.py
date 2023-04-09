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
            
def printFile(profiles):
    profilesIterator = profiles.iterator()
    while profilesIterator.hasNext() :
        profile = profilesIterator.next()
        print("\n\n" + profile.getEntityUrl())
        attributesIterator = profile.getAttributes().iterator()
        while attributesIterator.hasNext() :
            print(attributesIterator.next().toString())