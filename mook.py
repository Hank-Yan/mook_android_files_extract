#!/usr/bin/env python
import sys, os, json, shutil
if __name__ == "__main__":
    # F:\playpython\cn.com.open.mooc\video
    path = raw_input("please input the source path: ") + os.sep + "video"
    if path == "":
        print "the path can not be empty!^_^!"
        sys.exit(0)
    # destPath = "C:\mook\videos"
    destPath = raw_input("please input the destination path: ")
    if destPath == "":
        print "the destPath can not be empty!^_^!"
        sys.exit(0)
    if os.path.exists(destPath):
        # we can use shutil to remove a dir and use os.remove to remove a file
        shutil.rmtree(destPath, True)
    # get the file names
    files = os.listdir(path)
    # print dirs
    for myFile in files:
        subPath = path + os.sep + myFile
        subFiles = os.listdir(subPath)
        for i,mySubFile in enumerate(subFiles):
            finalPath = subPath + os.sep + mySubFile
            finalJsonPath = finalPath + os.sep + "json.txt"
            finalMp4Path = finalPath + os.sep + "down.mp4"
            try:
                with open(finalJsonPath) as fp:
                    # fp = open(finalJsonPath)
                    content = json.load(fp)
                    parentDirName = content['courseName']
                    mp4NewName = content['sectionName']
                    fp.close()
                    if i == 0:
                        # need create the parent filename
                        # first get the file name
                        parentDirPath = destPath + os.sep + parentDirName
                        os.makedirs(parentDirPath)
                    destFilePath = parentDirPath + os.sep + "[" + str(i+1) +  "]" + mp4NewName + ".mp4"
                    print "getting: " + parentDirName +"--------" + mp4NewName + "  please wait........"
                    shutil.copy(finalMp4Path, destFilePath)
            except IOError as err:
                    print("oops, get some error, please look  " + finalPath + "for some more details")
    print "finished !!!"