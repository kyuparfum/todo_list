# todo_list
DRF(Django Rest Framework)를 사용해서 작업한 부트캠프 django심화 프로젝트입니다.
# API명세
#### users
- 회원리스트조회
  - GET userlist/ 
- 회원가입
  - POST signup/
- 회원정보수정
  - PUT <int:user_id>/
- 회원탈퇴
  - DELETE <int:user_id>/

#### todos
- 할일 조회
  - GET 
- 할일 추가
  - POST todo/
- 할일 수정
  - PUT todo/<int:todo_list_id>
- 할일 삭제
  - DELETE todo/<int:todo_list_id>
