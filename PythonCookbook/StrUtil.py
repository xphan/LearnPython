# -*- coding: utf-8 -*-

def isAString(anobj):
  return isinstance(anobj, basestring)

def containsAny(seq, aset):
  """ 检查序列seq是否含有aset中的项 """
  for c in seq:
    if c in aset: return True
  return False

def containsOnly(seq, aset):
  """检查序列是否仅仅含有aset中的项"""
  for c in seq:
    if c not in aset: return False
  return True

def containsAll(seq, aset):
  """检查序列是否包含全部aset中的项"""
  return not set(aset).difference(seq)

