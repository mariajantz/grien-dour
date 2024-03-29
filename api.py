'''
PLEASE READ:

THIS FILE WAS STOLEN FROM NLTK. ACCORDING TO THEIR LICENSE, I MUST TELL
YOU THAT IT IS NOT MY WORK. THIS IS ME TELLING YOU THAT IT IS NOT MY WORK.
-Seth Yoder
'''

# Natural Language Toolkit: Classifier Interface
#
# Copyright (C) 2001-2012 NLTK Project
# Author: Edward Loper <edloper@gradient.cis.upenn.edu>
#         Steven Bird <sb@csse.unimelb.edu.au> (minor additions)
# URL: <http://www.nltk.org/>
# For license information, see LICENSE.TXT

"""
Interfaces for labeling tokens with category labels (or "class labels").

``ClassifierI`` is a standard interface for "single-category
classification", in which the set of categories is known, the number
of categories is finite, and each text belongs to exactly one
category.

``MultiClassifierI`` is a standard interface for "multi-category
classification", which is like single-category classification except
that each text belongs to zero or more categories.
"""
from nltk.internals import overridden

##//////////////////////////////////////////////////////
#{ Classification Interfaces
##//////////////////////////////////////////////////////

class ClassifierI(object):
    """
    A processing interface for labeling tokens with a single category
    label (or "class").  Labels are typically strs or
    ints, but can be any immutable type.  The set of labels
    that the classifier chooses from must be fixed and finite.

    Subclasses must define:
      - ``labels()``
      - either ``classify()`` or ``batch_classify()`` (or both)

    Subclasses may define:
      - either ``prob_classify()`` or ``batch_prob_classify()`` (or both)
    """
    def labels(self):
        """
        :return: the list of category labels used by this classifier.
        :rtype: list of (immutable)
        """
        raise NotImplementedError()

    def classify(self, featureset):
        """
        :return: the most appropriate label for the given featureset.
        :rtype: label
        """
        if overridden(self.batch_classify):
            return self.batch_classify([featureset])[0]
        else:
            raise NotImplementedError()

    def prob_classify(self, featureset):
        """
        :return: a probability distribution over labels for the given
            featureset.
        :rtype: ProbDistI
        """
        if overridden(self.batch_prob_classify):
            return self.batch_prob_classify([featureset])[0]
        else:
            raise NotImplementedError()

    def batch_classify(self, featuresets):
        """
        Apply ``self.classify()`` to each element of ``featuresets``.  I.e.:

            return [self.classify(fs) for fs in featuresets]

        :rtype: list(label)
        """
        return [self.classify(fs) for fs in featuresets]

    def batch_prob_classify(self, featuresets):
        """
        Apply ``self.prob_classify()`` to each element of ``featuresets``.  I.e.:

            return [self.prob_classify(fs) for fs in featuresets]

        :rtype: list(ProbDistI)
        """
        return [self.prob_classify(fs) for fs in featuresets]


class MultiClassifierI(object):
    """
    A processing interface for labeling tokens with zero or more
    category labels (or "labels").  Labels are typically strs
    or ints, but can be any immutable type.  The set of labels
    that the multi-classifier chooses from must be fixed and finite.

    Subclasses must define:
      - ``labels()``
      - either ``classify()`` or ``batch_classify()`` (or both)

    Subclasses may define:
      - either ``prob_classify()`` or ``batch_prob_classify()`` (or both)
    """
    def labels(self):
        """
        :return: the list of category labels used by this classifier.
        :rtype: list of (immutable)
        """
        raise NotImplementedError()

    def classify(self, featureset):
        """
        :return: the most appropriate set of labels for the given featureset.
        :rtype: set(label)
        """
        if overridden(self.batch_classify):
            return self.batch_classify([featureset])[0]
        else:
            raise NotImplementedError()

    def prob_classify(self, featureset):
        """
        :return: a probability distribution over sets of labels for the
            given featureset.
        :rtype: ProbDistI
        """
        if overridden(self.batch_prob_classify):
            return self.batch_prob_classify([featureset])[0]
        else:
            raise NotImplementedError()

    def batch_classify(self, featuresets):
        """
        Apply ``self.classify()`` to each element of ``featuresets``.  I.e.:

            return [self.classify(fs) for fs in featuresets]

        :rtype: list(set(label))
        """
        return [self.classify(fs) for fs in featuresets]

    def batch_prob_classify(self, featuresets):
        """
        Apply ``self.prob_classify()`` to each element of ``featuresets``.  I.e.:

            return [self.prob_classify(fs) for fs in featuresets]

        :rtype: list(ProbDistI)
        """
        return [self.prob_classify(fs) for fs in featuresets]


# # [XX] IN PROGRESS:
# class SequenceClassifierI(object):
#     """
#     A processing interface for labeling sequences of tokens with a
#     single category label (or "class").  Labels are typically
#     strs or ints, but can be any immutable type.  The set
#     of labels that the classifier chooses from must be fixed and
#     finite.
#     """
#     def labels(self):
#         """
#         :return: the list of category labels used by this classifier.
#         :rtype: list of (immutable)
#         """
#         raise NotImplementedError()

#     def prob_classify(self, featureset):
#         """
#         Return a probability distribution over labels for the given
#         featureset.

#         If ``featureset`` is a list of featuresets, then return a
#         corresponding list containing the probability distribution
#         over labels for each of the given featuresets, where the
#         *i*\ th element of this list is the most appropriate label for
#         the *i*\ th element of ``featuresets``.
#         """
#         raise NotImplementedError()

#     def classify(self, featureset):
#         """
#         Return the most appropriate label for the given featureset.

#         If ``featureset`` is a list of featuresets, then return a
#         corresponding list containing the most appropriate label for
#         each of the given featuresets, where the *i*\ th element of
#         this list is the most appropriate label for the *i*\ th element
#         of ``featuresets``.
#         """
#         raise NotImplementedError()

