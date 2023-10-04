import qrcode as qr

myqr = qr.make("My Programming Profiles link :: \n\nhttps://auth.geeksforgeeks.org/user/101rror\nhttps://leetcode.com/101rror/\nhttps://codeforces.com/profile/101rror\nhttps://github.com/101rror")

myqr.save("Myself.png")
