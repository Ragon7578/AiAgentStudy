# AI Agent 学习

从零理解 **AI Agent（智能体）**：它是什么、怎么工作、如何动手做一个。

## 你将学到什么

- Agent 与普通 Chatbot 的本质区别
- 工具调用、记忆、规划、多 Agent 协作
- 主流框架怎么选（OpenAI Agents / LangGraph / Cursor）
- 三个可运行的 Python 示例，由浅入深

## 学习路线

```
概念基础 → 框架选型 → 动手示例 → 实战项目
   │           │           │           │
 01-concepts 02-frameworks 03-examples 04-projects
```

| 阶段 | 目录 | 建议 |
|------|------|------|
| 1. 概念 | [01-concepts](./01-concepts/) | 先读完，建立心智模型 |
| 2. 框架 | [02-frameworks](./02-frameworks/) | 对照自己的场景选型 |
| 3. 示例 | [03-examples](./03-examples/) | 边跑边改，加深理解 |
| 4. 实战 | [04-projects](./04-projects/) | 独立完成一个小项目 |

## 快速开始（示例）

```bash
cd 03-examples
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt

export OPENAI_API_KEY="sk-..."   # 或兼容接口的 base_url + key
python 01-simple-chat/main.py
python 02-tool-calling/main.py
python 03-react-agent/main.py
```

> 示例默认使用 OpenAI 兼容 API。也可换成 DeepSeek、通义、Ollama 等，见各示例说明。

## 一句话定义

> **AI Agent = LLM + 工具 + 循环决策**  
> 模型不只「回答」，还会**观察 → 思考 → 行动 → 再观察**，直到完成目标。

## 目录一览

```
AiAgentStudy/
├── README.md
├── 01-concepts/          # 核心概念（建议按编号阅读）
├── 02-frameworks/        # 框架与产品对比
├── 03-examples/          # 可运行代码
└── 04-projects/          # 实战练习题
```

## 适合谁

- 会一点 Python，想搞懂 Agent 原理
- 用过 ChatGPT，想做「能干活」的自动化
- 准备在 Cursor / 工作流里用 Agent 提效

祝学习顺利。有问题直接在本仓库提 Issue。
