软工实践作业——敏感词检测
中文

1、中文敏感词可能进行一些伪装，在敏感词中插入除字母、数字、换行的若干字符仍属于敏感词。如：当山寨为敏感词词汇时，山_寨，山@寨，山 寨，均可视为敏感词。

2、中文文本中存在部分谐音替换、拼音替代、拼音首字母替代的敏感词（拼音不区分大小写），如 shan寨，栅寨，山Z等均可视为敏感词。

3、中文文本中还存在少部分较难检测变形如繁体、拆分偏旁部首(只考虑左右结构)等。

4、不存在变形后再拆开偏旁部首的情况。

英文

1、英文文本不区分大小写，在敏感词中插入若干空格、数字等其他符号(换行、字母除外)，也属于敏感词，如hello为敏感词时，he_llo，h%ell@o，he llo均为敏感词 。

2、多个敏感词之间不考虑嵌套出现的情况，但可能存在变形后插入字符的情况。

3、敏感词中间一次插入的字符不超过20个

4、对输出进行一些可视化表示，如自动生成统计图、词云图等等（不要在测试的main文件中体现）。
