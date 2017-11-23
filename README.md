# 基于图灵机器人的API接口测试框架
# Python+requests+unittest+Excel

1：所有接口数据参数以字典形式存入Excel文件中
![excel_test](https://github.com/huguishun/Python_API/blob/master/img/excel_test.png)

2：使用unittest模块来进行接口断言以及生成HTMLtestrunner测试报告
![htmltestrunner](https://github.com/huguishun/Python_API/blob/master/img/htmltestrunner.png)

3：通过读取ini文件中的邮件地址来发送带有HTMLtestrunner附件的邮件
![email_test](https://github.com/huguishun/Python_API/blob/master/img/email_test.png)

注：测试报告生成路径在report文件中

# 使用说明：
1，配置ini文件参数
2，运行runmain.py执行测试操作并发送邮件
