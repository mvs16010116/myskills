---
name: video-pipeline
description: Generate a narrated animated Chinese-news video (Lottie, text-only scenes, burned subtitles, +10dB audio) from a plain-text news script. Use when the user provides a copy/text and wants a finished MP4 video, is writing a new 侯哥军情-style geopolitics/finance video, or asks to reuse the "houge/ulchi" pipeline.
---

# Video Pipeline — 文案 → 成片

把一篇中文文案转成「带旁白 + 纯文字分镜动画 + 烧录字幕 + 音轨」的 MP4，基于 houge / ulchi 两个已验证项目沉淀的通用流水线。

## 前置条件

- 项目根：`D:\Danny\projects\animation\lottie`
- 依赖：`python -m edge_tts`（TTS）、ffmpeg/ffprobe 在 PATH、`canvaskit-wasm` 已安装
- 字体：场景目录必须含 `msyh.ttc`（否则 Skottie 渲染文字为空 —— 流水线会自动从 `public/projects/houge/scene-1/msyh.ttc` 复制）

## 核心命令

```bash
# 从一个新配置生成完整视频
# 1) 新建配置：scripts/projects/<name>.json（结构见下）
# 2) 跑流水线
node scripts/pipeline.mjs <name>
#   常用开关：--force 忽略全部缓存重新生成
#             --no-render 只到字幕(1-5步)不渲染，快速验证文案与分镜
```

产物：
- `scripts/.tts-<name>/clip-N.mp3` 每镜旁白
- `scripts/.tts-<name>/timeline.json` 镜头时间轴（旁白驱动）
- `scripts/.tts-<name>/full_audio.m4a` 音轨（带 +10dB）
- `scripts/.tts-<name>/subtitles.ass` 烧录字幕
- `public/projects/<name>/scene-1/<name>-scene-1.mp4` **最终成片**

## 配置 schema（scripts/projects/<name>.json）

```jsonc
{
  "title": "HouGe Geo Alert",            // lottie 文档名
  "channel": "侯哥军情 · 地缘观察",       // 顶部小字条
  "voice": "zh-CN-YunyangNeural",        // edge-tts 音色
  "rate": "+0%",
  "font": "public/projects/houge/scene-1/msyh.ttc",
  "segments": [                          // 每镜一条
    {
      "narration": "……",                // 旁白全文，驱动该镜时长（TTS 读这段）
      "subtitle": "……",                 // 字幕文案（自动 ≤17字/行 标点断行）
      "texts": [                         // 镜内文字层，按数组顺序 stagger 入场(+50帧/层)
        { "nm": "title", "t": "…", "size": 58, "color": "textMain", "cy": 156,
          "cx": 256, "wrapW": 470, "opacity": 90, "tr": 0 }
      ],
      "mark": { "word": "军演", "size": 100, "cy": 452 }  // 可选：淡色大字水印
    }
  ]
}
```

- `color` 取值：`textMain` | `textDim` | `alert` | `amber` | `cyan` | `okay` | `panel`
- `texts[].nm` 需在整篇内唯一（层名）；`cy` 为文字块垂直中心；画布 512×512
- 字幕断行规则：≤17 字/行、在 `，。！？；：、—` 边界用 `\N` 换行、超长词硬折 —— 由 pipeline 自动处理，无需手工加 `\N`

## 视频约定（与 houge/ulchi 完全一致）

- 画布 512×512，60fps，微软雅黑（MSYH）
- **纯文字分镜**：不要加国旗/铁链/K线/图形等矢量对象；被删图形的"视觉锚点"用淡色大字水印 `panel` 色补位
- 顶部小字条 `channel`；每个镜头标题/强调/副文案分层，主色阶梯：白主标题、`alert` 强调、`amber` 警示数字、`cyan` 冷信息、`textDim` 说明
- 字幕：底部安全区（Alignment 2、MarginV 30、fontsize 26），停留 = 旁白窗口对齐语音
- 音频：旁白叠放 adelay 分镜定位，amix 归一化 `normalize=0` + `volume=10dB`

## 踩坑记录（必须遵守）

1. **字幕时序**：`timeline.startSec` 已含 LEAD(0.9s)，字幕起点用 `startSec + 0.2`（对齐 TTS 内嵌前导静音后的说话起点），**不要再减 0.9**，否则字幕比语音早 1.1s。
2. **字体必须存在**：`msyh.ttc` 未复制到场景目录时，Skottie 渲染全部文字为空、只有背景和烧录字幕。流水线会自动复制，删除场景 `msyh.ttc` 会导致空白成片。
3. **ffmpeg ASS 路径**：Windows 下字幕路径含冒号会被 ass filter 解析错乱。解决：把 `.ass` 复制为 `burn.ass`，用相对路径 + `cwd: 输出目录` 调用 ffmpeg。
4. **旁白驱动时长**：每镜 `dur = clipDur + LEAD(0.9) + TAIL(0.8)`；镜头间留白由时间轴自动算出，文案切镜以"段落语义"为准（通常一段一镜）。
5. **TTS 大段文字**：长镜旁白（>20s）没问题，但字幕文案要精简，别照抄 narration（narration 用于语音，subtitle 用于显示）。
6. PIP 依赖 edge-tts 只在有网环境可用；已生成的 clip-N.mp3 会被缓存跳过（`--force` 才重生成）。

## 验证步骤（成片后必须做）

1. 检查流与时长：
   ```bash
   ffprobe -v error -show_entries stream=codec_type,codec_name -of compact public/projects/<name>/scene-1/<name>-scene-1.mp4
   ```
   期望：h264 视频 + aac 音频，时长 ≈ timeline.totalSec。
2. **字幕-语音同步**（重点）：用 silencedetect 找语音区间，与 `subtitles.ass` 事件对比，字幕应在语音开始 ~0.2s 内出现：
   ```bash
   ffmpeg -i scripts/.tts-<name>/full_audio.m4a -af silencedetect=noise=-35dB:d=0.4 -f null - 2>&1 | grep silence_
   ```
   抽查 2–3 个镜头边界即可。
3. **画面内容**：抽关键帧验证文字渲染非空白（有字幕不代表 Lottie 文字渲染成功——字体缺失时两者会混淆）：
   ```bash
   ffmpeg -y -ss <mid-sec> -i public/projects/<name>/scene-1/<name>-scene-1.mp4 -frames:v 1 /tmp/chk.png
   ```
   或用像素直方图检查中间区域是否出现主色调文字。
4. lottie.json 层类型：应只有 1 个 `ty:4`（背景）+ 若干 `ty:5`（文字）。

## 参考实现

- 流水线：`scripts/pipeline.mjs`（自包含，含 TTS/时间轴/混流/Lottie/字幕/渲染/混流全逻辑）
- 配置示例：`scripts/projects/houge.json`（9 镜）、`scripts/projects/ulchi.json`（5 镜）
- 独立渲染入口：`scripts/export-video.mjs <project> <scene> [--out ...] [--frame-dir ...]`