# read from data.txt and write into bengluru.txt
fp1=open("data.txt",'r')
data=fp1.read()
fp2=open("bengluru.txt",'w')
fp2.write(data)
fp1.close()
fp2.close()