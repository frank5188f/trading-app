import kivy

# 导入 Kivy 库，Kivy 是一个开源的 Python 框架，用于快速开发应用，可以创建用户友好的用户界面，例如多点触控应用。
kivy.require('2.3.1')  # 请根据您的 Kivy 版本修改
#  指定 Kivy 的版本要求，确保程序运行在指定的 Kivy 版本或更高版本上。请用户根据自己的 Kivy 版本修改版本号。

from kivy.app import App
# 从 kivy.app 模块导入 App 类。App 类是所有 Kivy 应用的基础类，用于管理应用的生命周期、配置和用户界面。
from kivy.uix.gridlayout import GridLayout
# 从 kivy.uix.gridlayout 模块导入 GridLayout 类。GridLayout 是一种布局管理器，用于在网格中排列子部件（widgets）。
from kivy.uix.label import Label
# 从 kivy.uix.label 模块导入 Label 类。Label 类用于显示文本标签。
from kivy.uix.textinput import TextInput
# 从 kivy.uix.textinput 模块导入 TextInput 类。TextInput 类用于接收用户输入的单行或多行文本。
from kivy.uix.button import Button
# 从 kivy.uix.button 模块导入 Button 类。Button 类用于创建按钮，响应用户的点击事件。
# from kivy.uix.image import Image  # Image 组件如果需要再启用
# 从 kivy.uix.image 模块导入 Image 类。(这行代码被注释掉了) Image 类用于显示图片。如果需要显示图片，可以取消注释。
from kivy.clock import Clock
# 从 kivy.clock 模块导入 Clock 类。Clock 类用于调度函数在未来的某个时间或以一定的时间间隔运行，常用于异步操作和事件调度。
from kivy.logger import Logger
# 从 kivy.logger 模块导入 Logger 类。Logger 类用于记录日志信息，帮助开发者调试和监控应用运行状态。
from kivy.core.window import Window
from kivy.metrics import dp
import pandas as pd
# 导入 pandas 库，并将其别名为 pd。Pandas 是一个强大的数据分析库，提供了 DataFrame 等数据结构，用于高效地处理和分析结构化数据。
import numpy as np
# 导入 numpy 库，并将其别名为 np。Numpy 是一个科学计算库，提供了高性能的数组对象和数学函数，用于数值计算。
import akshare as ak
# 导入 akshare 库，并将其别名为 ak。Akshare 是一个开源的金融数据接口库，用于获取股票、基金等金融市场的数据。
import matplotlib

# 导入 matplotlib 库。Matplotlib 是一个绘图库，用于创建各种静态、动态、交互式的可视化图表。
matplotlib.use('Agg')
# 设置 Matplotlib 的 backend 为 'Agg'。'Agg' backend 是一个非交互式的 backend，用于在没有图形界面环境下生成图像文件，例如在服务器端或批量处理脚本中。
import matplotlib.pyplot as plt
# 从 matplotlib 库导入 pyplot 模块，并将其别名为 plt。pyplot 模块提供了一系列绘图函数，用于创建图表。
import io
import os

# 导入 io 模块。io 模块提供了处理各种 I/O 类型的主要工具，例如内存中的文本或二进制数据流。


#  !!!  添加以下代码，设置 Matplotlib 使用中文字体 (这部分代码已经存在，无需修改) !!!
#  !!!  添加以下代码，设置 Matplotlib 使用中文字体 (这部分代码是注释，提示用户以下代码用于设置 Matplotlib 使用中文字体，并且说明这部分代码已经存在，无需修改) !!!
plt.rcParams['font.sans-serif'] = ['SimSun']
# 设置 Matplotlib 的字体为 SimSun（宋体）。rcParams 是 matplotlib 的配置字典，'font.sans-serif' 键用于设置 sans-serif 字体族，这里设置为宋体，以显示中文。
plt.rcParams['axes.unicode_minus'] = False


# 设置 Matplotlib 正常显示负号。默认情况下，Matplotlib 可能会将负号显示为方块，设置 'axes.unicode_minus' 为 False 可以解决这个问题，确保正确显示负号。
#  !!!  字体设置代码添加完毕  !!!
#  !!!  字体设置代码添加完毕 (这部分是注释，提示用户字体设置代码添加完成) !!!


# 设置适合移动设备的字体大小
FONT_SIZE = dp(14)
BUTTON_HEIGHT = dp(40)
INPUT_HEIGHT = dp(35)

class TradingAppGridLayout(GridLayout):
    # 定义一个名为 TradingAppGridLayout 的类，继承自 GridLayout 类。这个类将作为交易应用的主布局。
    def __init__(self, **kwargs):
        # 定义构造函数 __init__，当创建 TradingAppGridLayout 类的实例时，会自动调用这个函数。**kwargs 允许接收任意数量的关键字参数。
        super(TradingAppGridLayout, self).__init__(**kwargs)
        # 调用父类 GridLayout 的构造函数，确保父类的初始化逻辑被执行。super() 用于调用父类的方法。
        self.cols = 1  # 改为单列布局
        self.padding = [dp(10)]  # 添加内边距
        self.spacing = dp(10)  # 添加部件间距

        # 创建一个用于输入的GridLayout
        input_grid = GridLayout(cols=2, spacing=dp(10), size_hint_y=None)
        input_grid.bind(minimum_height=input_grid.setter('height'))

        # 设置字体路径
        font_path = os.path.join('fonts', 'simsun.ttf')
        if not os.path.exists(font_path):
            font_path = 'simsun.ttf'  # 回退到默认路径

        # 添加输入部件
        labels = [
            '基金代码 (6位):',
            '开始日期 (YYYYMMDD):',
            '结束日期 (YYYYMMDD):',
            'EMA 短期窗口期:',
            'WMA 中期窗口期:',
            'SMA 长期窗口期:'
        ]
        
        self.inputs = {}
        for label_text in labels:
            label = Label(
                text=label_text,
                font_name=font_path,
                font_size=FONT_SIZE,
                size_hint_y=None,
                height=INPUT_HEIGHT,
                halign='right'
            )
            input_field = TextInput(
                multiline=False,
                font_name=font_path,
                font_size=FONT_SIZE,
                size_hint_y=None,
                height=INPUT_HEIGHT
            )
            input_grid.add_widget(label)
            input_grid.add_widget(input_field)
            self.inputs[label_text] = input_field

        self.add_widget(input_grid)

        # 添加运行按钮
        self.run_button = Button(
            text='运行量化交易策略',
            font_name=font_path,
            font_size=FONT_SIZE,
            size_hint_y=None,
            height=BUTTON_HEIGHT
        )
        self.run_button.bind(on_press=self.run_trading_strategy)
        self.add_widget(self.run_button)

        # 添加状态和结果标签
        self.status_label = Label(
            text='等待运行...',
            font_name=font_path,
            font_size=FONT_SIZE,
            size_hint_y=None,
            height=dp(30)
        )
        self.add_widget(self.status_label)

        self.result_label = Label(
            text='',
            font_name=font_path,
            font_size=FONT_SIZE,
            size_hint_y=None,
            height=dp(90),
            text_size=(Window.width - dp(20), None)
        )
        self.add_widget(self.result_label)

    def run_trading_strategy(self, instance):
        # 获取输入值
        try:
            etf_fund_code = self.inputs['基金代码 (6位):'].text
            start_date = self.inputs['开始日期 (YYYYMMDD):'].text
            end_date = self.inputs['结束日期 (YYYYMMDD):'].text
            v_short_window = int(self.inputs['EMA 短期窗口期:'].text)
            long_window = int(self.inputs['WMA 中期窗口期:'].text)
            short_window = int(self.inputs['SMA 长期窗口期:'].text)

            if not all([etf_fund_code, start_date, end_date]):
                self.status_label.text = '请填写所有必要字段'
                return

            self.status_label.text = '数据获取和计算中...'
            Clock.schedule_once(
                lambda dt: self.execute_strategy(
                    etf_fund_code, start_date, end_date,
                    v_short_window, long_window, short_window
                ), 0
            )
        except ValueError:
            self.status_label.text = '请确保窗口期为有效的数字'

    def execute_strategy(self, etf_fund_code, start_date, end_date, v_short_window, long_window, short_window):
        try:
            # 获取数据
            etf_data_raw = ak.fund_etf_fund_info_em(
                fund=etf_fund_code,
                start_date=start_date,
                end_date=end_date,
            )
            
            # 数据处理
            data = etf_data_raw.copy()
            data.rename(columns={'净值日期': 'Date', '累计净值': 'Close'}, inplace=True)
            data['Date'] = pd.to_datetime(data['Date'])
            data.set_index('Date', inplace=True)
            data.sort_index(inplace=True)

            # 计算指标
            data['V_Short_EMA'] = data['Close'].ewm(span=v_short_window, adjust=False).mean()
            data['Short_SMA'] = data['Close'].rolling(window=short_window).mean()
            data['Long_WMA'] = data['Close'].rolling(window=long_window).apply(
                lambda x: np.average(x, weights=np.arange(1, long_window + 1)))

            # 生成信号
            data['Signal'] = 0.0
            data.iloc[long_window:, data.columns.get_loc('Signal')] = np.where(
                (data['V_Short_EMA'].iloc[long_window:] > data['Short_SMA'].iloc[long_window:]) &
                (data['Short_SMA'].iloc[long_window:] > data['Long_WMA'].iloc[long_window:]),
                1.0, 0.0
            )
            data['Position'] = data['Signal'].diff()

            # 回测计算
            initial_capital = 10000
            positions = 0
            cash = initial_capital
            equity_history = [initial_capital]

            for i in range(long_window, len(data)):
                if data['Position'].iloc[i] == 1.0 and cash > 0:
                    positions = cash / data['Close'].iloc[i]
                    cash = 0
                elif data['Position'].iloc[i] == -1.0 and positions > 0:
                    cash = positions * data['Close'].iloc[i]
                    positions = 0
                current_equity = cash + positions * data['Close'].iloc[i]
                equity_history.append(current_equity)

            final_equity = equity_history[-1]
            roi = (final_equity - initial_capital) / initial_capital * 100

            # 更新结果显示
            result_text = (
                f'初始资金: ¥{initial_capital:,.2f}\n'
                f'最终资金: ¥{final_equity:,.2f}\n'
                f'总回报率: {roi:.2f}%'
            )
            self.result_label.text = result_text
            self.status_label.text = '策略执行完成'

            # 保存图表
            self.save_strategy_plot(data, v_short_window, long_window, short_window, etf_fund_code)

        except Exception as e:
            error_message = f"运行出错: {str(e)}"
            self.status_label.text = error_message
            Logger.error(error_message)

    def save_strategy_plot(self, data, v_short_window, long_window, short_window, etf_fund_code):
        try:
            plt.figure(figsize=(12, 8))
            plt.plot(data['Close'], label='累计净值')
            plt.plot(data['V_Short_EMA'], label=f'{v_short_window}日EMA')
            plt.plot(data['Long_WMA'], label=f'{long_window}日WMA')
            plt.plot(data['Short_SMA'], label=f'{short_window}日SMA')
            
            # 添加买卖点标记
            plt.plot(
                data.loc[data['Position'] == 1].index,
                data['V_Short_EMA'][data['Position'] == 1],
                '^', markersize=10, color='g', label='买入信号'
            )
            plt.plot(
                data.loc[data['Position'] == -1].index,
                data['V_Short_EMA'][data['Position'] == -1],
                'v', markersize=10, color='r', label='卖出信号'
            )
            
            plt.title(f'三均线交易策略 - {etf_fund_code}')
            plt.xlabel('日期')
            plt.ylabel('净值')
            plt.legend()
            plt.grid(True)
            
            # 保存图表
            plot_path = os.path.join(os.path.dirname(__file__), f'strategy_plot_{etf_fund_code}.png')
            plt.savefig(plot_path, dpi=300, bbox_inches='tight')
            plt.close()
            
            self.status_label.text = f'策略执行完成，图表已保存'
        except Exception as e:
            Logger.error(f'保存图表时出错: {str(e)}')

class TradingApp(App):
    # 定义一个名为 TradingApp 的类，继承自 App 类。这个类是 Kivy 应用的主类。
    def build(self):
        # 设置窗口大小
        Window.size = (dp(360), dp(640))  # 模拟常见手机屏幕尺寸
        return TradingAppGridLayout()
        # 返回 TradingAppGridLayout 类的实例，作为应用的根部件。这意味着应用的界面将由 TradingAppGridLayout 定义的布局和部件构成。


if __name__ == '__main__':
    # 判断是否在主程序入口处运行。当直接运行此脚本时，__name__ 的值为 '__main__'。
    TradingApp().run()
    # 创建 TradingApp 类的实例，并调用 run() 方法启动 Kivy 应用。run() 方法会进入 Kivy 的事件循环，开始处理用户输入和界面更新。
