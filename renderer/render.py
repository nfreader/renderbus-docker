#!/usr/bin/env python
import os, json, sys
from subprocess import call

json_files = [pos_json for pos_json in os.listdir('/usr/src/codebase/_maps') if pos_json.endswith('.json')]

maps = []
for j in json_files:
  maps.append(json.load(open('/usr/src/codebase/_maps/'+j)))

print(maps)

for map in maps:
  command = "/usr/src/spacemandmm/target/release/dmm-tools minimap --pngcrush -o /output {0}".format('_maps/'+map['map_path']+'/'+map['map_file'])
  call(command.split(), shell=False, cwd="/usr/src/codebase")