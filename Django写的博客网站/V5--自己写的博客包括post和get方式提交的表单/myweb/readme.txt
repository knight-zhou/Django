﻿(1)当请求一个页面时,Django创建一个 HttpRequest 对象.
该对象包含 request 的元数据.
然后 Django 调用相应的 view 函数(HttpRequest 对象自动传递给该view函数<作为第一个参数>),
每一个 view 负责返回一个 HttpResponse 对象.


（3）对于表单的提交，如果没有写if method == "GET",默认就是 if methond == "POST"之外的就是post，

对于是GET的默认就是  return HttpResponse(u"内容.....")