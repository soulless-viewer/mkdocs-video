import mkdocs
import lxml.html
from mkdocs.config import config_options
from mkdocs.exceptions import ConfigurationError


class Plugin(mkdocs.plugins.BasePlugin):
    config_scheme = (
        ("mark", config_options.Type(str, default="type:video")),
        ("is_video", config_options.Type(bool, default=False)),
        ("video_type", config_options.Type(str, default="mp4")),
        ("video_muted", config_options.Type(bool, default=False)),
        ("video_loop", config_options.Type(bool, default=False)),
        ("video_controls", config_options.Type(bool, default=True)),
        ("video_autoplay", config_options.Type(bool, default=False)),
        ("css_style", config_options.Type(
            dict,
            default={
                "position": "relative",
                "width": "100%",
                "height": "22.172vw"
            }
        ))
    )


    def on_page_content(self, html, page, config, files):
        content = lxml.html.fromstring(html)
        tags = content.xpath(f'//img[@alt="{self.config["mark"]}" and @src]')
        for tag in tags:
            if not tag.attrib.get("src"):
                continue
            tag.getparent().replace(tag, self.create_repl_tag(tag))
        return lxml.html.tostring(content, encoding="unicode")


    def create_repl_tag(self, tag):
        """
        Сreate a replacement tag with the specified source and style.

        return: str
        """

        is_video = self.config["is_video"]
        # Override global config if desired tag is specified
        # use global default if both are specified
        if "video" in tag.attrib:
            if "iframe" not in tag.attrib:
              is_video = True
            tag.attrib.pop('video')
        if "iframe" in tag.attrib:
            if "video" not in tag.attrib:
              is_video = False
            tag.attrib.pop('iframe')

        repl_tag = lxml.html.Element("video" if is_video else "iframe")

        # Basic config if global is disabled
        if is_video:
            repl_subtag = lxml.html.Element("source")
            repl_subtag.set("src", tag.attrib["src"])
            video_type = self.config["video_type"].lower().strip()
            if any(i in video_type for i in [" ", "/"]):
                raise ConfigurationError("Unsupported video type")
            video_type = f"video/{video_type}"
            repl_subtag.set("type", video_type)
            repl_tag.append(repl_subtag)
        else:
            repl_tag.set("src", tag.attrib["src"])

        # Extended config if global is enabled
        if "disable-global-config" not in tag.attrib:
            css_style = ";".join(
                [f"{k}:{v}" for k, v in self.config["css_style"].items()]
            )
            repl_tag.set("style", css_style)

            if is_video:
                if self.config["video_loop"]:
                    repl_tag.set("loop")
                if self.config["video_muted"]:
                    repl_tag.set("muted")
                if self.config["video_controls"]:
                    repl_tag.set("controls")
                if self.config["video_autoplay"]:
                    repl_tag.set("autoplay")
            else:
                repl_tag.set("frameborder", "0")
                repl_tag.set("allowfullscreen")
        else:
            tag.attrib.pop("disable-global-config")

        # Remove alt attribute - video/iframe doesn't have an alt attribute
        tag.attrib.pop('alt')

        # Duplicate everything from original tag (except 2)
        for attr, val in tag.attrib.items():
            if "src" != attr:
                repl_tag.set(attr, val if val else None)

        div = lxml.html.Element("div")
        div.set("class", "video-container")
        div.append(repl_tag)

        return div
