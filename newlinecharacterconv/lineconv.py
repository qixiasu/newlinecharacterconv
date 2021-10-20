"""Main module."""
import os,re
def crlf_to_lf(filename_list:list):
    #循环文件名列表
    for filename in filename_list:
        with open(filename,'rb') as f1, open('%s.bk'%filename,'wb') as f2:
            for line in f1:
                f2.write(re.sub(b'\r\n',b'\n',line))
        os.rename('%s.bk'%filename,filename+'.tmp')
        os.rename(filename,filename+'.bk')
        os.rename(filename+'.tmp', filename)
        print('%s 转换完成...'% os.path.basename(filename))
