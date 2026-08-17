#!/usr/bin/env python3
"""Plain chat — baseline before introducing tools and loops."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from common import make_client, model_name


def main() -> None:
    client = make_client()
    user_message = "用三句话解释什么是 AI Agent，面向初学者。"

    response = client.chat.completions.create(
        model=model_name(),
        messages=[
            {
                "role": "system",
                "content": "你是简洁的中文老师，解释清楚即可，不要堆砌术语。",
            },
            {"role": "user", "content": user_message},
        ],
    )

    answer = response.choices[0].message.content
    print(f"用户: {user_message}")
    print(f"助手: {answer}")


if __name__ == "__main__":
    main()
