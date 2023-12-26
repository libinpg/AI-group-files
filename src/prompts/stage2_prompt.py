# prompts.py {}对应的参数依次为directoryconclusion和content
CLASSIFY_FILE_PROMPT = (
    "这是一个元素: '{}' ,接下来执行一个循环判断以下结构体： ```'{}'```中元素和其中一个相像则返回(尽可能基于你庞大的知识储备猜测)，你只需要返回一个答案?. 请遵循格式{{the choice from ai model}}返回 "
    "着意味着你的回答中的应该包含一个大括号返回的答案，大括号内只能包含一个选项, 格式非常重要，不然回答无效"
)