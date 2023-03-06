import random
def sequence_alignment(seq1, seq2, match=3, mismatch=-1, gap_open=-1, gap_extend=-0.5):
    # Initialize the scoring matrix
    rows = len(seq1) + 1
    cols = len(seq2) + 1
    score_matrix = [[0 for j in range(cols)] for i in range(rows)]

    # Initialize the traceback matrix
    traceback_matrix = [[0 for j in range(cols)] for i in range(rows)]

    # Fill in the scoring and traceback matrices
    for i in range(1, rows):
        for j in range(1, cols):
            # Calculate the scores for each possible alignment
            match_score = score_matrix[i-1][j-1] + (match if seq1[i-1] == seq2[j-1] else mismatch)
            delete_score = score_matrix[i-1][j] + gap_open + gap_extend
            insert_score = score_matrix[i][j-1] + gap_open + gap_extend

            # Choose the highest score
            score_matrix[i][j] = max(match_score, delete_score, insert_score)

            # Set the traceback value
            if score_matrix[i][j] == match_score:
                traceback_matrix[i][j] = (i-1, j-1)
            elif score_matrix[i][j] == delete_score:
                traceback_matrix[i][j] = (i-1, j)
            elif score_matrix[i][j] == insert_score:
                traceback_matrix[i][j] = (i, j-1)

    # Traceback to find the optimal alignment
    align1 = ""
    align2 = ""
    i = rows - 1
    j = cols - 1
    while i > 0 or j > 0:
        if traceback_matrix[i][j] == (i-1, j-1):
            align1 = seq1[i-1] + align1
            align2 = seq2[j-1] + align2
            i -= 1
            j -= 1
        elif traceback_matrix[i][j] == (i-1, j):
            align1 = seq1[i-1] + align1
            align2 = "-" + align2
            i -= 1
        elif traceback_matrix[i][j] == (i, j-1):
            align1 = "-" + align1
            align2 = seq2[j-1] + align2
            j -= 1

    # Return the optimal alignment and the score
    return align1, align2, score_matrix[rows-1][cols-1]
seq1a = ''.join(random.choices('ATCG', k=4))
seq2a = ''.join(random.choices('ATCG', k=4))
print()
print(sequence_alignment(seq1a,seq2a))