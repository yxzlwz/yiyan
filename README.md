# 异想之旅亿言项目

## 项目背景

本项目的思路来源于[Hitokoto - 一言](https://hitokoto.cn/)，我使用了一个下午的时间基本上完成了复刻，现有句子请求、分类、提交、审核（后两项依赖于异想之旅登录系统）。

## 项目开源

由于**目前异想之旅服务器并不稳定**，加之完整版本由于设计缺陷目前无法开启多线程或多进程，另外提交和审核部分依赖异想之旅登录系统和留言板系统较难供大家适配，因此我们开源了一个可以完成句子获取的简易版本。

该版本每次启动时会与GitHub上的data目录进行同步保证数据处于最新状态。前期我们的句子库并不全，您可以选择使用来自Hitokoto的数据（使用方法详见 **修改配置文件** 部分）

预览地址（完整版，非开源版）：[https://yiyan.yixiangzhilv.com/]()

## 快速上手

1. 确保环境中已经安装 python3.6+ 和 pip3
2. clone项目到本地： `git clone https://github.com/Danny-Yxzl/yiyan.git`
3. 使用pip安装依赖： `pip3 install flask flask_cors requests`
4. 根据自己的需要修改配置文件 `config.py`
5. 使用 `python3 app.py` 或 `uwsgi uwsgi.ini` 命令启动服务

程序默认监听 `0.0.0.0:596` 端口，若想要监听其它端口，请根据自己的启动方式自行修改 `app.py` （最后一行）或 `uwsgi.ini` （很明显的位置）

## 修改配置文件

- `data_from` ：可选值为 `local` 或 `remote` ，分别表示从本地或远端获取句子数据。程序根据您的设定将分别使用 `dir` 或 `url` 中设置的数据文件路径。
- `dir` ：若 `data_from` 值为 `local` 需填写，表示本地data文件夹的位置
- `url` ：若 `data_from` 值为 `remote` 需填写，表示远端data文件夹的请求路径
- `cate` ：目前使用的句子分类代码，也就是目前存在的配置文件名称。

此处举例一个例子方便理解。

若变量设置如下：

```python
data_from = "remote"
url = "https://cdn.jsdelivr.net/gh/Danny-Yxzl/yiyan@master/data/"
cate = "abc"
```

则程序会请求 `https://cdn.jsdelivr.net/gh/Danny-Yxzl/yiyan@master/data/` 目录下的 `a.json` `b.json` `c.json` 三个文件，并分别作为 "原创" "网络" "歌曲" 三个分类的数据保存。

由于只有这三个数据，因此用户请求呼指定请求参数的 `type` 字段时，程序只会返回这三个分类的数据。若用户指定了这三个分类之外的类别，则程序会报错。

分类代码与名称映射详见下表：

```json
{
    "a": "原创",
    "b": "网络",
    "c": "歌曲",
    "d": "文学",
    "e": "影视",
    "f": "游戏",
    "g": "哲学",
    "h": "诗词",
    "i": "动漫/漫画",
    "j": "抖机灵",
    "y": "其它",
    "z": "未知"
}
```

## 用户请求

对于页面，我们有路径 `/` 来获取展示页；对于接口，我们有随机接口 `/get `和指定接口 `/uuid/<uuid>` 来获取数据。

使用 `GET` 方式请求页面  `/`，程序会渲染并返回 `templates/index.html `模板文件。其中，程序渲染时会写入随机的句子；网页前端会通过异想之旅的接口获取必应壁纸作为网页背景。特别说明的是，由于网页字体文件较大，您可以选择删去 `templates/index.html `第11-16行的 `style` 定义来去除字体，加快网页响应。

使用 `GET` 或 `POST` 请求接口 `/get` ，可选传递参数 `type`（GET查询字符串或POST表单均可）。 `type` 指定请求的句子分类，可以填写多个，可选值、格式与 **修改配置文件** 部分中的 `cate` 变量完全相同。

使用 `GET` 或 `POST` 请求接口 `/uuid/<uuid>` ，其中 `<uuid>` 替换为要查询句子的uuid。就是一个通过uuid获取句子的接口，没啥好说的。

## 帮助我们

作为一个数据共享平台，我们需要大量的优质句子输入素材库。我们会持之以恒地做这件事，也恳请您帮助我们提交一些您原创或搜集到的句子：[提交句子 - 异想之旅亿言](https://yiyan.yixiangzhilv.com/user/new)。

如果您愿意赞助我们资金或服务器，那就再好不过了。

您可以通过微信公众号 异想之旅 或邮箱地址 [mail@yixiangzhilv.com](mailto:mail@yixiangzhilv.com) 联系到我们。
