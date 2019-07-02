import urllib.request
import os
import re

os.makedirs(os.path.join("CVPR-2019","paper"))
os.makedirs(os.path.join("CVPR-2019","supplemental"))
with open("cvpr2019.txt", "rt") as f:
    for line in f:
        name = line.split("/")[-1]
        name_list = re.split(r"_|\.",name)
        name = " ".join(name_list[1:-4])+".pdf"
        type = name_list[-2]
        print(type,":",name)
        urllib.request.urlretrieve("http://openaccess.thecvf.com/"+line, os.path.join("CVPR-2019",type,name))