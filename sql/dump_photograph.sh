#!/bin/sh
MOD_DIR=photograph
MOD_PREFIX=photograph
DIR=/usr/local/OAKlouds/$MOD_DIR/mysql
cd $DIR
DB=ecm_1
rm -f *.sql

TABLE=`mysql $DB -e "show tables like \"$MOD_PREFIX%\""| grep ^$MOD_PREFIX |grep -v '[0-9]\{4\}m[0-9]\{2\}'`
mysqldump --compact --no-data $DB $TABLE > $MOD_DIR.sql

mysqldump --compact --no-create-info $DB phone_codelist >> $MOD_DIR.sql
perl -pi -e 's/ AUTO_INCREMENT=[0-9]*\b|CHARACTER SET utf8[ ]?//g' *.sql
perl -pi -e 's/CREATE TABLE/CREATE TABLE IF NOT EXISTS/g' *.sql
perl -pi -e 's|DEFAULT CHARSET=latin1|DEFAULT CHARSET=utf8|g' *.sql
perl -pi -e "s| COMMENT[ =]?'[^']+'||g" *.sql
perl -pi -e 's|^/\*.+\*/;$||g' *.sql

