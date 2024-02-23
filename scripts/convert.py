import json
import time
from pathlib import Path


def main():
    # This script converts the output of running the Wordware prompt into a set of markdown files that can be served as
    # GitHub pages
    base_path = Path("~/Documents/Random/Karpathy Tokenizer").expanduser()
    input_path = base_path / "karpathy_tokenizer.json"

    with input_path.open() as f:
        data = json.load(f)

    for i, section in enumerate(data['loop_sections']['generations']):
        if i > 23:
            break
        # print(list(section['YT->BP/Write section'].keys()))
        title = section['YT->BP/Write section']['get_section_title']['logs']
        print(title)
        content = section['YT->BP/Write section']['content']
        print(content)
        yt_url = section['YT->BP/Get time stamped URL']['time']['output']
        print(yt_url)

        folder = base_path / f"{time.strftime('%Y%m%d-%H%M%S')}"
        folder.mkdir(exist_ok=True)
        with (folder / f"{i+1}. {title}.md").open('w') as f:
            f.write(f"# {title}\n\n{content}\n\n[Video link]({yt_url})")


if __name__ == '__main__':
    main()
