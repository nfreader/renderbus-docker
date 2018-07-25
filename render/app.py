#!/usr/bin/env python
import os, json, sys
from subprocess import call

json_files = [pos_json for pos_json in os.listdir('/usr/src/codebase/_maps') if pos_json.endswith('.json')]

maps = []
for j in json_files:
  maps.append(json.load(open('/usr/src/codebase/_maps/'+j)))

print(maps)

with open('/output/maps.json', 'w') as outfile:
  json.dump(maps, outfile)

for map in maps:
  command = "/usr/src/spacemandmm/target/release/dmm-tools minimap -o /tmp {0}".format('_maps/'+map['map_path']+'/'+map['map_file'])
  call(command.split(), shell=False, cwd="/usr/src/codebase")

  crushcmd = "pngcrush -q /tmp/{0}-1.png /output/{0}-1.png ".format(map['map_file'].replace('.dmm',''))
  call(crushcmd.split(), shell=False, cwd="/usr/src/codebase")

  tilecommand = "./tile.sh /output/{0}-1.png {1} 256 5 /output".format(map['map_file'].replace('.dmm',''),map['map_name'].replace(' ',''))

  print("Tiling {0}...".format(map['map_name']))
  call(tilecommand.split(), shell=False, cwd="/usr/src/render")

