# coding=gbk
import os
import sys
import re
import operator
#功能2和功能3统计单词个数
def total_words(filename):	
	with open(filename,encoding='utf-8') as f:
		str1 = f.read()
		str1 = re.sub('[^a-zA-Z]',' ',str1) #sub函数 将不是字母的用空格代替
		str2 = str1.lower().split() #将所有单词变为小写统计
		words_dic = {}
		total = 0
		for word in str2:
			if word in words_dic:
				words_dic[word] += 1 #重复的单词加一
			else:
				words_dic[word] = 1 #不重复的单词写入words_dic字典
				total += 1    #统计单词个数
		print("total " + str(total) + " words")
		#对统计单词个数按值排序 
		words_order = sorted(words_dic.items(),key=lambda words_dic : words_dic[1],reverse=True)
		for key,value in words_order:
			print(key + " : " + str(value))
	f.close()
#功能4统计单词个数 文章和重定向
def total_word(content):
	str3 = content.lower().split()
	word_dic = {}
	total_1 = 0
	for word1 in str3:
		if word1 in word_dic:
			word_dic[word1] += 1
		else:
			word_dic[word1] = 1
			total_1 += 1
	print("total " + str(total_1) + " words")
	words_order1 = sorted(word_dic.items(),key=lambda word_dic : word_dic[1],reverse=True)
	for key1,value1 in words_order1:
		print(key1 + " : " + str(value1))
#功能3打开文件夹
def files_dic(files):
	files_list = os.listdir(files) #获取文件夹下列表
	for file in files_list:
		print("\n" + file)
		if not os.path.isdir(file):
			total_words(file)
def main(argv):
	#功能4 输入一段文章
	if(len(argv)==1):
		str = input()
		str = re.sub('[^a-zA-Z]',' ',str)
		total_word(str)
	#功能1和功能4
	elif sys.argv[1] == '-s':
		#功能1
		if(len(argv) == 3):
			total_words(sys.argv[2])
		#功能4 重定向
		elif(len(argv) == 2):
			redirect_words = sys.stdin.read() #读取文章内容
			redirect_words = re.sub('[^a-zA-Z]',' ',redirect_words)
			total_word(redirect_words)
	#功能3
	elif os.path.isdir(sys.argv[1]): #判断是文件夹
		files_dic(sys.argv[1])
	#功能2
	else:
		total_words(sys.argv[1])
#调用函数
if __name__ == "__main__":
	main(sys.argv[0:])



