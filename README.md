# AI Agent 学习

从零理解 **AI Agent**：它是什么、怎么工作、如何按**角色**组装进**项目**。

## 核心节奏（先读这个）

> **按角色拆 Agent，按项目组装角色。**  
> 角色可跨项目复用；项目只提供目标与材料。

```
定角色 → 选项目 → 组装 Cast → 上场
```

详见：[角色 vs 项目](./01-concepts/07-role-vs-project.md)

## 你将学到什么

- Agent 与 Chatbot 的区别  
- 工具、记忆、规划、多 Agent  
- **角色优先**的拆分方式（而不是一项目一只要命 Agent）  
- 可运行 Python 示例 + 用角色拼项目的练习  

## 学习路线

```
概念 → 框架 → 示例 → 角色库 → 项目剧本
 01      02     03      04        05
```

| 阶段 | 目录 | 建议 |
|------|------|------|
| 1. 概念 | [01-concepts](./01-concepts/) | 建心智模型；重点读 07 |
| 2. 框架 | [02-frameworks](./02-frameworks/) | 选型参考 |
| 3. 示例 | [03-examples](./03-examples/) | 跑通工具与循环 |
| 4. 角色 | [04-roles](./04-roles/) | 沉淀可复用角色卡 |
| 5. 项目 | [05-projects](./05-projects/) | 用角色拼项目，勿再按项目重写 Agent |

## 快速开始（示例）

```bash
cd 03-examples
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt

export OPENAI_API_KEY="sk-..."
python 01-simple-chat/main.py
python 02-tool-calling/main.py
python 03-react-agent/main.py
```

## 一句话定义

> **AI Agent = LLM + 工具 + 循环决策**  
> 工程上再加一层：**Role（稳定）× Project（易变）**

## 目录

```
AiAgentStudy/
├── 01-concepts/     # 概念（含「角色优先」）
├── 02-frameworks/   # 框架对比
├── 03-examples/     # 可运行代码
├── 04-roles/        # 可复用角色卡
└── 05-projects/     # 项目剧本（组装角色）
```

## 适合谁

- 会一点 Python，想搞懂 Agent  
- 以前按项目拆 Agent，想改成可复用角色  
- 在 Cursor 里用 Agent 做多仓库协作  

祝学习顺利。
