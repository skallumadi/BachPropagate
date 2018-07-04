### Steps for training and testing and running on the challenge set

1. Get track background data from spotify, create necessary pkls
    1. for the whole dataset for challenge run: python build_bipartites_challenge.py
2. Create splits: 
    1. BG750 
    2. train 
    3. test
    4. challenge(provided) 
    5. telescoping
3. Generate pkl where necessary-> pkl for trackfeatures and details; pid track mapping; splits pkls; most popular tracks
4. clean the titles, *provide stop list *provide synonyms list, bigrams
5. create background index documents, script to generate docs; config file to create indexes. 3 indexes -> Meta1, Meta2 and PRFQE
    1. run python build_indri_index_challenge.py
6. create queries for these indexes for train, test and challenge
7. script to generate results for the queries
8. script to parse these results 2 different formats(BM25 vs QE)
9.  script to generate various metapaths and w2v models on BG 750 playlists;4 CBOW models ->a)just playlists, b)playlists and titles interspersed, c)AILA, d)ILI  
10. for each query playlist in splits, get 1000 items for the plalyist representation; batch generate and save
11. main track: generate training data [PRFQE+BM25-1+BM25-2 -> 2000 items]+trackfeatures+playlist features+track-playlistfeatures+w2v features
12. main track: generate test data(and challenge data)
13. param sweep script to find right lambda mart model [train, test and evaluate]
14. creative track: generate training data [PRFQE+BM25-1+BM25-2 -> 2000 items]+trackfeatures+playlist features+track-playlistfeatures+w2v features+track features from spotify api --> -missingzero
15. run built model on  challenge data
16. prepare submission(popular items when playlist size <500)
