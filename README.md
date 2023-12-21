<h1 align="center">
  AI-group-files
</h1>
<p align="center" width="100%">
  <img src="https://libinpg.github.io/logo.png" alt="Llama" style="width: 20%; display: block; margin: auto;"></a>
</p>

# 自动文件整理系统

这个项目利用 OpenAI API 及其它大模型API自动地对文件进行分类和整理。基于文件内容，它将文件移动到相应的分类文件夹中，使文件管理更加高效和有序。

## 功能

- **文件解析**：读取指定文件的内容。
- **内容分类**：使用 OpenAI API 分析文件内容，并返回分类标签。
- **自动整理**：根据分类标签，将文件移动到对应的分类文件夹。

## 安装

1. 克隆此仓库到您的本地机器：
   ```bash
   git clone https://github.com/libinpg/AI-group-files.git

2. 进入项目目录：
   ```bash
   cd AI-group-files
   ```
3. 安装所需依赖（确保您已安装 Python 和 pip）：
   ```bash
   pip install -r requirements.txt
   ```

## 配置

1. 在 `config.json` 文件中填入您的 OpenAI API 密钥或百度千帆平台API密钥，至少填写一个模型：
   ```json
   {
     "openai": {
          "openai_api_key": "your_openai_api_key"
     },
     "baidu_qianfan": {
         "api_key": "your_api_key",
         "api_secret": "your_api_secret"
     }
   }
   ```
2. 确保不要公开您的 API 密钥，尤其是在公共代码库中。

## 使用

1. 调用openai gpt-3.5模型进行文件整理并指定待整理的目录和整理后的路径(可选)：
   ```bash
   python src/main.py your_file_directory_path --classifier openai --save_path xxx
   ```
2. 调用Llama-2-7b-chat模型进行文件整理并指定要整理的目录和整理后的路径(可选)：
   ```bash
   python src/main.py your_file_directory_path --classifier llama --save_path xxx
   ```
3. 调用ChatGLM2_6B_32K模型进行文件整理并指定要整理的目录和整理后的路径(可选)：
   ```bash
   python src/main.py your_file_directory_path --classifier glm --save_path xxx
   ```
4. 查看输出以确认文件分类和整理结果。

## Model Benchmark

1. gpt3.5
2. llama
3. chatglm_6B_32k

## ToDo

1. 用国内大模型接口降低成本(已适配百度千帆ChatGLM2_6B_32K api,Llama-2-7b-chat api)。
2. 添加中英文文件名选项
3. 添加分类结果整合逻辑
4. 更新openai api调用函数
5. 取消跟踪.gitignore文件
6. 添加不同模型的benchmark
7. 添加本地模型支持
8. 编译为可执行程序
9. 系统可以用学习用户的分类习惯


## 贡献

如果您想为此项目贡献代码或提出改进建议，请联系我的邮箱获取测试openai apikey, 请遵循以下步骤：

1. Fork 仓库。
2. 创建新的分支 (`git checkout -b feature-branch`).
3. 提交您的更改 (`git commit -m 'Add some feature'`).
4. 推送到分支 (`git push origin feature-branch`).
5. 创建新的 Pull Request。

## 许可证

[MIT](https://choosealicense.com/licenses/mit/)

## 联系方式

如有问题或需要帮助，请通过以下方式联系我：[Email](mailto:1790572759@qq.com)
