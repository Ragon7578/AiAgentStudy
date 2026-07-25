"""Shared OpenAI-compatible client helpers for the study examples."""

from __future__ import annotations

import os
import sys

from openai import OpenAI


def require_api_key() -> str:
    key = os.getenv("OPENAI_API_KEY")
    if not key:
        print(
            "缺少 OPENAI_API_KEY。\n"
            "示例：\n"
            '  export OPENAI_API_KEY="sk-..."\n'
            "可选：\n"
            '  export OPENAI_BASE_URL="https://api.openai.com/v1"\n'
            '  export OPENAI_MODEL="gpt-4o-mini"',
            file=sys.stderr,
        )
        sys.exit(1)
    return key


def make_client() -> OpenAI:
    require_api_key()
    base_url = os.getenv("OPENAI_BASE_URL")
    if base_url:
        return OpenAI(base_url=base_url)
    return OpenAI()


def model_name(default: str = "gpt-4o-mini") -> str:
    return os.getenv("OPENAI_MODEL", default)
