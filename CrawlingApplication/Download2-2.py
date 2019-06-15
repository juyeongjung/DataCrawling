# 관리자 권한 필요. 아나콘다 실행시 관리자 권한으로 실행하자
#라이브러리들도 자주 확인하자.

import urllib.request as dw #이렇게 별칭을 주면 더욱 편하게 사용할 수 있음

imgURL="https://cafeptthumb-phinf.pstatic.net/20150404_41/onehodang2_1428121325007MWF8c_JPEG/10.jpg?type=w740"
htmlURL="https://www.google.com"

savePath1="c:/test1.jpg"
savePath2="c:/test1.html" #주로 html 파일을 다운로드 받아 필요한 정보를 파싱해서 얻는 것이 목적임

f=dw.urlopen(imgURL).read()
f2=dw.urlopen(htmlURL).read()

saveFile1=open(savePath1,'wb') # w:write, r:read, a:add, b:binary
saveFile1.write(f)
saveFile1.close() #반환하는 작업을 까먹지 말자

with open(savePath2,'wb') as saveFile2: #이렇게 파일을 가져오기를 권장. with 밖을 나가면 자동으로 close()를 호출해줌. 코드도 간결해 짐
    saveFile2.write(f2)

print("다운로드 완료")

#urlopen vs urlretrieve
#urlopen은 먼저 변수에 할당하고 파싱해서 저장(중간 작업이나 필요한 것만 가져 올때 좋음)
#urlretrieve는 바로 데이터 저장. 그 후에 변수에 할당(파싱 필요 없이 데이터를 가져올 때 좋음)

