# MkDocs Video

This plugin allows you to embed videos on the documentation pages using a simple Markdown syntax.

## Contents

* [Installation](#installation)
* [Usage](#usage)
* [Configuration](#configuration)  
    * [Marker](#marker)
    * [Style](#style)
    * [Tag `<video>`](#tag-video)
    * [Video type](#video-type)
    * [Video autoplay](#video-autoplay)
    * [Video loop](#video-loop)
    * [Video muted](#video-muted)
    * [Video controls](#video-controls)
* [Embedding examples](#embedding-examples)

## Installation

Install the package with pip:

```bash
$ pip install mkdocs-video
```

Enable the plugin in the `mkdocs.yml` file:

```yaml
plugins:
    - mkdocs-video
```

> See how to use [MkDocs Plugins](https://www.mkdocs.org/dev-guide/plugins/#using-plugins)

## Usage

To add a video to the final documentation page, you need to use the Markdown syntax for images with a **specific name** *(hereinafter ***marker***)*.

> See how to use [Markdown syntax](https://guides.github.com/features/mastering-markdown/)

**Example:**

*content folder structure*

```
├── content
|   ├── ...
│   ├── video.md
│   └── videos
│       └── costa_rica.mp4
└── mkdocs.yml
```

*video.md*
```
# Video example

Lorem ipsum dolor sit amet

![type:video](https://www.youtube.com/embed/LXb3EKWsInQ)
```

*\<mkdocs-url>/video*

![](https://user-images.githubusercontent.com/29832584/123962612-5188db00-d9ba-11eb-9e0f-1470ca57c452.png)

You can also use relative paths for videos stored together with your content
```
![type:video](./videos/costa_rica.mp4)
```

## Configuration

The following parameters can be used to change the functionality and appearance of video elements in the final HTML. Keep in mind that the plugin configuration parameters are applied globally to all relevant [marked](#marker) elements. To fine-tune each video element, you can use the [Attribute Lists](https://python-markdown.github.io/extensions/attr_list/) extension.

When using this plugin and the mentioned extension together, the following rules apply *(with an illustrative examples)*:

0. *[Let's assume we have this plugin configuration]*
   ```yaml
   # mkdocs.yml
   markdown_extensions:
     - attr_list
   plugins:
     - mkdocs-video:
         is_video: True
         video_muted: True
         video_controls: True
         css_style:
           width: "50%"
   ```

1. The plugin attributes are used globally by default
   ```markdown
   ![type:video](video.mp4)
   ```
   ```html
   <video style="width:50%" muted="" controls="" alt="type:video">
      <source src="video.mp4" type="video/mp4">
   </video>
   ```

2. The extension attributes will override the corresponding plugin attributes, but the rest will remain by default.
   ```markdown
   ![type:video](video.mp4){: style='width: 100%'}
   ```
   ```html
   <video style="width: 100%" muted="" controls="" alt="type:video">
      <source src="video.mp4" type="video/mp4">
   </video>
   ```

3. The plugin attributes can be disabled for specific video element by adding `disable-global-config` attribute.
   ```markdown
   ![type:video](video.mp4){: disable-global-config style='width: 100%'}
   ```
   ```html
   <video alt="type:video" style="width: 100%">
      <source src="video.mp4" type="video/mp4">
   </video>
   ```

4. The extension attribute `src` will override video source... Do what you want with this info 🙃.
   ```markdown
   ![type:video](video.mp4){: src='another-video.mp4'}
   ```
   ```html
   <video style="width:50%" muted="" controls="" alt="type:video">
      <source src="another-video.mp4" type="video/mp4">
   </video>
   ```

### Marker

By default, the string `type:video` is used as a **marker** in the Markdown syntax.

You can change this value by adding the following lines to your `mkdocs.yml`:

```yaml
plugins:
  - mkdocs-video:
      mark: "custom-marker"
```

Now you can use this **marker** in the Markdown syntax:

```
![custom-marker](https://www.youtube.com/embed/LXb3EKWsInQ)
```

### Style

By default, the following CSS styles are used for the `<iframe>` tag that is inserted into the final page:

```css
position: relative;
width: 100%;
height: 22.172vw;
```

You can change the style by adding the following lines to your `mkdocs.yml`:

```yaml
plugins:
  - mkdocs-video:
      css_style:
        width: "100%"
        height: "22.172vw"
        ...
```

### Tag `<video>`

By default, the `<iframe>` tag will be used to display the video in the final page, but in some cases you may need to use `<video>` tag instead. You can use it by adding the following lines to your `mkdocs.yml`:

```yaml
plugins:
  - mkdocs-video:
      is_video: True
      ...
```

### Video type

> This parameter will only work with the `<video>` tag (`is_video: True`)

You can specify the MIME type of the video *(default: `mp4`)* resource by adding the following lines to your `mkdocs.yml`:

```yaml
plugins:
  - mkdocs-video:
      is_video: True
      video_type: ogg
      ...
```

### Video autoplay

> This parameter will only work with the `<video>` tag (`is_video: True`)

You can specify whether the video should be played automatically *(default: `False`)* or not by adding the following lines to your `mkdocs.yml`:

```yaml
plugins:
  - mkdocs-video:
      is_video: True
      video_autoplay: True
      ...
```

> The operation of this parameter may be affected by browser settings or video provider configuration

### Video loop

> This parameter will only work with the `<video>` tag (`is_video: True`)

You can specify whether the video should be looped *(default: `False`)* or not by adding the following lines to your `mkdocs.yml`:

```yaml
plugins:
  - mkdocs-video:
      is_video: True
      video_loop: True
      ...
```

> The operation of this parameter may be affected by browser settings or video provider configuration

### Video muted

> This parameter will only work with the `<video>` tag (`is_video: True`)

You can specify whether the video should be muted *(default: `False`)* or not by adding the following lines to your `mkdocs.yml`:

```yaml
plugins:
  - mkdocs-video:
      is_video: True
      video_muted: True
      ...
```

> The operation of this parameter may be affected by browser settings or video provider configuration

### Video controls

> This parameter will only work with the `<video>` tag (`is_video: True`)

You can specify whether the video controls should be displayed *(default: `True`)* or not by adding the following lines to your `mkdocs.yml`:

```yaml
plugins:
  - mkdocs-video:
      is_video: True
      video_controls: False
      ...
```

> The operation of this parameter may be affected by browser settings or video provider configuration

## Embedding examples

The following list contains some of the popular services, as well as examples of direct and embedded links to their videos.

* YouTube
    * https://www.youtube.com/watch?v=iSpglxHTJVM
    * https://www.youtube.com/embed/iSpglxHTJVM
* Vimeo
    * https://vimeo.com/224903454
    * https://player.vimeo.com/video/224903454
* Dailymotion
    * https://www.dailymotion.com/video/x7ogfqo
    * https://www.dailymotion.com/embed/video/x7ogfqo
* Facebook Watch
    * https://www.facebook.com/gamechangersmovie/videos/343098689705587
    * https://www.facebook.com/plugins/video.php?href=https://www.facebook.com/gamechangersmovie/videos/343098689705587

## Contributing

1.  Fork it.
2.  Create your feature branch:  `git checkout -b my-new-feature`
3.  Commit your changes:  `git commit -am 'Add some feature'`
4.  Push to the branch:  `git push origin my-new-feature`
5.  Submit a pull request

## License
The MIT License (MIT)

Copyright (c) 2023 Mikalai Lisitsa

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Did you like it?

<a href="https://www.buymeacoffee.com/soulless.viewer">
  <img height="50em" src="https://cdn.buymeacoffee.com/buttons/v2/default-blue.png" alt="soulless.viewer" />
</a>
