import re
import os
try:
    os.remove("cvpr2019.txt")
except:
    pass
with open("cvpr2019.txt","wt") as wf:
    with open("html.txt", "rt") as f:
        for line in f:
            pdf = re.search(r'content_CVPR_2019.*\.pdf', line)
            if pdf:
                wf.write(pdf.group(0)+"\n")
