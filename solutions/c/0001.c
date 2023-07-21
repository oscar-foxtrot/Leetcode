/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize)
{
    for (int i = 0; i < numsSize - 1; ++i)
        for (int j = i + 1; j < numsSize; ++j)
            if (nums[i] + nums[j] == target)
            {
                *returnSize = 2;
                int *returnv = malloc(sizeof(int) * 2);
                returnv[0] = i;
                returnv[1] = j;
                return returnv;
            }
    return NULL;
}
