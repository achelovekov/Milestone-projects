import numpy as np

distance = lambda p1,p2: ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5
sorted_x = lambda A: sorted(A)
sorted_y = lambda A: sorted(A, key = lambda index: index[::-1])


def bruteforce(P):
	if len(P) < 2:
		return 0, P[0], P[0]

	dist = np.inf
	p1, p2 = None, None

	for i in range(len(P) - 1):
		for j in range(i + 1, len(P)):
			tmp_dist = distance(P[i], P[j])
			if tmp_dist < dist:
				dist = tmp_dist
				p1, p2 = P[i], P[j]

	return dist, p1, p2

def split(X, Y):
	m = (len(X) - 1) // 2
	XL = X[:m + 1]
	XR = X[m + 1:]
	YL = sorted_y(XL)
	YR = sorted_y(XR)
	
	return XL, XR, YL, YR

def closest_pair(X, Y):
	if len(X) < 4:
		return bruteforce(X)

	XL, XR, YL, YR = split(X, Y)
	dL, pL1, pL2 = closest_pair(XL, YL)
	dR, pR1, pR2 = closest_pair(XR, YR)

	if dL < dR:
		p1, p2 = pL1, pL2
	else:
		p1, p2 = pR1, pR2

	delta = min(dL, dR)

	for i in range(len(Y) - 1):
		for j in range(i + 1, min(len(Y), i + 8)):
			if distance(Y[i], Y[j]) < delta:
				delta = distance(Y[i], Y[j])
				p1, p2 = Y[i], Y[j]

	return delta, p1, p2


if __name__ == '__main__':
	P = [(1,1),(3,4),(2,4),(2,8),(10,13),(9,2),(4,1),(6,1)]
	X, Y = sorted_x(P), sorted_y(P)
	print(closest_pair(X, Y))