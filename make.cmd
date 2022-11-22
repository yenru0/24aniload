ffmpeg -f concat -i mylist.txt -c copy all.ts

ffmpeg -i all.ts -acodec copy -vcodec copy all.mp4