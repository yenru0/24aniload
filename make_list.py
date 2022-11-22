start = 0
end = 709
with open("list.txt", 'w', encoding='utf-8') as f:
    f.writelines("file %03d.ts\n"%i for i in range(start, end+1))