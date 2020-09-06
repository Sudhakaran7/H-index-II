class Solution(object):
    def hIndex(self, citations):
        """ :type citations: List[int] :rtype: int """
        start, end = 1, len(citations)
        while start <= end:
            h = int((start+end)/2)
            if citations[len(citations)-h] < h: 
                end = h-1
            elif len(citations)-h-1>=0 and citations[len(citations)-h-1] > h:
                start = h+1
            else:
                return h
        return 0

if __name__ == '__main__':
    s = Solution()
    n=int(input())
    array = list(map(int,input().split()))
    array.sort()
    print(s.hIndex(array))
