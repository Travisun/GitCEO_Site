import xml.etree.ElementTree as ET

# 读取sitemap.xml文件
tree = ET.parse('public/sitemap.xml')
root = tree.getroot()

# 打开urls.txt文件以写入模式
with open('public/baidu_urls.txt', 'w') as f:
    # 查找所有的 <loc> 元素并写入到urls.txt文件中
    for url in root.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}loc'):
        f.write(url.text + '\n')

print("URLs 已提取并保存到 public/baidu_urls.txt 文件中。")
