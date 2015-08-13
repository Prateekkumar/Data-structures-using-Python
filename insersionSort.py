def insertionSort(sample):
	print "The initial sample of the array\n"
	print sample

	for x in range(1,len(sample)):
		y = x
		while ( y!= 0 and sample[y-1] > sample[y]):
			sample[y-1] , sample[y] = sample[y] , sample[y-1]
			y -= 1

	print "The sample after insersion sort"
	print sample


if __name__ == "__main__":
	a = [4,7,3,5,2,9,6]
	insertionSort(a)
