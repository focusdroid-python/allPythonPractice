from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader,RequestContext


def my_render(request, template_path, context_dict={}):

    # 使用模板文件
    # 1.加载模板文件, temp是模板对象
    temp = loader.get_template(template_path)
    # 2. 定义上下文，给模板文件传递数 据
    context = RequestContext(request, context_dict)
    # 3. 模板渲染：产生标准的html内容
    res_html = temp.render(context)

    return HttpResponse(res_html)



# Create your views here.

# 1.定义视图函数， HttpResponse
# 2. 进行url配置，建立url地址和视图的对应关系
# http://127.0.0.1:8000/index
def index(request):
    # 进行处理，和M，T进行交互
    # return HttpResponse('Hello Django')
    #
    # # 使用模板文件
    # # 1.加载模板文件, temp是模板对象
    # temp = loader.get_template('booktest/index.html')
    # # 2. 定义上下文，给模板文件传递数据
    # context = RequestContext(request, {})
    # # 3. 模板渲染：产生标准的html内容
    # res_html = temp.render(context)
    #
    # return HttpResponse(res_html)

    # 使用自己封装的
    # return my_render(request, 'booktest/index.html')

    # 使用系统render渲染
    return render(request, 'booktest/index.html', {'content': '这是传递的字段', 'list':list(range(1,10))})



def login(request):
    return HttpResponse('<h1>登录</h1>')