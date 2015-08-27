# Copyright (c) 2014 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import sys
import os
import re


def _AddToPathIfNeeded(path):
  if path not in sys.path:
    sys.path.insert(0, path)

def UpdateSysPathIfNeeded():
  p = GameProject()
  _AddToPathIfNeeded(p.vinn_path)
  _AddToPathIfNeeded(os.path.join(p.third_party_path, 'WebOb'))
  _AddToPathIfNeeded(os.path.join(p.third_party_path, 'Paste'))
  _AddToPathIfNeeded(os.path.join(p.third_party_path, 'six'))
  _AddToPathIfNeeded(os.path.join(p.third_party_path, 'webapp2'))

class GameProject():
  main_path = os.path.dirname(__file__)
  third_party_path = os.path.abspath(os.path.join(main_path, 'third_party'))
  vinn_path = os.path.abspath(os.path.join(third_party_path, 'vinn'))
  polymer_path = os.path.abspath(os.path.join(third_party_path, 'polymer'))
  game_root_path = os.path.abspath(os.path.join(main_path, 'game'))

  def __init__(self):
    self.source_paths = [self.game_root_path, self.polymer_path]
