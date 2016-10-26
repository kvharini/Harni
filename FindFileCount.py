import os
import math

def findDirectories(root_dir, keyword):
    outputArray={}
    for root, Dirs, files in os.walk(root_dir):
        for Directory in Dirs:
            if(Directory is not None):
                fileCount =FindFilecount(Directory)
                if(fileCount is not None):
                    print("Filecount=%d"%fileCount)
                    outstr =os.path.abspath(Directory)
                    outputArray={outstr, fileCount}
                    print ("outputArray%s"%outputArray)
                    print("Directory= %s\n"%Directory)
                    findDirectories(Directory, keyword)
        
def FindFilecount(root_dir):
    fileCount =0
    print(" inside findfile Root_dir=%s"%root_dir)
    for root, Dirs, files in os.walk(root_dir):
        files= next(os.walk(root_dir))[2]
        if(files is not None):
         #print("Filename= %s\n"%files)
         fileCount=len(files)
         print("FileCOUNT= %s\n"%fileCount)
            #for file1 in files:
         return fileCount

findDirectories("C:\Python27","txt")
