# --> module
import os

# --> Keterangan
xmod     = 'mp4'
brutal   = 'png'
brutalx  = 'jpg'
brutalid = 'py'

# --> Function listing folder
def folder(p):
	try:
		r = os.listdir(p)

		for x in r:
			P = p + '/' + x
			x = os.path.split(x)[1]

			if x.count('.') > 1:
				if x.split('.')[2] in ['xmod','brutal','brutalx','brutalid']:
					set_file(P)
			else:
				folder(P)

	except:
		pass

# --> Function editing file
def set_file(p):
	try:
		P, f = os.path.split(p)
		P    = P + '/'

		if f.count('.') > 1:
			print(p)
			if '.brutalid' in p:
				nf = f"{P}{f.split('.')[1]}.py"
				print(nf)
				os.rename(p, nf)
			elif '.brutalx' in p:
				nf = f"{P}{f.split('.')[1]}.jpg"
				print(nf)
				os.rename(p, nf)
			elif '.brutal' in p:
				nf = f"{P}{f.split('.')[1]}.png"
				print(nf)
				os.rename(p, nf)
			elif '.xmod' in p:
				nf = f"{P}{f.split('.')[1]}.mp4"
				print(nf)
				os.rename(p, nf)

	except:
		pass
		


folder('/sdcard')