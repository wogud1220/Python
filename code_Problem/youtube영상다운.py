
# https://github.com/yt-dlp/yt-dlp#embedding-yt-dlp

# 깃허브 사용법 참조

import yt_dlp   


ydl_opt = {
    # 'listformats':True 
    # 다운로드가 가능한 모든 플랫폼 출력
    # 보통 best라고 적힌 마지막 포맷을 다운받음
    
    'format': '18',
    # 18번째 가져와라

    # 'format': 'best[height<=400]'
    # 해상도가 400이하인것중에서 해상도 가장 높은
    # arg = filesize<10M 파일 사이즈 제한
    'outtmpl' : '%(title)s %(resolution)s.%(ext)s'
    # 파일 이름 바꾸기
}

with yt_dlp.YoutubeDL(ydl_opt) as ydl:    
    ydl.download(['https://www.youtube.com/watch?v=GkGjk7OPO78'])
