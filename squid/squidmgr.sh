# !/bin/sh

ROOTDIR="/home/tianyin/conquid/app/squid-3.4.8/build/";
LOGDIR=$ROOTDIR/var/logs

if [ "$1" = "start" ]; then
    rm -f $LOGDIR/access.log
    rm -f $LOGDIR/cache.log
    rm -Rf $ROOTDIR/var/cache/squid
    $ROOTDIR/sbin/squid -f $ROOTDIR/etc/squid.conf -d 1 -N >$ROOTDIR/stdout.log 2>$ROOTDIR/stderr.log &
    echo "Started..."

elif [ "$1" = "stop" ]; then
    $ROOTDIR/sbin/squid -k kill
    echo "Stoped..."
else
    echo "Wrong option!"
fi


