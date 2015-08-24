# Copyright (c) 2014 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import sys
import os
import re


def _AddToPathIfNeeded(path):
  print path
  if path not in sys.path:
    sys.path.insert(0, path)

def UpdateSysPathIfNeeded():
  p = GameProject()
  _AddToPathIfNeeded(p.vinn_path)

class GameProject():
  main_path = os.path.dirname(__file__)
  third_party_path = os.path.abspath(os.path.join(main_path, 'third_party'))
  vinn_path = os.path.abspath(os.path.join(third_party_path, 'vinn'))
  game_root_path = os.path.abspath(os.path.join(main_path, 'game'))

  def __init__(self):
    self.source_paths = []
    self.source_paths.append(self.game_root_path)
