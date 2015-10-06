#include <iostream>
#include <vector>
#include <math.h>

using namespace std;

int dude (int x, int y)
{

	int count = 0;
	for (int i = x; i<=y; i++)
	{
		double original = sqrt(i);
		double deformed = floor(original);
		
		if (original == deformed)
			count++;
	}
	return count;

}

int main()
{

	vector<int> v1;
	int t;
	cin >> t;
	for (int i = 0; i<t; i++)
	{
			int x;
			int y;
			cin >> x >> y;
			int ans;
			ans = dude(x,y);
			cout << ans << endl;
		


}
return 0;
}
