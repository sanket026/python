fp=open('number_file','a')
for i in range(1,101):
    fp.write(f"/nnumber{i}")
    fp.write(str(i))