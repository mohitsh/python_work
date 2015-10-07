
#include <iostream>
#include <vector>
using namespace std;

long taum(vector<long> arr1, vector<long> arr2)
{
	long b = arr1[0];
	long w = arr1[1];
	long x = arr2[0];
	long y = arr2[1];
	long z = arr2[2];
	long init_sum = b*x + w*y;
	for (long i = 1; i<=b; i++)
	{
		long new_sum = (b-i)*x + (w+i)*y + i*z;
		if (new_sum < init_sum)
			init_sum = new_sum;
	}
	for (long i = 1; i<=w; i++)
	{
		long new_sum = (b+i)*x + (w-i)*y + i*z;
		if (new_sum < init_sum)
			init_sum = new_sum;
	}
	return init_sum;
}

int main()
{

	long t;
	cin >> t;
	for (long i = 0; i<t; i++)
	{
		vector<long> v1;
		long a,b,c,d,e;
		cin >> a >> b;
		v1.push_back(a);
		v1.push_back(b);
		vector<long> v2;
		cin >> c >> d >> e;
		v2.push_back(c);
		v2.push_back(d);
		v2.push_back(e);
		long ans;
		ans = taum(v1,v2);
		cout.setf(ios::fixed);
		cout << ans << endl;
	}
}
	


