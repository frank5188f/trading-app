# 量化交易应用 - 简化版

这是一个使用 Kivy 框架开发的量化交易 Android 应用简化版。

## 简化说明

为了确保构建成功，我们简化了应用功能：

1. 移除了复杂的依赖（pandas, numpy, akshare等）
2. 简化了用户界面
3. 简化了构建配置

## 构建命令

使用以下命令构建APK：

```bash
buildozer android debug
```

## 后续开发

成功构建后，我们将逐步添加更多功能，恢复完整的应用程序功能。

## 功能特点

- 支持基金数据查询和分析
- 使用三均线交叉策略进行交易信号生成
- 提供回测功能
- 可视化交易结果

## 技术栈

- Python 3.9
- Kivy 2.3.1
- Pandas
- NumPy
- Akshare
- Matplotlib

## 安装方法

### 从源码构建

1. 克隆仓库：
```bash
git clone https://github.com/frank5188f/trading-app.git
cd trading-app
```

2. 安装依赖：
```bash
pip install -r requirements.txt
```

3. 运行应用：
```bash
python main.py
```

### 直接安装 APK

1. 从 [Releases](https://github.com/frank5188f/trading-app/releases) 页面下载最新的 APK
2. 在 Android 设备上安装下载的 APK 文件

## 使用说明

1. 输入基金代码（6位数字）
2. 设置开始日期和结束日期（格式：YYYYMMDD）
3. 设置三个均线周期：
   - EMA短期窗口期（建议：10）
   - WMA中期窗口期（建议：30）
   - SMA长期窗口期（建议：60）
4. 点击"运行量化交易策略"按钮
5. 查看回测结果和交易信号图表

## 开发说明

### 环境要求

- Python 3.9 或更高版本
- Android SDK
- Buildozer（用于构建 Android APK）

### 构建 Android APK

```bash
buildozer android debug
```

生成的 APK 文件将位于 `bin` 目录中。

## 许可证

MIT License

## 贡献指南

1. Fork 本仓库
2. 创建您的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交您的更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 打开一个 Pull Request 