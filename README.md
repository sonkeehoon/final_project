# Final-Project

## 테스트용 Flask
## templates 폴더 : html 파일들 
## static 폴더 : css, js 파일들과 이미지 폴더
## - EC2 instance(OS : 아마존 linux)에 flask 실행환경 구축하는 방법
<br><br>

<p> ubuntu의 경우 flask 웹서버 구축하는 방법이 검색하면 많이 나온다. </p>
<p> 이 글은 <strong>amazon linux</strong>에서 flask 웹서버를 구축하는 방법을 다룬다. </p>
<br>
<p>sudo git clone https://github.com/sonkeehoon/final_project.git</p> 
<p>sudo mv ./final_project/* /var/www/html</p>
<p> sudo chown -R ec2-user *</p>


## 우분투와는 이 부분이 다르다

<p>yum install java-1.8.0-openjdk </p>
<p>yum install java-1.8.0-openjdk-devel </p>
<p>---------------------------</p>
<p>pip3 install -r requirements.txt    # 필요 모듈 및 패키지 설치</p>
<p> /static/script.js 에 var url부분을 내 ec2인스턴스의 퍼블릭IP로 변경하자(5000번 포트가 열려 있어야 함)</p>
<p>sudo python3 app.py (서버 실행)</p>
 


