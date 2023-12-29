from pprint import pprint
import pandas as pd


def test():
    df = pd.read_excel(r'C:\Users\Dell\Desktop\ok卡帮助中心.xlsx')  # 打开文件
    # 获取第一列数据
    first_column_data = df.iloc[:, 0]
    print("\n")
    # 将内容转换为 Markdown 格式
    markdown_text = ""
    for item in first_column_data:
        markdown_text += f"## {item}\n\n"

    # 打印生成的 Markdown 文本
    print(markdown_text)
    # 将 Markdown 文本保存到 .md 文件
    md_file_path = r'C:\Users\Dell\Desktop\ok卡帮助中心.md'
    with open(md_file_path, 'w', encoding='utf-8') as file:
        file.write(markdown_text)
        # 打印生成的 Markdown 文本路径
    print(f"Markdown 文本已保存至 {md_file_path}")


if __name__ == "__main__":
    print("test")
    test()
