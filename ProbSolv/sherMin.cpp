#include<iostream>
#include<vector>
#include<algorithm>
#include<cmath>
using namespace std;
long long sher_min(vector <long long> arr,int n,int p,int q)
{
	vector<long long> vec1;
	vector<long long> cool;

	for (int i = p; i<=q; ++i)
	{
		vector<long long> vec2;
		for (int j = 0; j<n; ++j)
		{
			vec2.push_back(abs(arr[j]-i));
		}
		cool.push_back(*min_element(vec2.begin(), vec2.end()));
		vec1.push_back(i);
	}
	long long dude = *max_element(cool.begin(),cool.end());
	long long index = distance(cool.begin(), find(cool.begin(),cool.end(),dude));
	return vec1[index];
}


int main()
{

	int n;
	cin >> n;
	//cout << endl;
	vector<long long> v;
	for (int i = 0; i<n; ++i)
	{
		long long dude;
		cin >> dude;
		v.push_back(dude);
	}
	vector<int>::iterator it;
	/*
	for (it = v.begin(); it<v.end(); ++it)
	{
		cout << *it << " ";
	}
	
	cout << endl;
	*/
	long long p,q;
	cin >> p >> q;
	//cout << p << endl;
	//cout << q << endl;
	cout << sher_min(v,n,p,q) << endl;
}
