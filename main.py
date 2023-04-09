from readfile import Readfile,printFile
def main():
    filePath='walmartProfiles'
    walmartProfiles=Readfile(filePath)
    printFile(walmartProfiles)

if __name__=="__main__":
    main()
    