h,m,s = map(int,input("Enter your time : ").split())

hsec = h * 3600
msec = m * 60
result = hsec+msec+s

print("{:02d}:{:02d}:{:02d} = {:,d} seconds".format(h,m,s,result))


