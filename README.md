# YouTube to Post 📺 ->📝

Convert educational videos into equivalent written materials.

Based on the challenge from [Andrej Karpathy](https://twitter.com/karpathy/status/1760740503614836917):

> Fun LLM challenge that I'm thinking about: take my 2h13m tokenizer video and translate the video into the format of a 
> book chapter (or a blog post) on tokenization.  
> Something like: 
> 
> 1.  Whisper the video
> 2.  Chop up into segments of aligned images and text
> 3.  Prompt engineer an LLM to translate piece by piece
> 4.  Export as a page, with links citing parts of original video
>
> More generally, a workflow like this could be applied to any input video and auto-generate "companion guides" for 
> various tutorials in a more readable, skimmable, searchable format. Feels tractable but non-trivial.


## Generated posts
[Let's build the GPT Tokenizer](./pages/Let's%20build%20the%20GPT%20Tokenizer)


## Prompts & scripts
[This Wordware prompt](https://app.wordware.ai/r/b058e9c3-ffee-4661-a5e3-c788eef0dfbc) takes in the JSON output from 
running Whisper (I used [this one](https://replicate.com/vaibhavs10/incredibly-fast-whisper) on 
[Replicate](https://replicate.com/)) and processes it into sections of a written lesson.

The simple script in `scripts/convert.py` turns the output into a set of Markdown files that are then served via GitHub 
pages.

### Getting the transcript
[Here](https://gist.github.com/wordware-ai/95312691264f66c7a893ab1dfea15807) is the output from running Whisper on the 
audio track of [Andrej's Tokenizer video](https://www.youtube.com/watch?v=zduSFxRajkE). 

Alternatively you can run [`youtube-dl`](https://github.com/ytdl-org/youtube-dl) on the video e.g.
```commandline
youtube-dl --extract-audio --audio-format mp3 "https://www.youtube.com/watch?v=<video_id>"
```
then run it through a transcription model like [this one](https://replicate.com/vaibhavs10/incredibly-fast-whisper).
