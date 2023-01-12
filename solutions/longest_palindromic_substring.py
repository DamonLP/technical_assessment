import sys

def longestPalindromicSubstring(s):
    result = s[0]
    result_len = 0

    # for palindromic with lengths are in odd number
    for i in range(1,len(s)):

        # Looking for palindromic starting with the middle character in index i
        # Starting from index = 1
        # left_index = 0
        # right_index = 2
        left_index = i-1
        right_index = i+1

        # if left_index and right_index are inbound
        # and substring, e.g. s[0:2], is a palindromic
        while left_index >=0 and right_index < len(s) and s[left_index] == s[right_index]:
            temp_len = right_index - left_index + 1

            # update result and result_len if length > result_len
            if temp_len > result_len:
                result_len = temp_len
                result = s[left_index:right_index+1]

            # set the left and right index to furter away from middle index
            left_index -= 1
            right_index += 1

    # for palindromic with lengths are in even number
    for i in range(len(s)):

        # Looking for palindromic starting with two consecutive character
        # Starting from index = 0
        # left_index = 0
        # right_index = 1
        left_index = i
        right_index = i+1

        # if left_index and right_index are inbound
        # and substring, e.g. s[0:1], is a palindromic
        while left_index >=0 and right_index < len(s) and s[left_index] == s[right_index]:
            temp_len = right_index - left_index + 1

            # update result and result_len if length > result_len
            if temp_len > result_len:
                result_len = temp_len
                result = s[left_index:right_index+1]

            # set the left and right index to furter away from middle index
            left_index -= 1
            right_index += 1

    return result

if len(sys.argv) > 1 and sys.argv[1]:
    print(longestPalindromicSubstring(sys.argv[1]))
else:
    print('Please provide string input, e.g. babbab')