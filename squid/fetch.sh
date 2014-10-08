# !/bin/sh

ROOTDIR="/home/tianyin/conquid/app/squid-3.4.8/build/";

$ROOTDIR/bin/squidclient -h localhost -p 3128 $1 >$ROOTDIR/fetch.res

