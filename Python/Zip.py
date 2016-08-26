# -×-coding:utf-8 -*-
import os,sys,zipfile


def unzipAll():
    coding = sys.argv[1]
    parentPath = os.getcwd()
    for name in os.listdir(parentPath):
        filePath = os.path.join(parentPath,name)
        if zipfile.is_zipfile(filePath):
            dirname = os.path.splitext(name)[0]
            dirPath = os.path.join(parentPath,dirname)
            if not os.path.exists(dirPath):
                os.mkdir(dirPath)
            fz = zipfile.ZipFile(filePath,'r')
            for n in fz.namelist():
                m = unicode(n,coding).encode('utf8')
                m = os.path.join(dirPath,m)
                path = os.path.split(m)[0]
                if not os.path.exists(path):
                    os.makedirs(path)
                try:
                    file(m,'wb').write(fz.read(n))
                except:
                    pass
            fz.close()
            print name+'解压完成！'

if __name__ == '__main__':
    unzipAll()
