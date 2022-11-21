# OpenAI Whisper standalone distribution

** This is still under construction**

This is a stand-alone application that packages [OpenAI's Whisper](https://github.com/openai/whisper) into one
executable file. Additionally, it provides a minimalistic graphical user interface for transcription.

## Installation

Please choose and download the standalone application for your operating system from the Releases section.

## Usage

Running the `whisper` standalone executable without any arguments will fire up the graphical user interface.

If you want to work with `whisper`'s command line interface instead, you can do so by providing arguments:

```
whisper --help
```

## Licensing

The code provided in this project itself is covered by [the MIT license](LICENSE.md).

The stand-alone executable bundles the following projects in binary form.
The resulting combined work is also licensed under the MIT License.

* [certifi](https://github.com/certifi/python-certifi), MPL v2 License, [Copyright Notice](https://github.com/certifi/python-certifi/blob/master/LICENSE)
* [charset-normalizer](https://github.com/Ousret/charset_normalizer), MIT License, [Copyright Notice](https://github.com/Ousret/charset_normalizer/blob/master/LICENSE)
* [ffmpeg-python](https://github.com/kkroening/ffmpeg-python), Apache-2.0 License, [Copyright Notice](https://github.com/kkroening/ffmpeg-python/blob/master/LICENSE)
* [filelock](https://github.com/tox-dev/py-filelock), Unlicense License, [Copyright Notice](https://github.com/tox-dev/py-filelock/blob/main/LICENSE)
* [future](https://github.com/PythonCharmers/python-future), MIT License, [Copyright Notice](https://github.com/PythonCharmers/python-future/blob/master/LICENSE.txt)
* [huggingface-hub](https://github.com/huggingface/huggingface_hub), Apache-2.0 License , [Copyright Notice](https://github.com/huggingface/huggingface_hub/blob/main/LICENSE)
* [idna](https://github.com/kjd/idna), BSD-3-Clause License, [Copyright Notice](https://github.com/kjd/idna/blob/master/LICENSE.md)
* [more-itertools](https://github.com/more-itertools/more-itertools), MIT License , [Copyright Notice](https://github.com/more-itertools/more-itertools/blob/master/LICENSE)
* [numpy](https://github.com/numpy/numpy), BSD-3-Clause License, [Copyright Notice](https://github.com/numpy/numpy/blob/main/LICENSE.txt), [Bundled Dependency Licenses](https://github.com/numpy/numpy/blob/main/LICENSES_bundled.txt)
* [nvidia-cublas-cu11](), Nvidia License Agreement for Nvidia SDKs (proprietary) , [Software License Agreement](https://docs.nvidia.com/cuda/eula/index.html)
* [nvidia-cuda-nvrtc-cu11](), Nvidia License Agreement for Nvidia SDKs (proprietary) , [Software License Agreement](https://docs.nvidia.com/cuda/eula/index.html)
* [nvidia-cuda-runtime-cu11](), Nvidia License Agreement for Nvidia SDKs (proprietary) , [Software License Agreement](https://docs.nvidia.com/cuda/eula/index.html)
* [nvidia-cudnn-cu11](), Nvidia License Agreement for Nvidia SDKs (proprietary), [Software License Agreement](https://docs.nvidia.com/deeplearning/cudnn/sla/index.html)
* [packaging](https://github.com/pypa/packaging), BSD-2-Clause License, [Copyright Notice](https://github.com/pypa/packaging/blob/main/LICENSE.BSD)
* [pyparsing](https://github.com/pyparsing/pyparsing), MIT License, [Copyright Notice](https://github.com/pyparsing/pyparsing/blob/master/LICENSE)
* [pyyaml](https://github.com/yaml/pyyaml), MIT License, [Copyright Notice](https://github.com/yaml/pyyaml/blob/master/LICENSE)
* [regex](https://github.com/mrabarnett/mrab-regex), Apache-2.0 License, [Copyright Notice](https://github.com/mrabarnett/mrab-regex/blob/hg/LICENSE.txt)
* [requests](https://github.com/psf/requests), Apache-2.0 License, [Copyright Notice](https://github.com/psf/requests/blob/main/LICENSE)
* [setuptools](https://github.com/pypa/setuptools), MIT License, [Copyright Notice](https://github.com/pypa/setuptools/blob/main/LICENSE)
* [tokenizers](https://github.com/huggingface/tokenizers), Apache-2.0 License, [Copyright Notice](https://github.com/huggingface/tokenizers/blob/main/LICENSE)
* [torch](https://github.com/pytorch/pytorch), BSD-3 Clause License, [Copyright Notice](https://github.com/pytorch/pytorch/blob/master/LICENSE)
* [tqdm](https://github.com/tqdm/tqdm), MPL + MIT License, [Copyright Notice](https://github.com/tqdm/tqdm/blob/master/LICENCE)
* [transformers](https://github.com/huggingface/transformers), Apache-2.0 License, [Copyright Notice](https://github.com/huggingface/transformers/blob/main/LICENSE)
* [typing-extensions](https://github.com/python/typing_extensions), Python Software Foundation License, [Copyright Notice](https://github.com/python/typing_extensions/blob/main/LICENSE)
* [urllib3](https://github.com/urllib3/urllib3), MIT License, [Copyright Notice](https://github.com/urllib3/urllib3/blob/main/LICENSE.txt)
* [wheel](https://github.com/pypa/wheel), MIT License, [Copyright Notice](https://github.com/pypa/wheel/blob/main/LICENSE.txt)
* [whisper](https://github.com/openai/whisper), MIT License, [Copyright Notice](https://github.com/openai/whisper/blob/main/LICENSE)
