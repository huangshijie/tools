#coding:utf-8
import os, sys
import yaml

os.chdir(sys.path[0])

filePath = r'C:\迅雷下载'
fileList = os.listdir(filePath)
yamlPath = './resources/config.yml'
with open(yamlPath, 'r', encoding='utf-8') as f:
    prefixes = yaml.safe_load(f)
print(list(prefixes))

for i in range(0, len(fileList)):
    fileName = fileList[i]
    if(os.path.isfile(os.path.join(filePath, fileName))):
        print('original file name: ' + fileName)
        for j in range(0, len(prefixes)):
            newName = fileName.replace(prefixes[j], '')
        print('new file name: ' + fileName)
        os.rename(os.path.join(filePath, fileName), os.path.join(filePath, newName))