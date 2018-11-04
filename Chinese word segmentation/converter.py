if __name__ == '__main__':
	"""
	convert dos linefeeds (crlf) to unix (lf)
	usage: dos2unix.py 
	"""
	originals = ["prob_emit.p", "prob_start.p", "prob_trans.p"]
	destinations = ["prob_emit_unix.p", "prob_start_unix.p", "prob_trans_unix.p"]
	
	for original, destination in zip(originals, destinations):
		content = ''
		outsize = 0
		with open(original, 'rb') as infile:
			content = infile.read()
		with open(destination, 'wb') as output:
			for line in content.splitlines():
				outsize += len(line) + 1
				output.write(line + str.encode('\n'))
		print("Done. Saved %s bytes." % (len(content)-outsize))
