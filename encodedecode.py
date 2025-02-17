"""weird-ass question with weird-ass solution"""




# def encode(strs):
#     encoded_lst = []
#     for text in strs:
#         modified_text = f"{len(text)}#{text}"
#         encoded_lst.append(modified_text)
#
#     encoded = ''.join(encoded_lst)
#     return encoded
#
#
# a=encode(["neet", "code", "love", "you"]
#              )
# def decode(strs):
#     i=0
#     decoded=[]
#     while i < len(strs):
#         j=i
#         while strs[j]!="#":
#             j+=1
#
#         length=int(strs[i:j])
#
#         text=strs[j+1:j+length+1]
#         decoded.append(text)
#
#         i=j+1+length
#
#     return decoded
