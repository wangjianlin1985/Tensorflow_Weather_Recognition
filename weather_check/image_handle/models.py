from django.db import models


class ImageCheck(models.Model):
    file_name = models.CharField(max_length=200, verbose_name='图片名')
    file_url = models.CharField(max_length=250, verbose_name='图片URL')
    check_result = models.CharField(max_length=100, verbose_name='识别结果', blank=True)
    check_time = models.DateTimeField(auto_now_add=True, verbose_name='检测时间')

    class Meta:
        db_table = 'image_check'
        verbose_name = '图片检测'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.file_name
