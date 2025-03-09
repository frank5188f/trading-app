import kivy
kivy.require('2.0.0')

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.metrics import dp

# 设置适合移动设备的字体大小
FONT_SIZE = dp(14)
BUTTON_HEIGHT = dp(40)
INPUT_HEIGHT = dp(35)

class TradingAppGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(TradingAppGridLayout, self).__init__(**kwargs)
        self.cols = 1
        self.padding = [dp(10)]
        self.spacing = dp(10)

        # 创建一个用于输入的GridLayout
        input_grid = GridLayout(cols=2, spacing=dp(10), size_hint_y=None)
        input_grid.bind(minimum_height=input_grid.setter('height'))

        # 添加输入部件
        labels = [
            '基金代码 (6位):',
            '开始日期 (YYYYMMDD):',
            '结束日期 (YYYYMMDD):',
        ]
        
        self.inputs = {}
        for label_text in labels:
            label = Label(
                text=label_text,
                font_size=FONT_SIZE,
                size_hint_y=None,
                height=INPUT_HEIGHT,
                halign='right'
            )
            input_field = TextInput(
                multiline=False,
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
            text='运行交易策略',
            font_size=FONT_SIZE,
            size_hint_y=None,
            height=BUTTON_HEIGHT
        )
        self.run_button.bind(on_press=self.run_trading_strategy)
        self.add_widget(self.run_button)

        # 添加状态标签
        self.status_label = Label(
            text='等待运行...',
            font_size=FONT_SIZE,
            size_hint_y=None,
            height=dp(30)
        )
        self.add_widget(self.status_label)

    def run_trading_strategy(self, instance):
        # 获取输入值
        etf_fund_code = self.inputs['基金代码 (6位):'].text
        start_date = self.inputs['开始日期 (YYYYMMDD):'].text
        end_date = self.inputs['结束日期 (YYYYMMDD):'].text

        if not all([etf_fund_code, start_date, end_date]):
            self.status_label.text = '请填写所有必要字段'
            return
            
        self.status_label.text = f'已收到代码: {etf_fund_code}, 从 {start_date} 到 {end_date}'

class TradingApp(App):
    def build(self):
        # 设置窗口大小
        Window.size = (dp(360), dp(640))
        return TradingAppGridLayout()

if __name__ == '__main__':
    TradingApp().run() 