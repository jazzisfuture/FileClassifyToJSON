import os
import json


def labling(path):
    ls =os.listdir(path)
    # 获取根目录文件夹
    for l in ls:
        lstr = l.split('.')
        if len(lstr) == 2:
            ls.remove(l)
    print(ls)
    i = 0
    for l in ls:
        print(l)
        # 生成该文件夹的json
        lable = dict(labels=[{"name":l}])
        jsonStr = json.dumps(lable, indent=4)
        nowPath = path+ '\\'+l
        print(nowPath)
        fileNames = os.listdir(nowPath)
        # print(fileNames)
        for fileName in fileNames:
            fileName = fileName.split('.')[0].__add__('.json')
            # print(fileName)
            filePath = nowPath + '\\' + fileName
            # print(filePath)
            with open(filePath,"w") as fp:
                fp.write(jsonStr)
            print(i)
            i = i + 1


# for l in ls:
#     fileName = l.split('.')[0].__add__('.json')
#     print(fileName)
#     with open(fileName,"w") as fp:
#         fp.write(jsonStr)



if __name__ == "__main__":
    # 获取当前目录
    path = os.getcwd()
    labling(path)
    print('----------------------------')
    print('done')