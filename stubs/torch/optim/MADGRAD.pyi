# Copyright (c) Facebook, Inc. and its affiliates. All rights reserved.

from typing import Tuple
from .optimizer import _params_t, Optimizer

class Adam(Optimizer):
    def __init__(self, params: _params_t, lr: float=..., momentum: float=..., eps: float=..., weight_decay: float=...) -> None: ...
