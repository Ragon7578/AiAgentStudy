# LangChain / LangGraph

## 一句话

- **LangChain**：组件库（模型、提示、检索、工具封装）  
- **LangGraph**：用**图（状态机）**编排 Agent / 工作流，可控性更强  

近年做复杂 Agent，社区更常推荐 **LangGraph** 做编排，LangChain 提供底层积木。

## 核心概念映射

| 本仓库概念 | LangGraph 里大致对应 |
|------------|----------------------|
| Agent 状态 | `State`（TypedDict / Pydantic） |
| 一步行动 | `Node`（函数） |
| 下一步去哪 | `Edge` / 条件边 |
| 工具调用 | Tool node + 绑定工具的 LLM |
| 循环 | 图上的回边，直到结束节点 |

## 最小心智模型

```
START → agent（调用 LLM） → 要不要用工具？
              ↑               │
              └── tools ◄─────┘ 是
                              │ 否
                              ▼
                            END
```

这就是经典的「Tool-calling Agent」图。

## 适合什么

- 需要**明确状态**与可恢复执行（checkpoint）  
- 要人工审批节点（human-in-the-loop）  
- 多步业务流：分流、汇合、重试  
- 团队要可视化与调试轨迹  

## 不太适合什么

- 只想 50 行代码验证想法（可能过重）  
- 完全绑定某一家专有 Agent 产品能力  

## 上手路径

1. 官方 LangGraph Quickstart  
2. 实现：聊天模型 + 1～2 个工具的循环图  
3. 加 checkpoint 与中断（审批）  
4. 再考虑多 Agent（supervisor 模式）  

## 和本仓库示例的关系

先跑：

- [02-tool-calling](../03-examples/02-tool-calling/)  
- [03-react-agent](../03-examples/03-react-agent/)  

再用 LangGraph 重写第三例：你会清晰看到「手写 while 循环」如何变成「图上的边」。
