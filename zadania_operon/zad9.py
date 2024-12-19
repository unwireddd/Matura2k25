# Function to find the length of the longest
# AP in the array
def znajdzCiag(arr):
    n = len(arr)

    # If there are less than 3 elements,
    # return the size
    if n <= 2:
        return n

    # Create a list of dictionaries to store
    # lengths of APs
    dp = [{} for _ in range(n)]

    max_length = 0
    end = 0
    difference = 0

    # Iterate through all pairs of elements as
    # possible first two terms
    for i in range(1, n):
        for j in range(i):
            # Calculate the common difference
            diff = arr[i] - arr[j]

            # Get the previous length or start with 1
            length = dp[j].get(diff, 1)

            # Update the length of the AP ending at index `i`
            dp[i][diff] = length + 1

            # Update the global maximum length
            if dp[i][diff] > max_length:
                end = i
                difference = diff
                max_length = dp[i][diff]

    print(f"{max_length} :", end='')
    for n in reversed(range(max_length)):
        print(f" {arr[end] - n * difference}", end='')
    print("")


tab1 = [1, 3, 4, 5, 6, 7, 9, 10, 11]
znajdzCiag(tab1)

tab2 = [4, 7, 9, 11, 14, 16, 19, 20, 22, 24, 27, 29]
znajdzCiag(tab2)

tab3 = [2, 3, 4, 6, 7,  8, 9, 11, 12, 13, 15]
znajdzCiag(tab3)
