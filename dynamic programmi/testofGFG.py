# Python3 program for
# the above approach

# Function to calculate the total
# number of ways to have sum N
def findWays(N):

	# Initialize dp array
	dp = [0] * (N + 1);
	dp[0] = 1;

	# Iterate over all the
	# possible intermediate
	# values to reach N
	for i in range(1, N + 1):
		dp[i] = 0;

		# Calculate the sum for
		# all 6 faces
		for j in range(1, 7):
			if (i - j >= 0):
				dp[i] = dp[i] + dp[i - j];

	# Print total number of ways
	print(dp[N]);

N = int(input())

findWays(N);

# This code is contributed by 29AjayKumar
