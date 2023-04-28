from django.db import models
from users.models import User

# Create your models here.

class TodoList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    is_complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completion_at = models.DateTimeField(null=True,blank=True)
    def __str__(self):
        return str(self.title)

""" 2. title : 할일 제목입니다.
    3. is_complete : 완료 여부입니다. 데이터 타입은 `boolean`이며 default false 설정을 합니다. 
    4. created_at : 할일 생성 시간입니다.
    5. updated_at : 할일의 마지막 수정 시간입니다.
    6. completion_at : 할일 완료 시간입니다.
    7. user_id : 사용자 테이블과 FK로 관계형성이 되어야합니다. """
