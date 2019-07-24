from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader, RequestContext
from booktest.models import BookInfo
from PIL import Image, ImageDraw, ImageFont
import random
# Create your views here.

def login_required(view_func):
    '''判断用户是否登录的装饰器Z'''
    def wrapper(request, *view_args, **view_kwargs):
        if request.session.has_key('islogin'):
            return view_func(request, *view_args, **view_kwargs)
        else:
            return redirect('/login')
    return wrapper


# django中的render就是下面的实现方法
def my_render(request, template_path, context={}):
    # 1加载模板文件，获取一个模板对象
    temp = loader.get_template(template_path)

    # 2。定义模板上下文，给模板传数据
    context = RequestContext(request, context)
    # 3. 渲染模板，产生后替换一个html内容
    res_html = temp.render(context)

    # 4。返回应答
    return HttpResponse(res_html)

# @login_required
def index(request):
    # return my_render(request, 'booktest/index.html')
    return render(request, 'booktest/index.html')

def index2(request):
    '''模板文件加载顺序'''
    render(request, 'booktest/index2.html')

def temp_var(request):
    '''模板变量'''
    # my_dict = {'title': '字典键值'}
    # my_list = [1, 2, 3]
    book = BookInfo.objects.get(id=1)

    # context = {'my_dict': my_dict, 'my_list': my_list}
    return render(request, 'booktest/temp_var.html', {'book': book})


def verify_code(request):
    '''随机验证码'''
    # 1.创建画面对象
    # 定义变量，用于画面的背景色、宽、高
    bgcolor = (255, 255, 255)
    width = 200
    height = 45

    im = Image.new('RGB', (width, height), bgcolor)
    # 2.创建画笔对象
    draw = ImageDraw.Draw(im)
    # 3.调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        draw.point(xy, fill=fill)
    # 调用画笔的point()函数绘制6条干扰线
    for i in range(6):
        x1 = int(random.randrange(0, width))
        y1 = int(random.randrange(0, height))
        x2 = int(random.randrange(0, width))
        y2 = int(random.randrange(0, height))
        fill = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        draw.line([(x1, y1), (x2, y2)], fill=fill, width=2)

    # 4.定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456klmnopqrstuvwsyzLMNOPQRS789TUVWXYZ0abcdefghij'
    # 随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    # 构造字体对象，ubuntu的字体路径为“/usr/share/fonts/truetype/freefont”
    # 构造字体类型和大小
    font = ImageFont.truetype('FreeMono.ttf', random.randrange(23, 40))
    # 绘制4个字
    draw.text((15, 10), rand_str[0], font=font, fill=random.randrange(0, 255))
    draw.text((65, 10), rand_str[1], font=font, fill=random.randrange(0, 255))
    draw.text((120, 10), rand_str[2], font=font, fill=random.randrange(0, 255))
    draw.text((175, 10), rand_str[3], font=font, fill=random.randrange(0, 255))
    # 5.释放画笔
    del draw
    # 6.存入session，用于做进一步验证
    # request.session['verifycode'] = rand_str

    # 内存文件操作(python2)
    # import cStringIO
    # buf = cStringIO.StringIO()

    # 内存文件操作(python3)
    from io import BytesIO
    buf = BytesIO()
    # 7.将图片保存在内存中，文件类型为png
    im.save(buf, 'png')
    # 8.将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'image/png')


def url_reverse(request):
    '''url反向解析页面'''
    return render(request, 'booktest/url_reverse.html')

def show_arg(request, a,b):
    '''url反向解析页面捕获参数'''
    return HttpResponse('页面参数='+a+':'+b)

def show_kwargs(request, c, d):
    '''捕获关键字参数'''
    return HttpResponse(c+':'+d)























