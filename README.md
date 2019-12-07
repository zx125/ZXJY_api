## 在你的Python环境下安装该项目所用依赖(packages.txt)
```python
pip install -r packages.txt
```

## 数据库配置
```python
1、创建数据库名为 luffy，编码采用 utf-8
2、创建该数据库操作用户：账号 - luffy 密码 - Luffy123?
3、完成数据库迁移：python manage_prod.py migrate
4、创建超级管理员：python manage_prod.py createsuperuser
5、自行添加测试数据(/xadmin)
```
```sql
INSERT INTO `luffy_teacher` VALUES ('1', '0', '1', '2019-07-14 13:44:19.661327', '2019-07-14 13:46:54.246271', 'Alex', '1', '老男孩Python教学总监', '金角大王', 'teacher/alex_icon.png', '老男孩教育CTO & CO-FOUNDER 国内知名PYTHON语言推广者 51CTO学院20162017年度最受学员喜爱10大讲师之一 多款开源软件作者 曾任职公安部、飞信、中金公司、NOKIA中国研究院、华尔街英语、ADVENT、汽车之家等公司', '1');
INSERT INTO `luffy_teacher` VALUES ('2', '0', '1', '2019-07-14 13:45:25.092902', '2019-07-14 13:45:25.092936', 'Mjj', '0', '前美团前端项目组架构师', null, 'teacher/mjj_icon.png', '是马JJ老师, 一个集美貌与才华于一身的男人，搞过几年IOS，又转了前端开发几年，曾就职于美团网任高级前端开发，后来因为不同意王兴(美团老板)的战略布局而出家做老师去了，有丰富的教学经验，开起车来也毫不含糊。一直专注在前端的前沿技术领域。同时，爱好抽烟、喝酒、烫头(锡纸烫)。 我的最爱是前端，因为前端妹子多。', '2');
INSERT INTO `luffy_teacher` VALUES ('3', '0', '1', '2019-07-14 13:46:21.997846', '2019-07-14 13:46:21.997880', 'Lyy', '0', '老男孩Linux学科带头人', null, 'teacher/lyy_icon.png', 'Linux运维技术专家，老男孩Linux金牌讲师，讲课风趣幽默、深入浅出、声音洪亮到爆炸', '3');
INSERT INTO `luffy_course_category` VALUES ('1', '0', '1', '2019-07-14 13:40:58.690413', '2019-07-14 13:40:58.690477', 'Python', '1');
INSERT INTO `luffy_course_category` VALUES ('2', '0', '1', '2019-07-14 13:41:08.249735', '2019-07-14 13:41:08.249817', 'Linux', '2');
INSERT INTO `luffy_course` VALUES ('1', '0', '1', '2019-07-14 13:54:33.095201', '2019-07-14 13:54:33.095238', 'Python开发21天入门', 'courses/alex_python.png', '0', 'Python从入门到入土&&&Python从入门到入土&&&Python从入门到入土&&&Python从入门到入土&&&Python从入门到入土&&&Python从入门到入土&&&Python从入门到入土&&&Python从入门到入土&&&Python从入门到入土&&&Python从入门到入土&&&Python从入门到入土&&&Python从入门到入土', '0', '2019-07-14', '21', '', '0', '231', '120', '120', '0.00', '1', '1', '1');
INSERT INTO `luffy_course` VALUES ('2', '0', '1', '2019-07-14 13:56:05.051103', '2019-07-14 13:56:05.051142', 'Python项目实战', 'courses/mjj_python.png', '0', '', '1', '2019-07-14', '30', '', '0', '340', '120', '120', '99.00', '1', '2', '2');
INSERT INTO `luffy_course` VALUES ('3', '0', '1', '2019-07-14 13:57:21.190053', '2019-07-14 13:57:21.190095', 'Linux系统基础5周入门精讲', 'courses/lyy_linux.png', '0', '', '0', '2019-07-14', '25', '', '0', '219', '100', '100', '39.00', '2', '3', '3');
INSERT INTO `luffy_course_chapter` VALUES ('1', '0', '1', '2019-07-14 13:58:34.867005', '2019-07-14 14:00:58.276541', '1', '计算机原理', '', '2019-07-14', '1', '1');
INSERT INTO `luffy_course_chapter` VALUES ('2', '0', '1', '2019-07-14 13:58:48.051543', '2019-07-14 14:01:22.024206', '2', '环境搭建', '', '2019-07-14', '1', '2');
INSERT INTO `luffy_course_chapter` VALUES ('3', '0', '1', '2019-07-14 13:59:09.878183', '2019-07-14 14:01:40.048608', '1', '项目创建', '', '2019-07-14', '2', '3');
INSERT INTO `luffy_course_chapter` VALUES ('4', '0', '1', '2019-07-14 13:59:37.448626', '2019-07-14 14:01:58.709652', '1', 'Linux环境创建', '', '2019-07-14', '3', '4');
INSERT INTO `luffy_course_section` VALUES ('1', '0', '1', '2019-07-14 14:02:33.779098', '2019-07-14 14:02:33.779135', '计算机原理上', '1', '2', null, null, '2019-07-14 14:02:33.779193', '1', '1');
INSERT INTO `luffy_course_section` VALUES ('2', '0', '1', '2019-07-14 14:02:56.657134', '2019-07-14 14:02:56.657173', '计算机原理下', '2', '2', null, null, '2019-07-14 14:02:56.657227', '1', '1');
INSERT INTO `luffy_course_section` VALUES ('3', '0', '1', '2019-07-14 14:03:20.493324', '2019-07-14 14:03:52.329394', '环境搭建上', '1', '2', null, null, '2019-07-14 14:03:20.493420', '0', '2');
INSERT INTO `luffy_course_section` VALUES ('4', '0', '1', '2019-07-14 14:03:36.472742', '2019-07-14 14:03:36.472779', '环境搭建下', '2', '2', null, null, '2019-07-14 14:03:36.472831', '0', '2');
INSERT INTO `luffy_course_section` VALUES ('5', '0', '1', '2019-07-14 14:04:19.338153', '2019-07-14 14:04:19.338192', 'web项目的创建', '1', '2', null, null, '2019-07-14 14:04:19.338252', '1', '3');
INSERT INTO `luffy_course_section` VALUES ('6', '0', '1', '2019-07-14 14:04:52.895855', '2019-07-14 14:04:52.895890', 'Linux的环境搭建', '1', '2', null, null, '2019-07-14 14:04:52.895942', '1', '4');
INSERT INTO `luffy_banner` VALUES ('1', '0', '1', '2019-11-28 10:14:35.126488', '2019-11-28 10:14:35.126488', 'banner1', '/free', 'banner/banner1.png', 'banner1 banner1 banner1', '4');
INSERT INTO `luffy_banner` VALUES ('2', '0', '1', '2019-11-28 10:14:58.123032', '2019-11-28 10:14:58.123032', 'banner2', '/course', 'banner/banner2.png', 'banner2 banner2 banner2', '3');
INSERT INTO `luffy_banner` VALUES ('3', '0', '1', '2019-11-28 10:15:20.899073', '2019-11-28 10:15:20.899073', 'banner3', '/light-course', 'banner/banner3.png', 'banner3 banner3 banner3', '2');
INSERT INTO `luffy_banner` VALUES ('4', '0', '1', '2019-11-28 10:16:13.818569', '2019-11-28 10:16:13.818569', 'banner4', 'https://www.baidu.com', 'banner/banner4.png', 'banner4 banner4 banner4', '1');
```
