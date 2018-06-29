import random
from io import BytesIO

from PIL import Image, ImageDraw, ImageFont
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def get_verity_code(request):
    #画布 画笔
    image_size=(200,100)#画布宽高
    image_color=(255,0,0)#背景颜色
    image=Image.new("RGB",image_size,image_color)#画布(颜色,图的尺寸,)
    image_draw=ImageDraw.Draw(image,"RGB")#画笔(画布,选色模式)
    image_font=ImageFont.truetype("/home/liuzhen/cyzm/HelloDjango/static/fonts/ADOBEARABIC-BOLD.OTF",size=60)#字体样式和大小
    source_str="qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM123456789"#字符串的源
    dest_str=""
    for i in range(4):
       r=random.randrange(len(source_str))
       dest_str +=source_str[r]
    for i in range(4):
        image_draw.text((20+40*i,20),dest_str[i],font=image_font)
    #image_draw.text((20,20),"R",font=image_font)#画一个R
    #此时整幅画在内存
    buffer=BytesIO()#实例化一个IO(input,output)流转换为图片流
    image.save(buffer,"png")#存放在流中格式为png
    return HttpResponse(buffer.getvalue(),content_type="image/png")#从io流中取值,打开类型每个mime有两部分组成前面是数据的大类型后面是电一的具体的种类

urls:
from django.conf.urls import url

from App import views

urlpatterns=[
    url(r'^getverity/',views.get_verity_code)
]
#加入包static复制fonts在image_font中复制copy path
setting:
STATIC_URL = '/static/'
STATICFILES_DIRS=[
os.path.join(BASE_DIR,'static')]

