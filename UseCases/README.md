<h1> USE CASES </h1>

1. 접속 후 로그인 |  2. 투표 |  3. 어드민 세팅 |  4. 투표 결과 조회

<br/>

<h3> 1. 접속 후 로그인 </h3> 

<img width="320" src="https://user-images.githubusercontent.com/96364048/191235108-db31e9ff-6296-4faf-b995-8788a691379b.png">

1. 케이스 명 : 접속 후 로그인 
2. 액터명 : User(Admin)
3. 사전 조건 : 로그인 되지 않음
4. 이벤트 흐름 : 
<br/>&ensp;  1. 홈 화면을 보여준다 (System)
<br/>&ensp;  2. 구글 로그인 클릭 (User)
<br/>&ensp;  3. 구글 로그인 화면을 띄운다 (System)
<br/>&ensp;  4. 구글 로그인 정보를 입력한다 (User)
<br/>&ensp;  5. 로그인된 계정에 대응되는 정보가 있는지 확인한다. (System)
<br/>&ensp;&emsp;    1. 첫 로그인이라면 정보입력 창을 띄운다 (System)
<br/>&ensp;&emsp;    2. 정보입력 창을 띄운다 (System)
<br/>&ensp;&emsp;    3. 정보를 입력한다 (User)
<br/>&ensp;  6. 투표 화면을 보여준다 (System)
<br/>&ensp;&emsp;    1. 가능한 투표가 없다면 no votes available 창을 띄운다 (System)
    
-----

<h3> 2. 투표 </h3> 

<img width="320" src="https://user-images.githubusercontent.com/96364048/191235126-ad384678-9c76-429d-8820-9901816e57ad.png">

1. 케이스 명 : 투표
2. 액터명 : User
3. 사전 조건 : 유저 로그인 완료 및 가능한 투표 1개 이상 
4. 이벤트 흐름 : 
<br/>&ensp;  1. 투표 화면을 보여준다 (System)
<br/>&ensp;  2. 투표할 선거의 ..more 링크를 누른다 (User)
<br/>&ensp;  3. 선택된 선거를 불러온다 (System)
<br/>&ensp;  4. 투표 후 submit 버튼을 누른다 (User)
<br/>&ensp;&emsp;    1. 투표한 케이스의 take_endpic == True라면 사진 업로드 화면을 보여준다 (System)
<br/>&ensp;&emsp;    2. 사진을 업로드 한다 (User)
<br/>&ensp;  5. 나머지 투표 화면을 보여준다 (System)
<br/>&ensp;&emsp;    1. 나머지 투표를 진행한다면 2번~4번을 반복한다 (User)
<br/>&ensp;  6. END 버튼을 누른다 (User)
<br/>&ensp;  7. 로그아웃 후 END 화면을 띄운다 (System)

----

<h3> 3. 어드민 세팅 </h3> 

<img width="320" src="https://user-images.githubusercontent.com/96364048/191235137-5835cd48-96f8-4410-9104-9df6c37b0b4f.png">

1. 케이스 명 : 어드민 세팅
2. 액터명 : Admin 
3. 사전 조건 : 어드민 접근 권한이 있는 소셜 로그인 계정 로그인 
4. 이벤트 흐름 : 
<br/>&ensp;  1. 어드민 화면을 보여준다 (System)
<br/>&ensp;  2. 수정, 추가할 모델을 선택한다 (User)
<br/>&ensp;  3. 선택한 모델의 수정 화면을 띄운다 (System)
<br/>&ensp;  4. 선택한 모델을 수정, 추가한다 (User)
<br/>&ensp;  5. 모델 변경사항을 반영한다 (User)
<br/>&ensp;&emsp;    1. 추가적으로 변경할 모델이 있다면 2번~5번을 반복한다 (User)

----

<h3> 4. 투표 결과 조회 </h3> 

<img width="320" src="https://user-images.githubusercontent.com/96364048/191235140-03155538-08c3-488d-b4b7-a9576d5d5b25.png">

1. 케이스 명 : 투표 결과 조회 
2. 액터명 : Admin
3. 사전 조건 : 어드민 접근 권한이 있는 소셜 로그인 계정 로그인 
4. 이벤트 흐름 : 
<br/>&ensp;  1. 어드민 화면을 보여준다 (System)
<br/>&ensp;  2. 상단 header이 POLL RESULT 링크를 클릭한다 (User)
<br/>&ensp;  3. POLL RESULT 화면을 띄운다 (System)
<br/>&ensp;  4. 조회할 투표 케이스를 선택한다 (User)
<br/>&ensp;  5. 선택한 투표 케이스의 시각화 자료들을 보여준다 (System)


