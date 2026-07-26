# 01 · 简单对话（还不是 Agent）

这一步只调用 LLM 聊天，**没有工具、没有循环**。

目的：确认 API Key / Base URL / 模型可用，作为后续示例的基线。

```bash
cd 03-examples
python 01-simple-chat/main.py
```

对比下一例你会发现：Agent = 在对话之上加「工具 + 循环」。
