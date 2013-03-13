# -*- coding: utf-8 -*-

def read_file_by_chunks(filename, chunksize=100):
  file_object = open(filename, 'rb')
  while True:
    chunk = file_object.read(chunksize)
    if not chunk:
      break
  yield chunk
  file_object.close()

def getline(thefilepath, desired_line_number):
  if desired_line_number < 1: return ''
  for current_line_number, line in enumerate(open(thefilepath, 'rU')):
    if current_line_number == desired_line_number - 1 : return line
  return ''

