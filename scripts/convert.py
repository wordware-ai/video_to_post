import json
from pathlib import Path
from urllib.parse import quote


def main():
    # This script converts the output of running the Wordware prompt into a set of markdown files that can be served as
    # GitHub pages
    project_name = "Let's build the GPT Tokenizer"
    input_path = Path("~/Documents/Random/Karpathy Tokenizer").expanduser() / "karpathy_tokenizer.json"

    with input_path.open() as f:
        data = json.load(f)

    output_folder = Path("../pages") / project_name
    output_folder.mkdir(exist_ok=True)

    sections = []
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

        section_path = output_folder / f"{i + 1}. {title}.md"
        sections.append({"path": section_path, "name": title})
        with section_path.open('w') as f:
            f.write(f"# {title}\n\n{content}\n\n[Video link]({yt_url})")

    with (output_folder / "index.md").open('w') as f:
        paths = "\n\n".join([f"[{i+1}. {s['name']}]({quote(str(s['path'].relative_to(output_folder).with_suffix('')))})" for i, s in enumerate(sections)])
        f.write(f"# {project_name}\n\n{paths}")


if __name__ == '__main__':
    main()
