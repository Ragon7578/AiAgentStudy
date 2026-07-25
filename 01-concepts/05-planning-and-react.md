# 05 · 规划与 ReAct

## 为什么需要规划

复杂目标很难一步完成，例如：

> 「分析这个仓库的测试覆盖，找出最薄弱模块，并提一个改进 PR。」

Agent 需要拆解步骤、选择工具、根据中间结果调整——这就是**规划**。

## ReAct：Reason + Act

经典模式（Yao et al., 2022）：

```
Thought: 我需要先知道仓库结构
Action: list_files(path=".")
Observation: src/, tests/, README.md ...

Thought: 接下来看测试目录
Action: list_files(path="tests")
Observation: ...

Thought: 已经够了，可以总结
Final Answer: ...
```

特点：

- 思考过程可读（便于调试）  
- 行动与观察交替  
- 适合搜索、排查、调研类任务  

本仓库示例：[03-react-agent](../03-examples/03-react-agent/)

## 其他常见规划方式

| 模式 | 思路 | 适合 |
|------|------|------|
| ReAct | 边想边做 | 探索型任务 |
| Plan-and-Execute | 先写完整计划再执行 | 步骤较清晰的流程 |
| Reflexion | 失败后反思再试 | 需要自我纠错 |
| 状态机 / Graph | 预定义节点与边 | 强可控、要审计 |
| Tree-of-Thoughts | 多路径搜索 | 难题、需对比方案 |

工业界很多「Agent 产品」本质是：**LLM + 工具 + 某种规划循环**，外加权限与日志。

## Plan-and-Execute 简图

```
1. Planner: 产出步骤列表 [S1, S2, S3]
2. Executor: 逐步执行，可调用工具
3. 若某步失败 → 重新规划或局部重试
4. 全部完成 → 汇总给用户
```

优点：计划可见、易插入人工审批。  
缺点：环境变化快时，一开始的计划可能过时（需要重规划）。

## 停止条件（别让 Agent 空转）

必须定义何时停下：

- 模型输出 `Final Answer` / 显式完成信号  
- 达到最大步数（如 10 步）  
- 连续工具失败 N 次  
- 需要用户确认才能继续  
- 超时  

没有停止条件 = 烧钱 + 死循环。

## 调试技巧

1. **打印每一步** Thought / Action / Observation  
2. 看模型是否在「无效循环」（反复同一工具同一参数）  
3. 检查工具描述是否误导  
4. 缩小目标，先让短链路跑通再加复杂度  

## 下一步

继续阅读：[06 · 多 Agent](./06-multi-agent.md) → 然后是 [07 · 角色优先](./07-role-vs-project.md)
