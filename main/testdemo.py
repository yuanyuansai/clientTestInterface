#
# headers = {
#             "cookie": "Path=/; Path=/; Path=/",
#             "content-type": "application/json"
#         }
# headers['a'] = 1
# print(headers)
# print(type(headers))


a='rememberMe=deleteMe; Path=/; Max-Age=0; Expires=Wed, 01-Dec-2021 09:25:17 GMT, SESSION=YjAxNTA5N2YtMGVlZC00MGFhLWI5YzYtM2I3MjYwNWMyNjBi; Path=/; HttpOnly; SameSite=Lax, Path=/; HttpOnly; Secure'
b=a[a.index('SESSION'):]
print(b)






