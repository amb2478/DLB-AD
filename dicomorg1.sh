#!/bin/bash
for i in $(ls *.json)

do 
# This is parsing each .json file
	MPRAGE=$(cat "$i" | grep "SeriesDescription" | awk '/RAGE",/')
	SPGR=$(cat "$i" | grep "SeriesDescription" | awk '/SPGR",/')
	other=$(cat "$i" | grep "SeriesDescription" | awk -F':' '{print $2}' | awk -F',' '{print $1}')
	echo "$other"

	# Is the file an MPRAGE OR SPGR? Then the following runs
	if [[ "$MPRAGE""$SPGR" ]];

	then
		#Everything here will be only on the .json that contain MPRAGE/SPGR scans
		nifti_name=$(echo "$i" | sed 's/json/nii/g')
		subject_ID=$(echo "$i" | cut -c 1-10)
		year=$(echo "$i" | cut -c 12-15)
		month=$(echo "$i" | cut -c 16-17)
		day=$(echo "$i" | cut -c 18-19)
		# This if tests to see if a file exists, if it does then it's the 2nd to the nth scan, if it doesn't it's the 1st
		if [[ -f "$subject_ID"_mris.txt ]]; # does mristxt exist
			then
				firstvisityear=$(echo `head -1 "$subject_ID"_mris.txt | awk -F',' '{print $3}'` | cut -c 3-4)
				#echo $firstvisityear
				firstvisitmonth=$(echo `head -1 "$subject_ID"_mris.txt | awk -F',' '{print $4}'`)
				firstvisitday=$(echo `head -1 "$subject_ID"_mris.txt | awk -F',' '{print $5}'`)
				firstvisitdate="$firstvisityear""$firstvisitmonth""$firstvisitday"
				#baseline=$(echo "$firstline" | cut -c 14-19)
				currentdate=$(echo "$i" | cut -c 14-19)
				duration=$(echo "$i" | echo $(( ($(date --date="$currentdate" +%s) - $(date --date="$firstvisitdate" +%s) )/(60*60*24) )))
				#echo "============================="
				#echo "$currentdate"
				#echo "$firstvisitdate"
				echo "$nifti_name","$other","$year","$month","$day","$duration" >> "$subject_ID"_mris.txt

			else #this is the fist
				#echo "$nifti_name","${other:1: -1}","$year","$month","$day", 0 >> "$subject_ID"_mris.txt
				# echo 0
				# firstvisityear=$(echo `head -1 "$subject_ID"_mris.txt | awk -F',' '{print $3}'` | cut -c 3-4)
				# firstvisitmonth=$(echo `head -1 "$subject_ID"_mris.txt | awk -F',' '{print $4}'`)
				# firstvisitday=$(echo `head -1 "$subject_ID"_mris.txt | awk -F',' '{print $5}'`)
				# firstvisitdate="$firstvisityear""$firstvistmonth""$firstvisitday"
				# currentdate=$(echo "$i" | cut -c 14-19)
				# #duration=$(echo "$i" | echo $(( ($(date --date="$currentdate" +%s) - $(date --date="$firstvisitdate" +%s) )/(60*60*24) )))
				# echo "$currentdate"
				echo "$nifti_name","$other","$year","$month","$day",0 >> "$subject_ID"_mris.txt
		fi

	#echo "$nifti_name","${other:1: -1}","$year","$month","$day" >> "$subject_ID"_mris.txt


	# elif [[ $SPGR ]];

	# then
	# nifti_name=$(echo "$i" | sed 's/json/nii/g')
	# subject_ID=$(echo "$i" | cut -c 1-10)
	# year=$(echo "$i" | cut -c 12-15)
	# month=$(echo "$i" | cut -c 16-17)
	# day=$(echo "$i" | cut -c 18-19)

	# if [[ -z "$subject_ID"_mris.txt ]];
	# then
	# firstline=$(read [-i text])
	# baseline=$(echo "$firstline" | cut -c 14-19)
	# date=$(echo "$i" | cut -c 14-19)
	# duration=$(echo "$i" | echo $(( ($(date --date="$date" +%s) - $(date --date="$baseline" +%s) )/(60*60*24) )))
	# echo "$nifti_name","${other:1: -1}","$year","$month","$day","$duration" >> "$subject_ID"_mris.txt

	# else
	# echo "$nifti_name","${other:1: -1}","$year","$month","$day", 0 >> "$subject_ID"_mris.txt

	# #echo "$nifti_name","${other:1: -1}","$year","$month","$day" >> "$subject_ID"_mris.txt


	fi
done
