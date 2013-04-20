furry-nemesis
=============
TO DO:

-We need to find some way to put more weight on some of the features when they
are positive (instead of negative)... for example, bookend\_const should
not hold any weight when it is False. This does not go for all features.

-We need to take into account vowels/consonants that are NOT first or
last. Could make a new feature that is a set or list of
vowels/consonants. In the corresponding test function in rulewizard.py,
we could find the intersection between the vowel/consonant sets for all
the words to check that the feature is significant.

