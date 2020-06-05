# -*- coding: utf-8 -*-

from .serializer import Serializer

from .dom import addClass, addOldIDs, appendChild, appendContents, approximateLineNumber, childElements, childNodes, circledDigits, clearContents, closestAncestor, closestAttr, createElement, dedupIDs, E, emptyText, escapeAttr, escapeCSSIdent, escapeHTML, escapeUrlFrag, filterAncestors, find, findAll, fixSurroundingTypography, fixTypography, fixupIDs, foldWhitespace, hasAncestor, hasAttrs, hasChildElements, hasClass, hashContents, hasOnlyChild, headingLevelOfElement, innerHTML, insertAfter, insertBefore, isElement, isEmpty, isNormative, isOddNode, moveContents, nodeIter, outerHTML, parentElement, parseDocument, parseHTML, prependChild, previousElements, relevantHeadings, removeAttr, removeClass, removeNode, replaceAwkwardCSSShorthands, replaceContents, replaceMacros, replaceNode, safeID, scopingElements, sectionName, serializeTag, textContent, textContentIgnoringDecorative, treeAttr, unescape, unfixTypography, wrapContents