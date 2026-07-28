# AI Agent 学习

> **本仓库是帮助你学习 AI Agent 的工具仓，不是某个业务产品项目。**  
> 没有「兑一兑 / SmartCity」之类的真实产品要交付；`05-projects/` 里的「项目」是**练习剧本**，用来练「用角色拼场景」。

从零理解 **AI Agent**：它是什么、怎么工作、如何按**角色**组装进**练习场景**。

## 核心节奏（先读这个）

> **按角色拆 Agent，按项目组装角色。**  
> 角色可跨场景复用；「项目」只提供目标与材料（学习里 = 练习剧本）。

```
定角色 → 选练习剧本 → 组装 Cast → 上场
```

详见：[角色 vs 项目](./01-concepts/07-role-vs-project.md)

## 学习目标

> 不只是「看懂 Agent」，而是：**半年后能独立完成 AI Agent 开发，并用作品找到工作。**

详细规划：[06-career · 半年路线](./06-career/README.md)

## 你将学到什么

- Agent 与 Chatbot 的区别  
- 工具、记忆、规划、多 Agent  
- **角色优先**的拆分方式（而不是一场景一只要命 Agent）  
- 可运行 Python 示例 + 用角色拼练习剧本  

## 学习路线

```
概念 → 框架 → 示例 → 角色库 → 练习剧本 → 半年求职路线
 01      02     03      04        05           06
```

| 阶段 | 目录 | 建议 |
|------|------|------|
| 1. 概念 | [01-concepts](./01-concepts/) | 建心智模型；重点读 07 |
| 2. 框架 | [02-frameworks](./02-frameworks/) | 选型参考 |
| 3. 示例 | [03-examples](./03-examples/) | 跑通工具与循环 |
| 4. 角色 | [04-roles](./04-roles/) | 沉淀可复用角色卡 |
| 5. 练习 | [05-projects](./05-projects/) | 用角色拼剧本，勿再按场景重写 Agent |
| 6. 求职 | [06-career](./06-career/) | 半年：作品 → 工程化 → 面试包装 |

## 建议从哪开始

1. 读 [01-concepts/01-what-is-agent.md](./01-concepts/01-what-is-agent.md)  
2. 跑通 [03-examples](./03-examples/) 里的三个脚本  
3. 再读 [07-role-vs-project](./01-concepts/07-role-vs-project.md)，按角色卡练 `05-projects`

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
> 工程上再加一层：**Role（稳定）× Project（易变；学习里 = 练习剧本）**

## 目录

```
AiAgentStudy/
├── 01-concepts/     # 概念（含「角色优先」）
├── 02-frameworks/   # 框架对比
├── 03-examples/     # 可运行代码
├── 04-roles/        # 可复用角色卡
├── 05-projects/     # 练习剧本（组装角色，非业务交付）
└── 06-career/       # 半年：做出作品并求职
```

## 适合谁

- 会一点 Python，想搞懂 Agent  
- **没有具体业务项目**，需要一套可跟练的学习工具  
- 以前按项目拆 Agent，想改成可复用角色  
- 希望半年内做出作品、找到相关工作  

祝你半年后交出作品、拿到 offer。
