from scipy import spatial

def similarity_score (phone, watch):
	scores = [1 - spatial.distance.cosine(phone['x'], watch['x']),
			  1 - spatial.distance.cosine(phone['y'], watch['y']),
			  1 - spatial.distance.cosine(phone['z'], watch['z'])]
	return scores

def similarity_score_1D (phone, watch):
	scores = [1 - spatial.distance.cosine(phone, watch)]
	#print "SCORES: X Y Z", scores
	#print "MEAN :", np.mean(scores)

	return scores	