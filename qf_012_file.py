stream = open(r"C:\aa.txt","a")
s="""
你好！
    欢迎来到澳门博彩赌场，赠送你一个金币
                赌王：高进
"""
stream.write(s)
stream.write("龙五")

stream.close()  #释放资源
