# Swiss Grid Video · 9:16 瑞士网格科普动效视频工作流

把你的方法论、AI 工作流或深度复盘，通过 Agent 自动拆解并渲染成 **Remotion 级弹簧动效 + 圆形真人头像声波环 + 逐字卡点字幕 + 真实音效** 的 9:16 竖屏讲解视频。

---

## 一、环境依赖（一次性安装）

```bash
# 1. Node.js 20+ & FFmpeg（macOS）
brew install node ffmpeg

# 2. Playwright Chromium（用于 1080x1920 逐帧无损渲染）
npm install playwright
npx playwright install chromium
```

---

## 二、三种配音方案完整配置指南（按门槛从低到高）

复制 `.env.example` 为 `.env`，`config.example.json` 为 `config.json`（均已在 `.gitignore` 中，不会被提交到 Git）。

### 方案 A：完全免费、零 API Key（Edge TTS · 新手首选）

不需要注册任何账号、不需要信用卡，直接调用微软 Edge 神经语音并自动产出逐字时间戳：

```bash
pip install edge-tts
```

在 `config.json` 中配置：
```json
{
  "tts": {
    "engine": "edge",
    "voice": "zh-CN-YunxiNeural",
    "rate": "+18%"
  }
}
```
常用自然中文音色推荐：
- 男声知性讲解：`zh-CN-YunxiNeural` / `zh-CN-YunjianNeural`
- 女声清亮干练：`zh-CN-XiaoxiaoNeural` / `zh-CN-XiaoyiNeural`

运行示例：
```bash
python3 scripts/tts-edge.py ./my-episode
```

---

### 方案 B：本机免费离线克隆自己的声音（Apple Silicon Mac · Qwen3-TTS MLX）

完全在本地 Apple Silicon GPU 跑通，**零费用、声音样本不上传云端**。

1. **安装本地 MLX 语音环境**：
   ```bash
   python3 -m venv .venv-voice
   source .venv-voice/bin/activate
   pip install mlx mlx-audio numpy
   ```
2. **下载 4-bit 量化模型**（约 0.5 GB，支持中文克隆）：
   - HuggingFace：`mlx-community/Qwen3-TTS-12Hz-0.6B-Base-4bit`
3. **准备你的本人干声样本**：
   - 在安静书房用手机或麦克风录 **8–15 秒** 自然连续讲解的干声（无背景音乐、无明显回声），保存为单声道 WAV（如 `assets/my-voice-ref.wav`）；
   - 逐字记下这段录音的准确文字作为 `ref_text`（标点准确能显著提升断句自然度）。
4. **避坑提示**：
   - 0.6B 本地模型在遇到“中英夹杂 + 空格”（如 `去 AI 味`）时偶尔会有轻微气口停顿；喂给模型前务必去掉中英之间的空格（如 `去AI味`），屏幕上仍显示带空格的标准字幕；
   - 建议先以 1.0x 生成，再用 FFmpeg `atempo=1.2` 不变调加速。

---

### 方案 C：云端高自然度克隆自己的声音（火山引擎 / 豆包语音 ICL 2.0 · 推荐日更）

中英混排（GPT / Markdown / Skill / Python）连读最自然，支持原生 `1.2x` 语速不变调，且直接返回毫秒级逐字时间戳 `words[]` 用于精确字幕卡点。

1. **获取本人复刻音色 ID**：
   - 登录火山引擎语音技术控制台 → 进入「**声音复刻（豆包语音 ICL 2.0）**」；
   - 按提示朗读 10–20 秒完成声音复刻，拿到以 `S_` 开头的专属音色 ID（例如 `S_xxxxxxxxx`）；
   - 在控制台创建 API Key（或 AppId + AccessToken），并确认已开通资源 ID **`seed-icl-2.0`**（旧版 1.0 为 `volc.megatts.default`）。
2. **填入本地 `.env`（绝不提交到 Git）**：
   ```env
   VOLC_TTS_API_KEY=你的火山API_KEY
   VOLC_TTS_RESOURCE_ID=seed-icl-2.0
   VOLC_TTS_VOICE=S_你的复刻音色ID
   VOLC_TTS_SPEED=20
   ```
   *(说明：`VOLC_TTS_SPEED=20` 对应原生 `1.2x` 语速，范围 `-50 ~ 100`，`0` 为原速。)*

---

## 三、圆形真人头像 + 实时声波环配置

1. 准备一张 `1:1` 清晰正面半身肖像（建议 500×500 以上，暖光背景最搭米白网格），放到本地 `assets/avatar.jpg`（已在 `.gitignore` 中）；
2. 在 `config.json` 中设置 `"avatar": "assets/avatar.jpg"`（设为 `""` 则自动隐藏头像）；
3. 声波环由干净人声轨的逐帧 RMS 振幅实时驱动，开口跳动、停顿静止，完全不受背景音效干扰。

---

## 四、真实音效（SFX）接入规范

- **严禁使用代码合成白噪声/正弦波扫频**，容易与人声频段打架；
- 建议使用真实采样的短促 UI 音效（放入本地 `assets/sfx/`）：
  - `typing.mp3`（打字机输入，音量 `0.25`）
  - `click-soft.mp3`（发送/点击，音量 `0.32`）
  - `whoosh-short.mp3`（切幕微转场，音量 `0.16`）
  - `pop.mp3` / `chime.mp3`（卡片弹出/验收提示，音量 `0.18`）
- 混音统一加 `highpass=f=120` 低切与 `alimiter=limit=0.95` 限幅，确保清晰托底、绝不抢人声。

---

## 五、配合 Agent 一句话开工

把本 Skill 挂载到你的 Agent（Claude Code / Codex / Antigravity）后，直接说：

> 「用 `swiss-grid-video` 工作流，帮我做一个 9:16 竖屏讲解视频，主题是《XXXX》，先按 6 步标准给我分幕脚本和每幕的视觉隐喻表，我确认后再配音渲染。」
