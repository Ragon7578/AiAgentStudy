# 可运行示例

三个示例，由浅入深。依赖同一套 `requirements.txt`。

## 环境

```bash
cd 03-examples
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

设置环境变量（任选一种后端）：

```bash
# OpenAI 官方
export OPENAI_API_KEY="sk-..."

# 兼容接口（DeepSeek / 通义 / 本地网关等）
export OPENAI_API_KEY="你的key"
export OPENAI_BASE_URL="https://api.deepseek.com"   # 示例
export OPENAI_MODEL="deepseek-chat"                 # 示例
```

本地 Ollama（若已启动且提供 OpenAI 兼容端口）：

```bash
export OPENAI_API_KEY="ollama"
export OPENAI_BASE_URL="http://localhost:11434/v1"
export OPENAI_MODEL="qwen2.5"   # 需支持 tool calling
```

## 示例列表

| 目录 | 学什么 |
|------|--------|
| [01-simple-chat](./01-simple-chat/) | 纯 LLM 对话，还没有 Agent |
| [02-tool-calling](./02-tool-calling/) | 一次工具调用闭环 |
| [03-react-agent](./03-react-agent/) | 多步 ReAct 循环（真正的迷你 Agent） |

共享客户端逻辑：[common.py](./common.py)

## 跑起来

```bash
python 01-simple-chat/main.py
python 02-tool-calling/main.py
python 03-react-agent/main.py
```

没有 API Key 时，脚本会打印配置说明并以非零状态退出。
