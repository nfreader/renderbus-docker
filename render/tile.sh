#!/bin/bash

FULLMAP=$1
MAPNAME=$2
TILESIZE=$3
ZOOM=$4

MAPSIZE=`identify -format "%w" $FULLMAP`
DESTDIR=$5

#Run the first tile pass on the main map size WITHOUT resizing
CROP="$TILESIZE"
CROP+="x$TILESIZE"

mkdir -p $DESTDIR/tiles/$MAPNAME/$ZOOM
convert $FULLMAP -crop $CROP +gravity -set filename:tile $DESTDIR/tiles/$MAPNAME/$ZOOM/tile_%[fx:page.x/$TILESIZE]-%[fx:page.y/$TILESIZE] %[filename:tile].png

ZOOM=$[$ZOOM-1] #Since we're not resizing the first iteration, we skip a zoom level

while [ $ZOOM -gt 0 ]
do
  MAPSIZE=$[$MAPSIZE/2]
  RESIZE="$MAPSIZE"
  RESIZE+="x$MAPSIZE"
  mkdir -p $DESTDIR/tiles/$MAPNAME/$ZOOM
  convert $FULLMAP -resize $RESIZE -crop $CROP +gravity -set filename:tile $DESTDIR/tiles/$MAPNAME/$ZOOM/tile_%[fx:page.x/$TILESIZE]-%[fx:page.y/$TILESIZE] %[filename:tile].png

ZOOM=$[$ZOOM-1]
done
