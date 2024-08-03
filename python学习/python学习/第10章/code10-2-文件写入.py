# 打开文件
f = open('test2.txt', mode='w', encoding='utf-8')

# 写入文件
f.write('你好，我是mia\n')
f.write('你是谁\n')
f.writelines(['A\n', 'B\n'])  # 写入多行

# 关闭文件
f.close()