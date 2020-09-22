# coding=gbk
import os
import sys
import re
import operator
#����2�͹���3ͳ�Ƶ��ʸ���
def total_words(filename):	
	with open(filename,encoding='utf-8') as f:
		str1 = f.read()
		str1 = re.sub('[^a-zA-Z]',' ',str1) #sub���� ��������ĸ���ÿո����
		str2 = str1.lower().split() #�����е��ʱ�ΪСдͳ��
		words_dic = {}
		total = 0
		for word in str2:
			if word in words_dic:
				words_dic[word] += 1 #�ظ��ĵ��ʼ�һ
			else:
				words_dic[word] = 1 #���ظ��ĵ���д��words_dic�ֵ�
				total += 1    #ͳ�Ƶ��ʸ���
		print("total " + str(total) + " words")
		#��ͳ�Ƶ��ʸ�����ֵ���� 
		words_order = sorted(words_dic.items(),key=lambda words_dic : words_dic[1],reverse=True)
		for key,value in words_order:
			print(key + " : " + str(value))
	f.close()
#����4ͳ�Ƶ��ʸ��� ���º��ض���
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
#����3���ļ���
def files_dic(files):
	files_list = os.listdir(files) #��ȡ�ļ������б�
	for file in files_list:
		print("\n" + file)
		if not os.path.isdir(file):
			total_words(file)
def main(argv):
	#����4 ����һ������
	if(len(argv)==1):
		str = input()
		str = re.sub('[^a-zA-Z]',' ',str)
		total_word(str)
	#����1�͹���4
	elif sys.argv[1] == '-s':
		#����1
		if(len(argv) == 3):
			total_words(sys.argv[2])
		#����4 �ض���
		elif(len(argv) == 2):
			redirect_words = sys.stdin.read() #��ȡ��������
			redirect_words = re.sub('[^a-zA-Z]',' ',redirect_words)
			total_word(redirect_words)
	#����3
	elif os.path.isdir(sys.argv[1]): #�ж����ļ���
		files_dic(sys.argv[1])
	#����2
	else:
		total_words(sys.argv[1])
#���ú���
if __name__ == "__main__":
	main(sys.argv[0:])



