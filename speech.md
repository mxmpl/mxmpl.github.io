---
layout: perso
title: Speech Processing
---

# Vocal Tract Length Normalization

Extraction of speech features from raw audio is the first step for any speech related application. Some speaker normalization techniques exist to reduce the sensibility of extracted features to speaker, thus focusing on speech content. Among them, vocal tract length normalization (VTLN) aims to compensate for the fact that speakers have vocal tracts of different sizes. 

This technique computes a learned factor for each speaker that is used to warp the frequency-axis of the spectra. The pipeline has the following steps : extract MFCC, extract VAD, train UBM model, train VTLN model, extract warp factor from trained VTLN model. 

More coming soon
