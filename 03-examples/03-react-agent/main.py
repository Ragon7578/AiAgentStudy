#!/usr/bin/env python3
"""Minimal ReAct-style agent loop with multiple tool calls."""

from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from common import make_client, model_name

WEATHER_DB = {
    "北京": {"temp_c": 24, "condition": "晴", "aqi": 65},
    "上海": {"temp_c": 28, "condition": "小雨", "aqi": 70},
    "深圳": {"temp_c": 31, "condition": "多云", "aqi": 42},
}

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "查询城市天气。城市名用中文。",
            "parameters": {
                "type": "object",
                "properties": {"city": {"type": "string"}},
                "required": ["city"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "calculator",
            "description": "计算简单算术表达式，例如 28-24 或 (31+24)/2。仅支持数字与 + - * / ()。",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "算术表达式",
                    }
                },
                "required": ["expression"],
            },
        },
    },
]


def get_weather(city: str) -> str:
    data = WEATHER_DB.get(city)
    if not data:
        return json.dumps(
            {"error": f"暂无 {city} 的数据", "supported": list(WEATHER_DB)},
            ensure_ascii=False,
        )
    return json.dumps({"city": city, **data}, ensure_ascii=False)


def calculator(expression: str) -> str:
    allowed = set("0123456789+-*/(). ")
    if not expression or any(ch not in allowed for ch in expression):
        return json.dumps({"error": "非法表达式"}, ensure_ascii=False)
    try:
        value = eval(expression, {"__builtins__": {}}, {})  # noqa: S307 — sandboxed arithmetic only
    except Exception as exc:  # noqa: BLE001 — return error to the model
        return json.dumps({"error": str(exc)}, ensure_ascii=False)
    return json.dumps({"expression": expression, "result": value}, ensure_ascii=False)


DISPATCH = {
    "get_weather": lambda **kw: get_weather(**kw),
    "calculator": lambda **kw: calculator(**kw),
}


def run_agent(question: str, max_steps: int = 6) -> str:
    client = make_client()
    messages: list[dict] = [
        {
            "role": "system",
            "content": (
                "你是会使用工具的研究助手。"
                "需要天气时用 get_weather；需要算数时用 calculator。"
                "信息足够后直接给出中文最终答案，不要无意义地重复调用工具。"
            ),
        },
        {"role": "user", "content": question},
    ]

    for step in range(1, max_steps + 1):
        print(f"\n===== 第 {step} 步 =====")
        response = client.chat.completions.create(
            model=model_name(),
            messages=messages,
            tools=TOOLS,
            tool_choice="auto",
        )
        msg = response.choices[0].message
        messages.append(msg)

        if msg.content:
            print(f"模型: {msg.content}")

        if not msg.tool_calls:
            return msg.content or "(空回复)"

        for call in msg.tool_calls:
            name = call.function.name
            args = json.loads(call.function.arguments or "{}")
            print(f"Action: {name}({args})")
            if name not in DISPATCH:
                result = json.dumps({"error": f"未知工具 {name}"}, ensure_ascii=False)
            else:
                result = DISPATCH[name](**args)
            print(f"Observation: {result}")
            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": call.id,
                    "content": result,
                }
            )

    return "达到最大步数仍未结束，请缩小问题或增加 max_steps。"


def main() -> None:
    question = (
        sys.argv[1]
        if len(sys.argv) > 1
        else "北京和上海的温差是多少度？结合天气，哪个更适合户外运动？"
    )
    print(f"问题: {question}")
    answer = run_agent(question)
    print("\n===== 最终答案 =====")
    print(answer)


if __name__ == "__main__":
    main()
