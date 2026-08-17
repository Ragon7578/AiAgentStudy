# 02 · 工具调用（一次闭环）

模型不再只「说话」，而是可以请求执行本地函数；框架执行后把结果再喂回模型，得到最终回答。

这是 Agent 的最小能力单元：**Function Calling**。

```bash
cd 03-examples
python 02-tool-calling/main.py
```

建议改一改：

- 换城市 / 换问题  
- 再注册一个 `get_time` 工具  
- 故意让工具返回错误，看模型如何解释  
