from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, RequestContext
from booktest.models import BookInfo
# Create your views here.

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

























