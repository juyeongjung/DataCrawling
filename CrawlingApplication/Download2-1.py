# 관리자 권한 필요. 아나콘다 실행시 관리자 권한으로 실행하자

import urllib.request as dw #이렇게 별칭을 주면 더욱 편하게 사용할 수 있음

imgURL="https://cafeptthumb-phinf.pstatic.net/20150404_41/onehodang2_1428121325007MWF8c_JPEG/10.jpg?type=w740"
htmlURL="https://www.google.com"

savePath1="c:/test1.jpg"
savePath2="c:/test1.html" #주로 html 파일을 다운로드 받아 필요한 정보를 파싱해서 얻는 것이 목적임

dw.urlretrieve(imgURL,savePath1)
dw.urlretrieve(htmlURL,savePath2)
print("다운로드 완료")

