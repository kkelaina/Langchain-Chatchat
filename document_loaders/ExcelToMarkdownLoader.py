from pathlib import Path
from pprint import pprint
from typing import List

from langchain.document_loaders.text import TextLoader
from langchain_core.documents import Document


class ExcelToMarkdownLoader(TextLoader):
    def load(self) -> List[Document]:
        def get_first_line(text):
            lines = text.splitlines()
            if lines:
                return lines[0]
            else:
                return ""

        def excel2text(filepath):
            import pandas as pd
            excel_file = pd.ExcelFile(filepath)

            # 遍历每个 sheet
            markdown_content = ""
            markdown_content += f"# {Path(filepath).name}\n\n"
            for sheet_name in excel_file.sheet_names:
                df = excel_file.parse(sheet_name, header=None)

                # 遍历每一行
                for index, row in df.iterrows():
                    # 获取第一列的文本
                    first_column_text = str(row[0])
                    # 提取第一句话
                    first_sentence = get_first_line(first_column_text)
                    # 构建 Markdown 格式
                    markdown_content += f"\n\n## {first_sentence}  "
                    markdown_content += f"\n{first_column_text}  "

            return markdown_content

        text = excel2text(self.file_path)
        metadata = {"source": self.file_path}
        return [Document(page_content=text, metadata=metadata)]


if __name__ == "__main__":
    loader = ExcelToMarkdownLoader(file_path=r"C:\Users\Dell\Desktop\ok卡帮助中心.xlsx")
    docs = loader.load()
    pprint(docs)
