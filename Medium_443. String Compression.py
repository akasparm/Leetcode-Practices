# class Solution:
#     def compress(self, chars: List[str]) -> int:
#         i = 1
#         if len(chars)==1:
#             return 2
#         instances = 1
#         while i < len(chars):
#             if chars[i] == chars[i-1]:
#                 instances += 1
#                 print(str(instances))
#                 chars.pop(i)
#             else:
#                 if not instances == 1:
#                     chars.insert(i, str(instances))
#                 i+=2
#                 instances = 1
                
#         chars.append(str(instances))


############# From Solutions #############

class Solution:
    def compress(self, chars: List[str]) -> int:
        s = []
        for key, group in groupby(chars):
            print("key: ", key, "group: ", group)
            #print(k, list(g))
            count = len(list(group))
            print("count: ", count)
            s.append(key)
            if count > 1: s.extend(list(str(count)))
        chars[:] = s