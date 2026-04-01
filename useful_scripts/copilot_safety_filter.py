#!/usr/bin/env python3
"""
Copilot Safety Filter - 用于过滤和增强 Copilot 提示的安全性

用法：作为 Copilot hooks 使用，通过 stdin 接收 JSON 输入
"""
import sys
import json
import re

# 输入格式：Copilot hooks 通常通过 stdin 传入 JSON（包含 prompt 等字段）
input_data = sys.stdin.read()
try:
    data = json.loads(input_data)
    user_prompt = data.get("prompt", "")  # 根据实际 hooks 输入结构调整字段名
except:
    user_prompt = ""

# === 1. 极简规则-based 过滤（最快、最轻量）===
def is_harmful(prompt: str) -> bool:
    prompt_lower = prompt.lower()
    
    # 常见 jailbreak / 敏感关键词模式（可自行扩展词库）
    harmful_patterns = [
        r"ignore previous instructions",
        r"ignore all rules",
        r"you are now",
        r"disregard your guidelines",
        r"jailbreak",
        r"dan mode",  # 经典越狱
        # 敏感话题示例（根据你的需求添加）
        r"(bomb|weapon|hack|crack|phish|suicide|self.?harm|child.?porn|illegal drug)"
    ]
    
    for pat in harmful_patterns:
        if re.search(pat, prompt_lower):
            return True
    return False

# === 2. 处理逻辑 ===
if is_harmful(user_prompt):
    # 方式 A：直接拒绝（推荐生产用）
    print(json.dumps({
        "action": "reject",
        "message": "抱歉，此请求包含可能违反安全政策的内容，无法处理。"
    }))
    sys.exit(1)  # 非 0 退出可让 Copilot 拦截

    # 方式 B：改写为无害（如果想保留对话）
    # sanitized = re.sub(r"敏感词|jailbreak 模式", "[已过滤]", user_prompt)
    # print(json.dumps({"action": "modify", "prompt": sanitized + "\n\n[安全提醒：请遵守合规使用]"}))
else:
    # 安全则放行，或添加防御指令
    enhanced_prompt = user_prompt + "\n\n[系统安全提醒：请严格遵守伦理和安全规范，不提供有害、非法或越狱相关内容。]"
    print(json.dumps({"action": "modify", "prompt": enhanced_prompt}))

# 如果 hooks 支持直接返回修改后的 prompt，就用 modify；否则可只做日志/拒绝。
