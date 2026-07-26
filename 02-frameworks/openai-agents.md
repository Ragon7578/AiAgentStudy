# OpenAI Agents SDK

## 一句话

OpenAI 提供的 **Agent 编排 SDK**：用少量代码定义 Agent、工具、交接（handoff），跑带工具的循环。

> 名称与版本会演进；学习时抓住概念即可，以官方文档为准。

## 核心概念

| 概念 | 含义 |
|------|------|
| Agent | 带指令、模型、工具的角色 |
| Tool | Python 函数或托管工具 |
| Handoff | 把对话交给另一个 Agent |
| Runner / Session | 执行循环、管理会话 |
| Guardrails | 输入输出安全校验（若提供） |

## 典型代码形状（示意）

```python
from agents import Agent, Runner, function_tool

@function_tool
def get_weather(city: str) -> str:
    """查询城市天气。"""
    return f"{city}: 晴，26°C"

assistant = Agent(
    name="助手",
    instructions="你是简洁的中文助手，需要天气时调用工具。",
    tools=[get_weather],
)

result = Runner.run_sync(assistant, "北京今天天气怎么样？")
print(result.final_output)
```

（具体 import 路径以当前官方包为准。）

## 适合什么

- 已经在 OpenAI 生态（Responses API / 兼容层）  
- 想快速上线单 Agent 或多 Agent handoff  
- 希望少写样板循环代码  

## 注意

- 与「裸 SDK + while 循环」相比，调试抽象层更多  
- 换模型供应商时，确认工具调用协议是否兼容  
- 生产环境仍要自己做：权限、超时、日志、费用控制  

## 学习建议

对照本仓库 [02-tool-calling](../03-examples/02-tool-calling/)：  
先理解手写 `tools` + `tool_calls`，再看 SDK 帮你省了哪几步。
