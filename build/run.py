#!/usr/bin/env python
# Copyright (c) 2015 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import argparse
import os
import sys

import game_project
import vinn


def _RelPathToUnixPath(p):
  return p.replace(os.sep, '/')


def RunTests():
  project = game_project.GameProject()
  cmd = """
  loadHTML('/game.html');
  """
  res = vinn.RunJsString(
    cmd, source_paths=list([project.source_path]),
    js_args=[], stdout=sys.stdout, stdin=sys.stdin)
  return res.returncode

def Main(argv):
  parser = argparse.ArgumentParser(description='Run game JS.')
  args = parser.parse_args(argv[1:])

  sys.exit(RunTests())
