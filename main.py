from langconv import Converter
import sys

Total = 0
Sign = [' ','_','，','、','。','·','.','…','`',',','"','“',':','：',';',
           '?','？','！','!','<','>','=','~','+','-','*','%','/','^','|',
           '\\','\'','&','#','@','$','￥','(',')','[',']','{','}','【','】',
           '《','》','0','1','2','3','4','5','6','7','8','9']

class DFAFilter(object):
    def __init__(self):
        self.keyword_chains = {}  # 关键词链表
        self.delimit = '\x00'  # 限定

    def add(self, keyword):
        keyword = keyword.lower()  # 关键词英文变为小写
        chars = keyword.strip()  # 关键字去除首尾空格和换行
        if not chars:  # 如果关键词为空直接返回
            return
        level = self.keyword_chains
        # 遍历关键字的每个字
        for i in range(len(chars)):
            # 如果这个字已经存在字符链的key中就进入其子字典
            if chars[i] in level:
                level = level[chars[i]]
            else:
                for j in range(i, len(chars)):
                    level[chars[j]] = {}
                    last_level, last_char = level, chars[j]
                    level = level[chars[j]]
                last_level[last_char] = {self.delimit: 0}
                break
        if i == len(chars) - 1:
            level[self.delimit] = 0
        self.keyword_chains=level

    def tradition2simple(line):
        # 将繁体转换成简体
        line = Converter('zh-hans').convert(line)
        line.encode('utf-8')
        return line

    def isch(str):
        for char in str:
            if not '\u4e00' <= char <= '\u9fa5' :
                return False
        return True

    def parse(self, path):
        with open(path, encoding='utf-8') as f:
            for keyword in f.readlines():
                keyword = keyword.strip()
                self.add(keyword)

    def filter(self, linenum,message,ans):
        start = 0
        count = 0
        while start < len(message):
            level = self.keyword_chains
            l=start
            r=0
            p1=0
            original_message = message[start:]
            if message[start:] not in level:
                start=start+1
                continue
            step_ins = 0
            for char in original_message:
                r=start
                if char in Sign and p1==1:
                    step_ins=step_ins+1
                    continue
                if char in level:
                    step_ins += 1
                    p1=1
                    if self.delimit not in level[char]:
                        level = level[char]
                    else:
                        p1=1
                        start += step_ins - 1
                        r = start
                        word=level[char][self.delimit]
                        count+=1
                        # ans.append("line{}:<{}>{}\n".format(linenum,word,original_message[l:r+1]))
                        ans.append("Line" + str(linenum) + ":<" + word + ">" + message[l:r + 1])
                        break
                else:
                    break

            start+=1
        return count





if __name__ == "__main__":
    #path = 'D:\软件工程\words.txt'
    #result='D:\软件工程\ccc.txt'
    gfw = DFAFilter()
    file_words = sys.argv[1]
    file_org = sys.argv[2]
    file_output = sys.argv[3]
    linenum = 1
    flag = 0
    total = 0
    count=0
    ans = []
    gfw.parse(file_words)
    #file_path = 'D:\软件工程\org.txt'
    file = open(file_org, encoding="utf-8")
    while True:
        message=file.readline()
        message=message.strip()
        gfw.filter(linenum,message,ans)
        linenum=linenum+1
        total=total+count
        if message:
            flag=0
        else:
            flag=flag+1
        if flag>5:
            break
    file.close()
    output=open(file_output,'w')
    output.write("total:")
    output.write(str(total))
    output.write('\n')
    for item in range(len(str(ans))-1):
        output.write(str(ans[item]))
        output.write('\n')
