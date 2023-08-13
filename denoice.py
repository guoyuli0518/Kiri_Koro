import os
path = input("请输入待处理数据路径（以\结尾）：")
out_path=input("请输入输出路径（以\结尾，一定要实际存在）：")
os.system("cd "+path+" && md temp")
os.system("cd "+path+" && md temp_1")
os.system("cd "+path+" && md temp_2")
os.system("cd "+path+" && md temp_3")
os.system("cd "+path+" && md temp_4")
os.system("cd "+path+" && md temp_5")
os.system("cd "+path+" && md temp_6")
os.system("cd "+path+" && md temp_7")
os.system("cd "+path+" && md temp_8")
os.system("cd "+path+" && md temp_9")
fns = [os.path.join(root,fn) for root, dirs, files in os.walk(path) for fn in files]
count=0
for f in fns:
    os.system("cd waifu2x-caffe && waifu2x-caffe-cui.exe -i "+ '"'+ f + '"'+" -m noise --noise_level 3 -o "+'"'+ path+r"temp\temp" +str(count)+'.png"')
    count+=1

fns_1 = [os.path.join(root,fn) for root, dirs, files in os.walk(path+"temp") for fn in files]
count=0
for f in fns_1:
    os.system("cd waifu2x-caffe && waifu2x-caffe-cui.exe -i "+ '"'+ f + '"'+" -m noise --noise_level 3 -o "+'"'+ path+r"temp_1\temp"+str(count)+'.png"')
    count+=1

os.system("rmdir /s /q "+path+"temp")

fns_2 = [os.path.join(root,fn) for root, dirs, files in os.walk(path+"temp_1") for fn in files]
count=0
for f in fns_2:
    os.system("cd waifu2x-caffe && waifu2x-caffe-cui.exe -i "+ '"'+ f + '"'+" -m noise --noise_level 3 -o "+'"'+ path+r"temp_2\temp"+str(count)+'.png"')
    count+=1

os.system("rmdir /s /q "+path+"temp_1")

fns_2 = [os.path.join(root,fn) for root, dirs, files in os.walk(path+"temp_2") for fn in files]
count=0
for f in fns_2:
    os.system("cd waifu2x-caffe && waifu2x-caffe-cui.exe -i "+ '"'+ f + '"'+" -m noise --noise_level 3 -o "+'"'+ path+r"temp_3\temp"+str(count)+'.png"')
    count+=1

os.system("rmdir /s /q "+path+"temp_2")

fns_2 = [os.path.join(root,fn) for root, dirs, files in os.walk(path+"temp_3") for fn in files]
count=0
for f in fns_2:
    os.system("cd waifu2x-caffe && waifu2x-caffe-cui.exe -i "+ '"'+ f + '"'+" -m noise --noise_level 3 -o "+'"'+ path+r"temp_4\temp"+str(count)+'.png"')
    count+=1

os.system("rmdir /s /q "+path+"temp_3")

fns_2 = [os.path.join(root,fn) for root, dirs, files in os.walk(path+"temp_4") for fn in files]
count=0
for f in fns_2:
    os.system("cd waifu2x-caffe && waifu2x-caffe-cui.exe -i "+ '"'+ f + '"'+" -m noise --noise_level 3 -o "+'"'+ path+r"temp_5\temp"+str(count)+'.png"')
    count+=1

os.system("rmdir /s /q "+path+"temp_4")

fns_2 = [os.path.join(root,fn) for root, dirs, files in os.walk(path+"temp_5") for fn in files]
count=0
for f in fns_2:
    os.system("cd waifu2x-caffe && waifu2x-caffe-cui.exe -i "+ '"'+ f + '"'+" -m noise --noise_level 3 -o "+'"'+ path+r"temp_6\temp"+str(count)+'.png"')
    count+=1

os.system("rmdir /s /q "+path+"temp_5")

fns_2 = [os.path.join(root,fn) for root, dirs, files in os.walk(path+"temp_6") for fn in files]
count=0
for f in fns_2:
    os.system("cd waifu2x-caffe && waifu2x-caffe-cui.exe -i "+ '"'+ f + '"'+" -m noise --noise_level 3 -o "+'"'+ path+r"temp_7\temp"+str(count)+'.png"')
    count+=1

os.system("rmdir /s /q "+path+"temp_6")

fns_2 = [os.path.join(root,fn) for root, dirs, files in os.walk(path+"temp_7") for fn in files]
count=0
for f in fns_2:
    os.system("cd waifu2x-caffe && waifu2x-caffe-cui.exe -i "+ '"'+ f + '"'+" -m noise --noise_level 3 -o "+'"'+ path+r"temp_8\temp"+str(count)+'.png"')
    count+=1

os.system("rmdir /s /q "+path+"temp_7")

fns_2 = [os.path.join(root,fn) for root, dirs, files in os.walk(path+"temp_8") for fn in files]
count=0
for f in fns_2:
    os.system("cd waifu2x-caffe && waifu2x-caffe-cui.exe -i "+ '"'+ f + '"'+" -m noise --noise_level 3 -o "+'"'+ path+r"temp_9\temp"+str(count)+'.png"')
    count+=1

os.system("rmdir /s /q "+path+"temp_8")

fns_2 = [os.path.join(root,fn) for root, dirs, files in os.walk(path+"temp_9") for fn in files]
count=0
for f in fns_2:
    os.system("cd waifu2x-caffe && waifu2x-caffe-cui.exe -i "+ '"'+ f + '"'+" -m noise --noise_level 3 -o "+'"'+ out_path+str(count)+'.png"')
    count+=1

os.system("rmdir /s /q "+path+"temp_9")