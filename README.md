# markdown2mindnode
convert markdown list to mindnode format

* [痛点](#痛点)
* [环境配置](#环境配置)
* [如何使用](#如何使用)
* [Workflow截屏](#workflow截屏)
* [常见问题](#常见问题)
* [TODO](#todo)
* [关于作者](#关于作者)

------

## 痛点

最近想使用「思维导图」帮助整理所学知识点，于是找到了mac端利器「MindNode」，对于习惯了markdown文字编写的人来说，在GUI下新建节点的方式不是很习惯，于是思考能否通过markdown格式直接转换为思维导图格式呢？于是就有了这个十分简单的小项目

> 「幕布」是支持类似markdown格式书写，自动转换为思维导图的，但是由于颜值和使用体验等放弃了

<br/>

## 环境配置

该项目的开发环境是

- **操作系统**：macOS Catalina 10.15.4
- **python环境**：Python 3.7.4
- **主要依赖**：pyperclip==1.8.0

⚠️MindNode为mac端软件，windows请咨询寻找类似思维导图软件，但不保证有相同的流程

>  主要确保python3的环境没问题基本就可以，在macOS较低版本和Window10上都测试过没问题，但是对于只有python2的环境来说可能存在一些「常见问题」

<br/>

## 如何使用

1. clone该项目到本地

2. 编写`.md`文件（⚠️现在只支持无序列表格式）

3. 打开`Terminal`执行shell脚本

   ```bash
   cd markdown2mindnode
   ./markdown2mindnode.sh [你的.md文件] [参数]
   # 示例: 
   # 1) ./markdown2mindnode.sh /User/doublez/Downloads/README.md
   # 2) ./markdown2mindnode.sh /User/doublez/Downloads/README.md clipboard
   # 2) ./markdown2mindnode.sh /User/doublez/Downloads/README.md file
   ```

4. 默认情况结果将复制到剪贴板中，可以直接粘贴到`MindNode`中

   - 如果输入`file`参数则会在`.md`文件同一目录新建`[filename]_refactor.md`文件存储结果

------

5. 可以通过修改`.bash_alias`快速执行以上功能

   ```bash
   # md2mn快捷指令
   echo "alias md2mn='sh /[clone文件的目录]/markdown2mindnode/markdown2mindnode.sh'"
   
   # 每次登陆终端时刷新.bash_alias文件
   echo "source ~/.bash_aliases" >> ~/.bash_profile
   ```

6. 这样每次只需在任何位置启动`Terminal`

   ```bash
   md2mn [.md文件路径]
   
   # 预期输出结果
   # /Users/xxx/markdown2mindnode
   # Requirement already satisfied: pyperclip==1.8.0 in /Users/doublez/opt/anaconda3/lib/python3.7/site-packages (from -r requirements.txt (line 1)) (1.8.0)
   # By default, the transformed content is copied to clipboard.
   # Successfully saved to clipboard!
   ```

<br/>

## Workflow截屏

1. 编写`.md`文件

   <img src="https://upload-images.jianshu.io/upload_images/12014150-02b69b35b0a74761.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" alt="markdown.png" width="50%;" />

2. 执行脚本

   ![workflow_1.gif](https://upload-images.jianshu.io/upload_images/12014150-66e9b347f5bbba27.gif?imageMogr2/auto-orient/strip)

3. 粘贴到`MindNode`中

   <img src="https://upload-images.jianshu.io/upload_images/12014150-8e584e4fbba03593.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" alt="mindnode.png" width="50%;" />

<br/>

## 常见问题

1. `TypeError: 'encoding' is an invalid keyword argument for this function`
   - 大概率是由于所用的环境是python2
   - macOS自带python2环境，切换python3环境请自行google
2. 安装`requirement.txt`中`pyperclip`依赖报错
   - 大概率是pip的问题，建议更换源或直接在命令行中执行`pip install pyperclip`
   - https://pypi.org/project/pyperclip/
3. 粘贴到MindNode中出错 或 样式不匹配
   - 该项目现只搭好框架
   - markdown语法只支持无序list，请检查markdown内容
   - 后续有时间会考虑处理复杂md文件，敬请谅解...

<br/>

## TODO

- [x] workflow框架搭建
- [x] markdown无序list
  - [x] 多级无序列表
- [x] 文件路径或文件名中有空格
- [ ] 支持更复杂的markdown语法
- [ ] 支持图片的添加

<br/>

## 关于作者

| 姓名 \| Name:bust_in_silhouette: | 张喆 \| doubleZ          |
| -------------------------------- | ------------------------ |
| 学校 \| University:school:       | 同济大学 \| Tongji Univ. |
| 联系方式 \| Email:email:         | dbzdbz@tongji.edu.cn     |
