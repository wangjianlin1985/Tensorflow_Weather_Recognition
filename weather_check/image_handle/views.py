import os
import numpy as np
from PIL import Image
from django.conf import settings
from django.shortcuts import render
from .models import ImageCheck
from utils import restful
from utils.image_check import check_handle


def index(request):
    return render(request, 'index.html')


def check(request):
    return render(request, 'check.html')


def upload_img(request):
    # 图片上传
    file = request.FILES.get('file')
    file_name = file.name
    with open(os.path.join(settings.MEDIA_ROOT, file_name), 'wb') as f:
        for chunk in file.chunks():
            f.write(chunk)
    upload_url = request.build_absolute_uri(settings.MEDIA_URL + file_name)
    try:
        ImageCheck.objects.create(file_name=file_name, file_url=upload_url)
    except ImageCheck:
        return restful.server_error(message='数据库发生错误！')
    return restful.ok(data={'url': upload_url})


def check_img(request):
    # 图片检测
    image_url = request.POST.get('img_url')
    if not image_url:
        return restful.params_error(message='缺少必要的参数image_url')
    image_name = image_url.rsplit('/')[-1]
    image_path = os.path.join(settings.MEDIA_ROOT, image_name)
    pred_name = check_handle(image_path)

    try:
        obj = ImageCheck.objects.filter(file_name=image_name).last()
        obj.check_result = pred_name
        obj.save()
    except:
        return restful.server_error(message='数据库发生错误')
    return restful.ok(data={'flower': pred_name, 'chance': str(pred_name) or '0'})
