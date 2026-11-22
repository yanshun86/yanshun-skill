#!/usr/bin/env python3
"""
免费零 API Key 配音脚本（Edge TTS）
用法：python3 scripts/tts-edge.py <project_dir>
输入：<project_dir>/script.json  [{"id":"s01","text":"..."}, ...]
输出：<project_dir>/audio/<id>.mp3 + <project_dir>/audio/manifest.json（含逐字时间戳 words[]）
"""
import asyncio, json, os, re, subprocess, sys
from pathlib import Path
import edge_tts

VOICE = os.environ.get("EDGE_TTS_VOICE", "zh-CN-YunxiNeural")
RATE = os.environ.get("EDGE_TTS_RATE", "+18%")
LEAD = 0.20
HOLD = 0.45

def clean_for_tts(text: str) -> str:
    text = re.sub(r"([\u4e00-\u9fff])\s+([A-Za-z0-9])", r"\1\2", text)
    text = re.sub(r"([A-Za-z0-9])\s+([\u4e00-\u9fff])", r"\1\2", text)
    return text

def get_duration(path: Path) -> float:
    out = subprocess.check_output([
        "ffprobe", "-v", "quiet", "-show_entries", "format=duration", "-of", "csv=p=0", str(path)
    ]).decode().strip()
    return float(out or 0)

async def synth_scene(sc, out_dir: Path):
    sid = sc["id"]
    tts_text = clean_for_tts(sc["text"])
    mp3 = out_dir / f"{sid}.mp3"
    comm = edge_tts.Communicate(tts_text, VOICE, rate=RATE, boundary="WordBoundary")
    words = []
    with open(mp3, "wb") as f:
        async for chunk in comm.stream():
            if chunk["type"] == "audio":
                f.write(chunk["data"])
            elif chunk["type"] == "WordBoundary":
                st = chunk["offset"] / 1e7
                et = (chunk["offset"] + chunk["duration"]) / 1e7
                words.append({"word": chunk["text"], "startTime": round(st, 3), "endTime": round(et, 3)})
    dur = get_duration(mp3)
    return mp3, dur, words

async def main():
    proj = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    scenes = json.loads((proj / "script.json").read_text(encoding="utf-8"))
    out_dir = proj / "audio"
    out_dir.mkdir(parents=True, exist_ok=True)
    manifest = []
    cursor = 0.0
    for sc in scenes:
        mp3, dur, words = await synth_scene(sc, out_dir)
        scene_dur = round(LEAD + dur + HOLD, 3)
        manifest.append({
            "id": sc["id"],
            "text": sc["text"],
            "audio": str(mp3),
            "audioDuration": round(dur, 3),
            "lead": LEAD,
            "hold": HOLD,
            "start": round(cursor, 3),
            "duration": scene_dur,
            "words": words,
        })
        cursor += scene_dur
        print(f"[edge-tts] ✓ {sc['id']} audio={dur:.2f}s words={len(words)}")
    (out_dir / "manifest.json").write_text(
        json.dumps({"engine": "edge", "voice": VOICE, "totalDuration": round(cursor, 3), "scenes": manifest}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"DONE! Total duration: {cursor:.2f}s")

if __name__ == "__main__":
    asyncio.run(main())
