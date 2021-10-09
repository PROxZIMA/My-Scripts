#!/bin/bash
LINK=$1
BRANCH="trunk"

REPO=${LINK%%/tree/*}
BASE=${LINK#*tree/}

IFS='/' read -r CURRBRANCH FOLDER <<< $BASE

if [[ $CURRBRANCH != "master" ]]; then
  BRANCH="branches/"$CURRBRANCH
fi

echo Exporting $REPO/$BRANCH/$FOLDER
svn export $REPO/$BRANCH/$FOLDER

