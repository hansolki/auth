from django.db import models
from accounts.models import User #=> 방법1
from django.conf import settings #=> 방법2
from django.contrib.auth import get_user_model #=> 방법3
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    # 유저모델 참조
    
    # 방법1-직접적으로 가져와서 사용하는 방법(권장 X)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    # 방법2 - setting.py에 설정해놓은 변수 가져오기 (권장)
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)

    # 방법3(권장)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)