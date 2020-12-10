for i in $(ls)

do
	RID=$(echo "$i" | cut -c 23-26)
	date=$(echo "i" | cut -c 28-35)