# Analyzes the election data

import sys

sys.path.insert(1, '../Common')
import common

def AnalyzeData(data):

    # get the total number of votes
    total_number_of_votes = len(data)

    candidates = []
    for vote in data:
        # get the candidate
        candidate = vote['candidate']

        # determine if candidate is already in the list
        candidateMatch = next((sub for sub in candidates if sub['candidate'] == candidate), None)
        if (candidateMatch == None):
            candidateMatch = {
                'candidate': candidate,
                'number_of_votes': 0
            }
            candidates.append(candidateMatch)

        # increment the candidates total number of votes
        candidateMatch['number_of_votes'] += 1

    # set each candidates percentage
    winningCandidate = None
    for candidate in candidates:
        candidate['vote_percentage'] = candidate['number_of_votes'] / total_number_of_votes
        if winningCandidate == None or candidate['number_of_votes'] > winningCandidate['number_of_votes']:
            winningCandidate = candidate



    analysis = {
        'total_votes':total_number_of_votes,
        'candidates':candidates,
        'winningCandidate':winningCandidate
    }
    return analysis