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

	local output=$(kathara exec $machine -- nc -zv -w $timeout $target_ip $port 2>&1)

	if echo "$output" | grep -q "Connection refused"; then
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


n_ok=0
n_fail=0

echo "~~TESTING PCS~~"

echo "internet access:"
if test_internet "pcs" == "OK"; then n_ok += 1; else n_fail += 1

echo "mail access:"
if test_nc "pcs" "172.16.2.2" "4567" == "OK"; then n_ok += 1; else n_fail += 1

echo "intranet http access:"
if test_nc "pcs" "172.16.3.28" "80" == "OK"; then n_ok += 1; else n_fail += 1

echo "intranet https access:"
if test_nc "pcs" "172.16.3.28" "443" == "OK"; then n_ok += 1; else n_fail += 1

echo "S app access:"
if test_nc "pcs" "172.16.3.28" "1224" == "OK"; then n_ok += 1; else n_fail += 1

echo "can't ssh access to pcdsi:"
if test_nc "pcs" "172.16.2.5" "22" true == "OK"; then n_ok += 1; else n_fail += 1

echo "can't ping pcdsi:"
if test_ping "pcs" "172.16.2.5" true == "OK"; then n_ok += 1; else n_fail += 1



echo "~~TESTING PCDSI~~"

echo "internet access:"
if test_internet "pcdsi" == "OK"; then n_ok += 1; else n_fail += 1

echo "mail acces:"
if test_nc "pcdsi" "172.16.2.2" "4567" == "OK"; then n_ok += 1; else n_fail += 1

echo "intranet http access:"
if test_nc "pcdsi" "172.16.3.28" "80" == "OK"; then n_ok += 1; else n_fail += 1

echo "intranet https access:"
if test_nc "pcdsi" "172.16.3.28" "443" == "OK"; then n_ok += 1; else n_fail += 1

echo "S app access:"
if test_nc "pcdsi" "172.16.3.28" "1224" == "OK"; then n_ok += 1; else n_fail += 1

echo "ssh access to pcs:"
if test_nc "pcdsi" "172.16.20.1" "22" == "OK"; then n_ok += 1; else n_fail += 1



echo "~~TESTING S~~"

echo "bdd mysql access:"
if test_nc "s" "172.16.2.3" "3306" == "OK"; then n_ok += 1; else n_fail += 1

echo "can't ssh access to pcdsi"
if test_nc "s" "172.16.2.5" "22" true == "OK"; then n_ok += 1; else n_fail += 1

n_test = $n_ok + $n_fail
echo "$n_test tests: $n_ok passed, $n_fail failed"