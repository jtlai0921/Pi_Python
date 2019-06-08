import _thread
import time

# 为线程定义一个函数
def run_cds( threadName, delay):
   count = 0
   while True:
      time.sleep(delay)
      count += 1
      print ("%s: %s" % ( threadName, time.ctime(time.time()) ))

def run_lm35( threadName, delay):
   count = 0
   while True:
      time.sleep(delay)
      count += 1
      print ("%s: %s" % ( threadName, time.ctime(time.time()) ))

def run_pir( threadName, delay):
   count = 0
   while True:
      time.sleep(delay)
      count += 1
      print ("%s: %s" % ( threadName, time.ctime(time.time()) ))

# 创建两个线程
try:
   _thread.start_new_thread( run_cds, ("CDS", 0.1, ) )
   _thread.start_new_thread( run_lm35, ("LM35", 0.3, ) )
   _thread.start_new_thread( run_pir, ("PIR", 0.2, ) )
except:
   print ("Error: 无法启动线程")

while 1:
   pass