from PIL import Image, ImageDraw, ImageFont
import os

def create_icon():
    # 创建一个512x512的图标
    img = Image.new('RGBA', (512, 512), color='white')
    draw = ImageDraw.Draw(img)
    
    # 绘制一个蓝色圆形背景
    draw.ellipse([50, 50, 462, 462], fill='#2196F3')
    
    # 添加文字
    try:
        font = ImageFont.truetype('fonts/simsun.ttf', 120)
    except:
        font = ImageFont.load_default()
    
    text = "量化"
    # 获取文本大小
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    
    # 计算文本位置使其居中
    x = (512 - text_width) // 2
    y = (512 - text_height) // 2
    
    # 绘制文字
    draw.text((x, y), text, font=font, fill='white')
    
    # 保存图标
    os.makedirs('data', exist_ok=True)
    img.save('data/icon.png')

def create_presplash():
    # 创建一个1024x1024的启动画面
    img = Image.new('RGBA', (1024, 1024), color='#2196F3')
    draw = ImageDraw.Draw(img)
    
    # 添加文字
    try:
        font = ImageFont.truetype('fonts/simsun.ttf', 160)
    except:
        font = ImageFont.load_default()
    
    text = "量化交易"
    # 获取文本大小
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    
    # 计算文本位置使其居中
    x = (1024 - text_width) // 2
    y = (1024 - text_height) // 2
    
    # 绘制文字
    draw.text((x, y), text, font=font, fill='white')
    
    # 保存启动画面
    os.makedirs('data', exist_ok=True)
    img.save('data/presplash.png')

if __name__ == '__main__':
    create_icon()
    create_presplash()
    print("图标和启动画面已生成在 data 目录中") 