int search(int* nums, int numsSize, int target) {
    int first = 0; int last = numsSize - 1;
    int mid = (last + first) / 2;
    
    while (first <= last) {
        if (nums[mid] == target) {
            return mid;
        } else if (nums[mid] < target) {
            first = mid + 1;
        } else if (nums[mid] > target) {
            last = mid - 1;
        }
        mid = (last + first) / 2;
    }
    return -1;
}
