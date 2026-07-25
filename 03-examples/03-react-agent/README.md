# 03 · 迷你 ReAct Agent

在工具调用之上加 **while 循环**：模型可多步调用工具，直到给出最终答案或达到步数上限。

这就是最小可用的 Agent。

```bash
cd 03-examples
python 03-react-agent/main.py
# 或自定义问题：
python 03-react-agent/main.py "北京和上海温差多少？哪个更适合户外运动？"
```

观察终端里每一步的 `Thought-ish`（模型中间内容）与 `Action` / `Observation`。

扩展练习见 [04-projects](../../04-projects/)。
