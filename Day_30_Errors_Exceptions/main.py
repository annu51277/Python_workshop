# try(Something that might cause an exception ) , except(Do this if there was an exception)
# # , else (Do this if there were NO exceptions ), finally ( Do this no matter what happens )
# try:
#     file = open('file1.txt')
#
# except Index as e:
#     print(f'{e}')
#     file = open('file.txt',mode='w')
#     file.write('Mohammad Rahamath Ansar')
#
# else:
#     data = file.read()
#     print(data)

facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

for key in facebook_posts:
 print(key['Likes'])