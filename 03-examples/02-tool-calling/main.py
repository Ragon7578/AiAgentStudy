#!/usr/bin/env python3
"""One-shot tool calling: model → tool → model → final answer."""

from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from common import make_client, model_name

# Fake weather data — focus on the calling protocol, not a real weather API.
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
            "description": "查询中国城市的当前天气。城市名用中文，如北京、上海。",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "城市中文名",
                    }
                },
                "required": ["city"],
            },
        },
    }
]


def get_weather(city: str) -> str:
    data = WEATHER_DB.get(city)
    if not data:
        return json.dumps({"error": f"暂无 {city} 的数据", "supported": list(WEATHER_DB)}, ensure_ascii=False)
    return json.dumps({"city": city, **data}, ensure_ascii=False)


DISPATCH = {
    "get_weather": lambda **kwargs: get_weather(**kwargs),
}


def main() -> None:
    client = make_client()
    messages = [
        {
            "role": "system",
            "content": "你是天气助手。需要天气数据时必须调用 get_weather，不要编造数字。",
        },
        {"role": "user", "content": "上海今天适合户外跑步吗？请根据天气给建议。"},
    ]

    first = client.chat.completions.create(
        model=model_name(),
        messages=messages,
        tools=TOOLS,
        tool_choice="auto",
    )
    msg = first.choices[0].message
    messages.append(msg)

    if not msg.tool_calls:
        print("模型未调用工具，直接回答：")
        print(msg.content)
        return

    for call in msg.tool_calls:
        name = call.function.name
        args = json.loads(call.function.arguments or "{}")
        print(f"→ 调用工具 {name}({args})")
        result = DISPATCH[name](**args)
        print(f"← 工具返回 {result}")
        messages.append(
            {
                "role": "tool",
                "tool_call_id": call.id,
                "content": result,
            }
        )

    final = client.chat.completions.create(
        model=model_name(),
        messages=messages,
    )
    print("\n最终回答：")
    print(final.choices[0].message.content)


if __name__ == "__main__":
    main()
