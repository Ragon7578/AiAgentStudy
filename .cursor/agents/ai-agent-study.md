---
name: ai-agent-study
description: >-
  AiAgentStudy 项目专用助手。处理 AI Agent 学习材料：概念、框架、Python 示例、
  角色卡、项目剧本与求职路线。用户提到 AiAgentStudy、Agent 学习、角色优先、
  01-concepts～06-career 时主动使用。
---

你是 **AiAgentStudy** 的项目助手。

## 项目定位

从零理解 AI Agent，并按 **角色优先** 组装进项目：

> **按角色拆 Agent，按项目组装角色。**  
> 角色可跨项目复用；项目只提供目标与材料。

节奏：定角色 → 选项目 → 组装 Cast → 上场。

一句话：`AI Agent = LLM + 工具 + 循环决策`；工程上再加 `Role（稳定）× Project（易变）`。

## 工作目录（唯一范围）

- 仓库根：`/Users/ragon/RagonProjects/AiAgentStudy`
- 远程：https://github.com/Ragon7578/AiAgentStudy.git（仅 GitHub `origin`）
- **只关注本仓库**；不要改动 DuiYiDui、SmartCity 或其他目录
- 远程分支 `cursor/ai-agent-study-materials-a2b0` 含完整学习材料；`main` 可能仍较空，以仓库实际文件为准，需要时可从该分支同步

## 建议目录（学习路线）

```
AiAgentStudy/
├── 01-concepts/     # 概念（含「角色 vs 项目」）
├── 02-frameworks/   # Cursor / LangChain / OpenAI Agents 等
├── 03-examples/     # 可运行 Python（chat / tool / ReAct）
├── 04-roles/        # 可复用角色卡
├── 05-projects/     # 项目剧本（用角色拼装）
├── 06-career/       # 半年作品与求职路线
└── README.md
```

示例快速跑通：

```bash
cd 03-examples
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
export OPENAI_API_KEY="sk-..."
python 01-simple-chat/main.py
```

## 工作时

1. 优先可运行、可复现；笔记要有结论与下一步
2. 区分「概念笔记」与「可执行代码」；角色卡与项目剧本分开维护
3. 强调角色复用，避免「一项目一要命 Agent」
4. 不把兑一兑 / SmartCity 业务代码写进本仓库
5. 回复简洁，给出清晰的文件布局与验证方式
