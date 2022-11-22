Copyright (c) 2022, Scientific Software Center, Heidelberg University

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---

The above code covers the Python code provided in this project itself. The
bundled stand-alone application offered on this project bundles many software
components. The combined work is distributed under the terms of the MIT license.
In the following you find a summary of bundled components, their licenses and
potential remarks. For easy readability we group by license and order them by
severity of implications on the overall legal situation.

---

Nvidia License Agreement for Nvidia SDKs (proprietary)

The NVidia Software License Agreement for the projects cublas, cuda-nvrtc and cuda-runtime can be found at https://docs.nvidia.com/cuda/eula/index.html. The SLA for cudnn is found at https://docs.nvidia.com/deeplearning/cudnn/sla/index.html.

The distribution includes shared libraries that are explicitly white-listed for distribution in the corresponding SLAs. They are obtained from the PyPI distribution of the Python packages nvidia-cublas-cu11, nvidia-cuda-nvrtc-cu11, nvidia-cuda-runtime-cu11, nvidia-cudnn-cu11

Currently, proprietary NVidia software is only included in the Linux distribution.

---

GNU Lesser General Public License v3

A copy of LGPL v3 is included into the distribution as LICENSE.LGPLv3.

* Name: FFmpeg
* Copyright: FFmpeg contributors
* URL: https://www.ffmpeg.org
* Remark: We distribute a statically linked ffmpeg executable that is provided by the
  FFmpeg-Builds project at https://github.com/BtbN/FFmpeg-Builds. We distribute the
  LGPL-only version of the executable. In order to change the version of ffmpeg used
  find the executable in the distribution folder and replace it with a version of your
  choice - the ffmpeg-python code base will interact with it using Python's subprocess
  module. This documents a technical requirement by the LGPLv3 license.

---

Mozilla Public License v2.0

A copy of the Mozilla Public License v2.0 is included into the distribution as LICENSE.MPLv2. The source code for these projects can be accessed from the given URLs.

* certifi
  * URL: https://github.com/certifi/python-certifi

* Parts of tqdm (other parts under MIT)
  * Copyright: 2015-2021 Casper da Costa-Luis
  * URL: https://github.com/tqdm/tqdm

---

Python Software Foundation License

A copy of the Python Software Foundation License is included into the distribution as LICENSE.PSF.

* typing-extensions
  * Copyright: 2001-2022 Python Software Foundation
  * URL: https://github.com/python/typing_extensions

---

Apache-2.0 License

A copy of the Apache-2.0 License is included into the distribution as LICENSE.Apache-v2.

* ffmpeg-python
  * Copyright: 2017 Karl Kroening
  * URL: https://github.com/kkroening/ffmpeg-python

* huggingface-hub
  * Copyright: huggingface developers
  * URL: https://github.com/huggingface/huggingface_hub

* regex
  * Copyright: 2020 Matthew Barnett
  * URL: https://github.com/mrabarnett/mrab-regex

* requests
  * Copyright: 2019 Kenneth Reitz
  * URL: https://github.com/psf/requests/

* tokenizers
  * Copyright: huggingface developers
  * URL: https://github.com/huggingface/tokenizers

* transformers
  * Copyright: huggingface developers
  * URL: https://github.com/huggingface/transformers

---

BSD-3 Clause License

A copy of the BSD-3 Clause License is included into the distribution as LICENSE.BSD-3. The conditions and disclaimer from the license text apply to all below projects.

* idna
  * Copyright: 2013-2022, Kim Davies and contributors
  * URL: https://github.com/kjd/idna

* numpy
  * Copyright: 2005-2022, NumPy Developers
  * URL: https://github.com/numpy/numpy

* torch
  * Copyright statement:
    Copyright (c) 2016-     Facebook, Inc            (Adam Paszke)
    Copyright (c) 2014-     Facebook, Inc            (Soumith Chintala)
    Copyright (c) 2011-2014 Idiap Research Institute (Ronan Collobert)
    Copyright (c) 2012-2014 Deepmind Technologies    (Koray Kavukcuoglu)
    Copyright (c) 2011-2012 NEC Laboratories America (Koray Kavukcuoglu)
    Copyright (c) 2011-2013 NYU                      (Clement Farabet)
    Copyright (c) 2006-2010 NEC Laboratories America (Ronan Collobert, Leon Bottou, Iain Melvin, Jason Weston)
    Copyright (c) 2006      Idiap Research Institute (Samy Bengio)
    Copyright (c) 2001-2004 Idiap Research Institute (Ronan Collobert, Samy Bengio, Johnny Mariethoz)
    From Caffe2:
    Copyright (c) 2016-present, Facebook Inc. All rights reserved.
    All contributions by Facebook:
    Copyright (c) 2016 Facebook Inc.
    All contributions by Google:
    Copyright (c) 2015 Google Inc.
    All rights reserved.
    All contributions by Yangqing Jia:
    Copyright (c) 2015 Yangqing Jia
    All rights reserved.
    All contributions by Kakao Brain:
    Copyright 2019-2020 Kakao Brain
    All contributions by Cruise LLC:
    Copyright (c) 2022 Cruise LLC.
    All rights reserved.
    All contributions from Caffe:
    Copyright(c) 2013, 2014, 2015, the respective contributors
    All rights reserved.
    All other contributions:
    Copyright(c) 2015, 2016 the respective contributors
    All rights reserved.
    Caffe2 uses a copyright model similar to Caffe: each contributor holds
    copyright over their contributions to Caffe2. The project versioning records
    all such contribution and copyright details. If a contributor wants to further
    mark their specific copyright on a particular contribution, they should
    indicate their copyright solely in the commit message of the change when it is
    committed.
  * Remarks: Specifically, the names of Facebook, Deepmind Technologies, NYU,
    NEC Laboratories America and IDIAP Research Institute may not be used
    to endorse of promote products derived from this software without specific
    prior written permission.
  * URL: https://github.com/pytorch/pytorch

---

BSD-2 Clause License

A copy of the BSD-2 Clause License is included into the distribution as LICENSE.BSD-2. The conditions and disclaimer from the license text apply to all below projects.

* packaging
  * Copyright: Donald Stufft and individual contributors
  * URL: https://github.com/pypa/packaging

---

MIT License

A copy of the MIT License is included into the distribution as LICENSE.MIT.

* charset-normalizer
  * Copyright: 2019 TAHRI Ahmed R.
  * URL: https://github.com/Ousret/charset_normalizer

* future
  * Copyright: 2013-2019 Python Charmers Pty Ltd, Australia
  * URL: https://github.com/PythonCharmers/python-future

* more-itertools
  * Copyright: 2012 Erik Rose
  * URL: https://github.com/more-itertools/more-itertools

* pyparsing
  * Copyright: 2003-2022  Paul T. McGuire
  * URL: https://github.com/pyparsing/pyparsing

* pyyaml
  * Copyright: 2017-2021 Ingy döt Net, 2006-2016 Kirill Simonov
  * URL: https://github.com/yaml/pyyaml

* setuptools
  * Copyright: Jason R. Coombs
  * URL: https://github.com/pypa/setuptools

* Parts of tqdm (other parts under MPLv2)
  * Copyright: 2013 Noam Yorav-Raphael, 2016 on behalf of Google Inc.
  * URL: https://github.com/tqdm/tqdm

* urllib3
  * Copyright: 2008-2020 Andrey Petrov and contributors
  * URL: https://github.com/urllib3/urllib3

* wheel
  * Copyright: 2012 Daniel Holth and contributors
  * URL: https://github.com/pypa/wheel

* whisper
  * Copyright: 2022 OpenAI
  * URL: https://github.com/openai/whisper

---

The Unlicense

* filelock
  * URL: https://github.com/tox-dev/py-filelock
