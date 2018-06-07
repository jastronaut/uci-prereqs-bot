# !/bin/sh
# run this to execute python bot
## --gen-prereqs

# TODO: get user to input department

dept="COMPSCI"

if [ "$1" == "--gen-prereqs" ]
then
	fname=$dept".json"
	if ls "$fname" >> /dev/null 2>&1
	then
		echo "$fname already exists!"
	else
		srcname="prereqspage"$dept".html"
		echo "creating $srcname"
		if ! ls "$srcname" >> /dev/null 2>&1
		then
			echo "going to run wget"
			dlurl="https://www.reg.uci.edu/cob/prrqcgi?dept="$dept"&term=201892&action=view_all"
			wget -q -O "$srcname" "$dlurl"
		fi
		python3 getprereqs.py $dept
		rm $srcname
		echo "Created $fname"
	fi
elif [ "$1" == "" ]
then
	python3 bot.py $dept
else
	echo "Invalid command."
fi