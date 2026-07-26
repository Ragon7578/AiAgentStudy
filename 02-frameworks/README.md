# 框架选型总览

学 Agent 不必先精通某个框架。先理解 [01-concepts](../01-concepts/)，再用最小代码验证，最后按场景选型。

## 怎么选（速查）

| 你的目标 | 更合适的方向 |
|----------|----------------|
| 理解原理、少依赖 | 本仓库 `03-examples`（裸 OpenAI SDK） |
| 生产级工作流、可审计 | [LangGraph](./langchain-langgraph.md) |
| 快速做 OpenAI 生态 Agent | [OpenAI Agents SDK](./openai-agents.md) |
| 改代码、提 PR、仓库内自动化 | [Cursor Agent](./cursor-agent.md) |
| 多角色仿真 / 群聊实验 | AutoGen / CrewAI（了解即可） |

## 学习建议

1. **先跑通本仓库三个示例**——建立「循环 + 工具」肌肉记忆  
2. 再读一篇框架文档，把概念映射过去（State、Node、Tool、Handoff…）  
3. 用框架重写示例 03（ReAct），对比自己手写版本  

## 本目录

- [LangChain / LangGraph](./langchain-langgraph.md)  
- [OpenAI Agents SDK](./openai-agents.md)  
- [Cursor Agent（产品向）](./cursor-agent.md)  

## 记住

框架是脚手架，核心仍是：

> **模型决策 → 工具执行 → 结果回灌 → 停止条件**

换框架时，优先问：状态存在哪？工具怎么注册？循环谁驱动？错误怎么暴露？
