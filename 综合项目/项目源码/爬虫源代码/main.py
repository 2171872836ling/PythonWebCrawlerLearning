import tkinter as tk
from tkinter import ttk # 在绘制圆角组件的样式有
from tkinter import messagebox
from PIL import Image, ImageTk
import time
import os
from GetPriceClass import CrawlDatas
"""
分辨率：1920x1080为模板(窗口大小960x540)
底色      #333333
二层色    #353535
三层色    #3F3F3F
输入框    #6B6B6B
点击色    #535353
字体色    white
标题字体大小：28pt~36pt
正文字体大小：24pt~28pt
项目符号和列表：20pt~24pt
脚注和引用：16pt~18pt
图表和图片：2pt~14pt
隐藏原生标题栏（根据系统定制的标题栏）后，要自定义放大，缩小，关闭
图片考虑到原生库无法调整放缩和放缩后导致的质量问题，这里使用PIL的库
text:组件文本
bg:背景颜色
"""

# 全局变量
cds = CrawlDatas()
crawling_type_select=1186# 爬取类型
save_type_select="1"# 保存类型
get_num="" # 爬取数量
return_information=""# 爬取后的结果
# ========================组件======================== #
# -----------标题按钮-------------#
def main_healing():
    def open_url():
        # 因为是windows系统展示，我没用webbrowser库打开俩，是直接用os的cmd指令
        os.system("start http://www.xinfadi.com.cn/priceDetail.html")
    # 标题（点击可以进入url）
    healing=tk.Button(
        root,
        text="物价爬虫分析",
        fg="white",
        bg="#333333",  # 背景色与窗口一致
        font=("宋体", 30),
        borderwidth=0,  # 无边框
        activebackground="#333333",
        activeforeground="black",
        command=open_url
    )
    healing.place(
        relx=0.5,
        rely=0.01,
        anchor="n",
        relwidth=0.3,
        relheight=0.1
    )

# -----------爬取类型选项-------------#

def crawling_type_radiobutton():
    # 创建回调函数返回变量值
    def on_selection():
        global crawling_type_select  # 必须是全局变量
        crawling_type_select=crawling_var.get()
        # print(crawling_var.get())

    crawling_var = tk.IntVar()  # 创建一个 IntVar 对象
    # 创建单选框
    vegetable = tk.Radiobutton(root, text="蔬菜",variable=crawling_var, value=1186, font=("宋体", 25), activeforeground="white", fg="white", bg="#333333", activebackground="#333333",borderwidth=0 ,selectcolor="black", command=on_selection)
    fruit = tk.Radiobutton(root, text="水果", variable=crawling_var, value=1187, font=("宋体", 25), activeforeground="white", fg="white", bg="#333333", activebackground="#333333",borderwidth=0 ,selectcolor="black", command=on_selection)
    Meat_poultry_eggs = tk.Radiobutton(root, text="肉禽蛋", variable=crawling_var, value=1188, font=("宋体", 25), activeforeground="white", fg="white", bg="#333333", activebackground="#333333",borderwidth=0 ,selectcolor="black", command=on_selection)
    aquatic_product = tk.Radiobutton(root, text="水产", variable=crawling_var, value=1189, font=("宋体", 25), activeforeground="white", fg="white", bg="#333333", activebackground="#333333",borderwidth=0 ,selectcolor="black", command=on_selection)
    grain_oil = tk.Radiobutton(root, text="粮油", variable=crawling_var, value=1190, font=("宋体", 25), activeforeground="white", fg="white", bg="#333333", activebackground="#333333",borderwidth=0 ,selectcolor="black", command=on_selection)
    bean_products = tk.Radiobutton(root, text="豆制品", variable=crawling_var, value=1203, font=("宋体", 25), activeforeground="white", fg="white", bg="#333333", activebackground="#333333",borderwidth=0 ,selectcolor="black", command=on_selection)
    seasoning = tk.Radiobutton(root, text="调料类", variable=crawling_var, value=1204, font=("宋体", 25), activeforeground="white", fg="white", bg="#333333", activebackground="#333333",borderwidth=0 ,selectcolor="black", command=on_selection)

    # 布局
    vegetable.place(relx=0.05, rely=0.23, anchor="center")
    fruit.place(relx=0.17, rely=0.23, anchor="center")
    Meat_poultry_eggs.place(relx=0.3, rely=0.23, anchor="center")
    aquatic_product.place(relx=0.45, rely=0.23, anchor="center")
    grain_oil.place(relx=0.60, rely=0.23, anchor="center")
    bean_products.place(relx=0.75, rely=0.23, anchor="center")
    seasoning.place(relx=0.9, rely=0.23, anchor="center")

    # 设置默认选中的单选框
    crawling_var.set(1186)  # 默认选中第一个单选框






# -----------保存类型选项-------------#

def save_type_radiobutton():
    # 创建回调函数返回变量值
    def on_selection():
        global save_type_select  # 必须是全局变量
        save_type_select=save_var.get()
        # print(save_type_select)
    save_var = tk.IntVar()  # 创建一个 IntVar 对象
    # 创建一个全局变量来存储选中的单选框的值
    # 创建单选框
    josn_type = tk.Radiobutton(root, text="xlsx",variable=save_var, value="1", font=("宋体", 25), activeforeground="white", fg="white", bg="#333333", activebackground="#333333",borderwidth=0 ,selectcolor="black", command=on_selection)
    scv_type = tk.Radiobutton(root, text="josn", variable=save_var, value="2", font=("宋体", 25), activeforeground="white", fg="white", bg="#333333", activebackground="#333333",borderwidth=0 ,selectcolor="black", command=on_selection)
    xlsx_type = tk.Radiobutton(root, text="scv", variable=save_var, value="3", font=("宋体", 25), activeforeground="white", fg="white", bg="#333333", activebackground="#333333",borderwidth=0 ,selectcolor="black", command=on_selection)

    # 布局
    josn_type.place(relx=0.2, rely=0.43, anchor="center")
    scv_type.place(relx=0.45, rely=0.43, anchor="center")
    xlsx_type.place(relx=0.8, rely=0.43, anchor="center")


    # 设置默认选中的单选框
    save_var.set("1")  # 默认选中第一个单选框






# 自定义圆角矩形绘制方法
def create_rounded_rect(self, x1, y1, x2, y2, radius=10, **kwargs):
    """
    在Canvas上绘制圆角矩形
    :param self: Canvas对象
    :param x1: 矩形左上角x坐标
    :param y1: 矩形左上角y坐标
    :param x2: 矩形右下角x坐标
    :param y2: 矩形右下角y坐标
    :param radius: 圆角半径
    :param kwargs: 其他Canvas绘图参数
    :return: 创建的图形对象ID
    """
    points = [
        x1 + radius, y1,
        x2 - radius, y1,
        x2, y1,
        x2, y1 + radius,
        x2, y2 - radius,
        x2, y2,
        x2 - radius, y2,
        x1 + radius, y2,
        x1, y2,
        x1, y2 - radius,
        x1, y1 + radius,
        x1, y1,
    ]
    return self.create_polygon(points, **kwargs, smooth=True)
# 将自定义方法绑定到Canvas类
tk.Canvas.create_rounded_rect = create_rounded_rect

def layout_entry(rx=0.7, ry=0.6,rw=0.2,rh=0.1):
    def update_layout(event):
        """
        窗口大小改变时的回调函数
        动态调整圆角矩形、输入框大小和字体大小
        :param event: 包含窗口尺寸信息的event对象
        """
        # 清除Canvas上所有内容
        canvas.delete("all")

        # 获取当前Canvas尺寸
        width = event.width
        height = event.height

        # 计算圆角半径（不超过20像素，且为高度的30%）
        radius = min(90, height * 0.3)

        # 绘制新的圆角矩形背景
        canvas.create_rounded_rect(
            0, 0, width, height,
            radius=radius,
            fill="#f8f8f8",  # 边框内填充颜色
            outline="#333333"  # 边框颜色
        )

        # 计算新的字体大小（不小于10像素，且为高度的30%）
        new_font_size = max(25, int(height * 0.3))

        # 更新Entry的字体样式（确保字体大小动态改变）
        font = ("Arial", new_font_size)
        style.configure("Rounded.TEntry", font=font)
        entry.configure(font=font)  # 直接更新Entry的字体

        # 更新Entry的位置和大小（保持居中，宽度80%，高度70%）
        entry.place_configure(
            relx=0.5,
            rely=0.5,
            anchor="center",
            relwidth=0.8,
            relheight=0.7
        )


    # 创建自定义ttk样式
    style = ttk.Style()
    # 初始字体大小
    initial_font = ("宋体", 25)
    style.configure(
        "Rounded.TEntry",  # 样式名称
        borderwidth=0,  # 无边框
        relief="flat",  # 扁平样式
        padding=1,  # 内边距
        background="#333333",  # 背景色与Canvas一致
        font=initial_font  # 初始字体
    )

    # 创建主框架（占窗口80%宽度、20%高度，居中，改变位置）
    main_frame = tk.Frame(root, bg="white")
    main_frame.place(
        relx=rx,  # 水平居中
        rely=ry,  # 垂直居中
        anchor="w",  # 中心锚点
        relwidth=rw,  # 相对宽度80%
        relheight=rh  # 相对高度20%
    )

    # 创建Canvas用于绘制动态圆角背景
    canvas = tk.Canvas(
        main_frame,
        bg="#333333",  # 圆角边框外颜色（重要）
        highlightthickness=0,  # 无高亮边框
        bd=0  # 无边框
    )
    # 创建输入框（使用自定义样式）
    entry = ttk.Entry(
        main_frame,
        style="Rounded.TEntry",
        font=initial_font  # 设置初始字体
    )

    # 布局
    canvas.place(relx=0, rely=0, relwidth=1, relheight=1)  # 使用place布局，让Canvas填充整个主框架
    canvas.bind("<Configure>", update_layout)  # 绑定Canvas大小改变事件
    entry.place(
        relx=0.1,  # 水平居中
        rely=0.3,  # 垂直居中
        anchor="center",  # 中心锚点
        relwidth=0.9,  # 相对宽度90%
        relheight=0.8  # 相对高度60%
    )
    return entry

def button_entry_clear_and_sure(entry):
    # 清空按钮事件
    def clear_button_founation():
        entry.delete(0, "end")

    # 确认按钮事件
    def sure_button_founation():
        global get_num
        get_num=entry.get()
        sure_button_crawl_datas()

    # 创建组件
    sure_button = tk.Button(root, text="提交", command=sure_button_founation, width=10, height=2, bd=0)
    clear_button = tk.Button(root, text="清空", command=clear_button_founation, width=10, height=2, bd=0)
    # 布局
    sure_button.place(
        relx=0.6,
        rely=0.7,
        relwidth=0.2,
        relheight=0.1
    )
    clear_button.place(
        relx=0.1,
        rely=0.7,
        relwidth=0.2,
        relheight=0.1
    )


# --------------转换输入类型，结合CrawlDatas类调用函数----------------#
def sure_button_crawl_datas():
    global cds,crawling_type_select, save_type_select ,get_num,return_information# 必须在try外面，否者会导致变量赋值错误，认为get_num局部变量
    try:

        get_num = int(get_num.strip())
        save_type_select=str(save_type_select)
        return_information=cds.save_style(josn_datas=cds.get_price_datas(get_num, crawling_type_select),select_save_style=save_type_select)
        print(return_information)
        # -------------------爬取提示---------------------#
        label_get = tk.Label(root, text="爬取结果:" +return_information, font=("宋体", 18), bg="#333333", fg="white",borderwidth=0)#清空报错
        label_get.place(rely=0.85,anchor="w")  # relx组建位置比例，anchor组件锚点，relwidth组建大小比例
    except ValueError or TypeError:
        return_information="值输入异常,请重新输入!"
        input_entry.delete(0, "end")




if __name__ == '__main__':
    # ========================创建主窗口======================== #
    def on_resize(event):
        new_font_size = max(16, int(event.height / 20))  # 文字大小至少16，随着分辨率改变，不是窗口缩放
        # 动态调整组件大小,位置。文字大小
        label.config(width=event.width, height=event.height, font=("Arial", new_font_size))


    root = tk.Tk()
    root.title("自适应布局示例")
    root.geometry("960x540")
    root.configure(bg="#333333")  # 设置整个窗口的背景颜色为黑色
    root.attributes("-alpha", 0.99)  # 设置透明度为 99%
    root.resizable(True, True)  # 设置是否可以缩放
    # root.bind("<Configure>", on_resize) # 绑定窗口大小变化事件


    main_healing()#标题
    # -----------爬取类型选项提示-------------#
    label_get_num = tk.Label(root, text="【请输入选择物品的类型】", font=("宋体", 22), bg="#333333", fg="white",
                             borderwidth=0)
    label_get_num.place(relx=0.5, rely=0.15, anchor="center", relwidth=1,
                        relheight=0.05)  # relx组建位置比例，anchor组件锚点，relwidth组建大小比例
    # 调用爬取类型选项单选框
    crawling_type_radiobutton()


    # -----------保存数据类型选项提示-------------#
    label_get_num = tk.Label(root, text="【请输入保存数据的类型】", font=("宋体", 22), bg="#333333", fg="white",
                             borderwidth=0)
    label_get_num.place(relx=0.5, rely=0.35, anchor="center", relwidth=1,
                        relheight=0.05)  # relx组建位置比例，anchor组件锚点，relwidth组建大小比例
    # 调用保存数据类型选项单选框
    save_type_radiobutton()

    # -----------爬取数据类型选项提示-------------#
    label_get_num = tk.Label(root, text="请输入爬取条数物价的数量（10万条以上需等待半分钟）", font=("宋体", 20), bg="#333333", fg="white",borderwidth=0)
    label_get_num.place(rely=0.6, anchor="w", relheight=0.2)#relx组建位置比例，anchor组件锚点，relwidth组建大小比例

    #输入框
    input_entry=layout_entry()
    # 清空提交按钮
    button_entry_clear_and_sure(input_entry)


    # 启动事件循环，使窗口保持打开状态
    root.mainloop()



