# Copilot Safety Filter

> 用于过滤和增强 Copilot 提示的安全性脚本

**发布时间：** 2026-04-01 11:25

```markdown
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
    user_prompt = data.get("prompt", "")
except:
    user_prompt = ""

# === 1. 极简规则-based 过滤（最快、最轻量）===
def is_harmful(prompt: str) -> bool:
    prompt_lower = prompt.lower()
    harmful_patterns = [
        r"ignore previous instructions",
        r"ignore all rules",
        r"you are now",
        r"disregard your guidelines",
        r"jailbreak",
        r"dan mode",
        r"(bomb|weapon|hack|crack|phish|suicide|self.?harm|child.?porn|illegal drug)"
    ]
    for pat in harmful_patterns:
        if re.search(pat, prompt_lower):
            return True
    return False

# === 2. 处理逻辑 ===
if is_harmful(user_prompt):
    print(json.dumps({
        "action": "reject",
        "message": "抱歉，此请求包含可能违反安全政策的内容，无法处理。"
    }))
    sys.exit(1)
else:
    enhanced_prompt = user_prompt + "\n\n[系统安全提醒：请严格遵守伦理和安全规范，不提供有害、非法或越狱相关内容。]"
    print(json.dumps({"action": "modify", "prompt": enhanced_prompt}))
```
