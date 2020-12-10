mkdir baseline

for i in $(ls *_mris.txt); do
	cat "$i"
	subject_ID=$(echo "$i" | cut -c 1-10)
	baseline=$(echo `head -1 "$subject_ID"_mris.txt | awk -F',' '{print $1}'`)
	new_name=$(echo "$baseline" | cut -c 1-19)
	cp "$baseline" ~/lbd_complete/baseline/"$new_name"".nii"
done