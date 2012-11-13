#!/usr/bin/python2.4
#
# Copyright 2010 Google Inc.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
#     * Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above
# copyright notice, this list of conditions and the following disclaimer
# in the documentation and/or other materials provided with the
# distribution.
#     * Neither the name of Google Inc. nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

"""Trivial replacements for Google-internal modules."""


# Ignore warnings about class names that look like module names.
# pylint: disable-msg=C6409
class iterlib(object):
  """Replacement for google3.pyglib.iterlib."""
  try:
    All = all  # available in python 2.5+
  except NameError:
    @staticmethod
    def All(iterable):
      for item in iterable:
        if not item:
          return False
      return True


class resources(object):
  """Replacement for google3.pyglib.resources."""

  @staticmethod
  def GetResource(f):
    return open(f).read()


class TestCaseHelpers(object):
  """Extra test helpers from Google test libraries / Python 2.7."""

  # Disable warnings about unittest method names.
  # pylint: disable-msg=C6409
  def assertIn(self, a, b, msg=None):
    if msg is None:
      msg = '"%s" not found in "%s"' % (a, b)
    self.assert_(a in b, msg)

  def assertNotIn(self, a, b, msg=None):
    if msg is None:
      msg = '"%s" unexpectedly found in "%s"' % (a, b)
    self.assert_(a not in b, msg)
