import subprocess

# make list 3 or 4
start = 0
end = 284
with open("list.txt", 'w', encoding='utf-8') as f:
    f.writelines("file 'loc/%04d.ts'\n"%i for i in range(start, end+1))

subprocess.check_output(['ffmpeg', '-f', 'concat', '-i', 'list.txt', '-c', 'copy', './output/all.ts'])

subprocess.run(['ffmpeg', '-i', './output/all.ts', '-acodec', 'copy', '-vcodec', 'copy', './output/all.mp4'])