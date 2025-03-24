test_ping() {
	local machine=$1
	local target_ip=$2
	local reverse=${3:-false}
	local max_ping=${4:-1}

	if kathara exec $machine -- ping -c $max_ping $target_ip >/dev/null 2>&1; then
		if $reverse; then echo "FAIL"; else echo "OK"; fi
	else
		if $reverse; then echo "OK"; else echo "FAIL"; fi
	fi
}

test_nc() {
	local machine=$1
	local target_ip=$2
	local port=$3
	local reverse=${4:-false}
	local timeout=${5:-1}

	if kathara exec $machine -- nc -z -w $timeout $target_ip $port >/dev/null 2>&1; then
		if $reverse; then echo "FAIL"; else echo "OK"; fi
	else
		if $reverse; then echo "OK"; else echo "FAIL"; fi
	fi
}
 
test_internet() {
	local machine=$1
	local reverse=${2:-false}

	if kathara exec $machine -- curl -s --max-time 3 https://1.1.1.1 >/dev/null 2>&1; then
		if $reverse; then echo "FAIL"; else echo "OK"; fi
	else
		if $reverse; then echo "OK"; else echo "FAIL"; fi
	fi
}




echo "~~TESTING PCS~~"

echo "internet access:"
test_internet "pcs"

echo "mail access:"
test_nc "pcs" "172.16.2.2" "4567"

echo "intranet http access:"
test_nc "pcs" "172.16.3.28" "80"

echo "intranet https access:"
test_nc "pcs" "172.16.3.28" "443" 

echo "S app access:"
test_nc "pcs" "172.16.3.28" "1224"

echo "can't ssh access to pcdsi:"
test_nc "pcs" "172.16.2.5" "22" true

echo "can't ping pcdsi:"
test_ping "pcs" "172.16.2.5" true



echo "~~TESTING PCDSI~~"

echo "internet access:"
test_internet "pcdsi"

echo "mail acces:"
test_nc "pcdsi" "172.16.2.2" "4567"

echo "intranet http access:"
test_nc "pcdsi" "172.16.3.28" "80"

echo "intranet https access:"
test_nc "pcdsi" "172.16.3.28" "443" 

echo "S app access:"
test_nc "pcdsi" "172.16.3.28" "1224"

echo "can't bdd sftp access:"
test_nc "pcdsi" "172.16.2.3" "22" true

echo "ssh access to pcs:"
test_nc "pcdsi" "172.16.20.1" "22"



echo "~~TESTING S~~"

echo "internet access:"
test_internet "s"

echo "bdd mysql access:"
test_nc "s" "172.16.3" "3306"

echo "can't ssh access to pcdsi"
test_nc "s" "172.16.2.5" "22" true