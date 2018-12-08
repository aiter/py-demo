#!/usr/bin/python
# -*- coding: UTF-8 -*-

try:
    fh = open("testfile", "w")
    fh.write("这是一个测试文件，用于测试异常!!")
except IOError:
    print "Error1: 没有找到文件或读取文件失败"
else:
    print "内容写入文件成功"
    fh.close()

'''
try-finally 语句无论是否发生异常都将执行最后的代码。
try:
    fh = open("testfile", "w")
    fh.write("这是一个测试文件，用于测试异常!!")
finally:
    print "Error2: 没有找到文件或读取文件失败"
	fh.close()
'''

'''
当在try块中抛出一个异常，立即执行finally块代码。

finally块中的所有语句执行后，异常被再次触发，并执行except块代码。
'''
try:
    fh = open("testfile", "w")
    try:
        fh.write("这是一个测试文件，用于测试异常!!")
    finally:
        print "关闭文件"
        fh.close()
except IOError:
    print "Error3: 没有找到文件或读取文件失败"


print "异常的参数demo---"
# 定义函数
def temp_convert(var):
    try:
        return int(var)
    except ValueError, Argument:
        print "参数没有包含数字\n", Argument

# 调用函数
temp_convert("xyz")

print "触发异常demo---"
# 定义函数
def mye( level ):
    if level < 1:
        raise Exception,"Invalid level!"
        # 触发异常后，后面的代码就不会再执行

try:
    mye(0)            # 触发异常
except Exception,err:
    print 1,err
else:
    print 2


print "自定义异常demo---"
class Networkerror(RuntimeError):
    def __init__(self, arg):
        self.args = arg

def errortest( level ):
	if level < 1:
		raise Networkerror,"use define error"

try:
	errortest(0)
except Networkerror,err:
	print 1,''.join(err)
else:
	print 2
