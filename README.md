# 自动文件整理系统

这个项目利用 OpenAI API 自动地对文件进行分类和整理。基于文件内容，它将文件移动到相应的分类文件夹中，使文件管理更加高效和有序。

## 功能

- **文件解析**：读取指定文件的内容。
- **内容分类**：使用 OpenAI API 分析文件内容，并返回分类标签。
- **自动整理**：根据分类标签，将文件移动到对应的分类文件夹。

## 安装

1. 克隆此仓库到您的本地机器：
   ```bash
   git clone https://github.com/your-username/AI-group-files.git

2. 进入项目目录：
   ```bash
   cd AI-group-files
   ```
3. 安装所需依赖（确保您已安装 Python 和 pip）：
   ```bash
   pip install -r requirements.txt
   ```

## 配置

1. 在 `config.json` 文件中填入您的 OpenAI API 密钥：
   ```json
   {
     "openai_api_key": "YOUR_API_KEY"
   }
   ```
2. 确保不要公开您的 API 密钥，尤其是在公共代码库中。

## 使用

1. 运行主脚本并指定要整理的目录：
   ```bash
   python src/main.py your_file_directory_path
   ```
2. 查看输出以确认文件分类和整理结果。

## 贡献

如果您想为此项目贡献代码或提出改进建议，请遵循以下步骤：

1. Fork 仓库。
2. 创建新的分支 (`git checkout -b feature-branch`).
3. 提交您的更改 (`git commit -m 'Add some feature'`).
4. 推送到分支 (`git push origin feature-branch`).
5. 创建新的 Pull Request。

## 许可证

[MIT](https://choosealicense.com/licenses/mit/)

## 联系方式

如有问题或需要帮助，请通过以下方式联系我：[Email](mailto:1790572759@qq.com)
