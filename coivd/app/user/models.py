from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

# AbstractBaseUser 是基本骨架，只有 3 个项： password, last_login, is_active。


class User(AbstractUser):
    name = models.CharField(verbose_name="用户名", max_length=64)
    # loving_user = models.ManyToManyField('User', verbose_name="关注的人", related_name="loving_users", blank=True)
    # loved_user = models.ManyToManyField('User', verbose_name="被谁关注", related_name="loved_users", blank=True)
    create_time = models.DateTimeField("创建时间", auto_now_add=True)
    update_time = models.DateTimeField("修改时间", auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        abstract = False
        verbose_name = '用户表'
        verbose_name_plural = verbose_name



