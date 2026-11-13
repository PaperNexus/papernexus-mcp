---
name: check-references
description: Check a reference list or bibliography against Paper Nexus's records - is each reference a real paper, and are its title, year, first author and DOI right? Use to verify citations an assistant wrote, to catch made-up or garbled references, or to proofread a manuscript's, thesis's or .bib file's references before submission.
---

# Check references with Paper Nexus

`verify_references` looks up each reference and says which paper it is, and
where its title, year, first author and DOI differ from Paper Nexus's record.
It is the way to check references you or another assistant wrote from memory,
and to proofread a manuscript's list.

## Workflow

1. **Collect the references as written.** Take them from the message, the
   manuscript, or a `.bib`, `.ris` or reference-manager file. Don't tidy,
   complete or correct them first: the point is to check what is there. A
   formatted reference in any style, a DOI, an arXiv, PubMed or publisher
   link, or a bare title each work as a string. When you already have the
   parts (a BibTeX entry, say), pass an object `{title, authors, year, doi}`
   instead, which can't be misread.
2. **Call `verify_references`** with up to 50 at a time, in the order given.
   Each reference uses one lookup (100 a day on a free account, 1,000 on
   Premium), so for a long list call `get_usage` first, and say so when the
   list won't fit rather than checking part of it silently.
3. **Read each result by its `status`:**
   - `found`: the paper the reference names. Then look at `differences`
     (fields that differ from the record, as `given` and `paper`) and `notes`
     (differences that are usually no error: a year one apart, often a
     preprint and its published version, or a first author who is another of
     the paper's authors).
   - `conflict`: the reference's parts name different papers, the usual sign
     of a made-up or garbled reference. `identifier_title_differs` means its
     DOI or other identifier belongs to a paper with another title;
     `author_not_on_paper` means the title is a paper with none of the
     authors given. `title_matches`, when present, names the paper the title
     belongs to.
   - `not_found`: not in Paper Nexus. That is not proof it was made up: Paper
     Nexus holds papers with citation data, not every publication. Books,
     reports, web pages and very recent papers are often missing.
   - `not_checked`: nothing in it to look up, or the search ran out of time
     (`out_of_time`); check those again in a smaller batch.
4. **Check `read_as` when a result looks wrong.** Free-text references are
   read by pattern. If `read_as` shows the title or author misread, pass that
   reference again as fields before reporting it.
5. **Report, worst first.** Lead with the `summary` counts, then the
   conflicts, then the references not found, then those found with
   differences, each with the reference as given, what differs, and the
   paper's papernex.us `url`. List the references that are fine by count, not
   one by one, unless the user asks. Keep the user's numbering or citation
   keys so they can find each one.
6. **Offer the fix, don't apply it unasked.** For a reference with
   differences or a conflict, say what Paper Nexus records. If the user wants
   corrected entries, `export_citations` gives BibTeX, RIS or CSL-JSON for
   the matched papers; say that the citation keys will be Paper Nexus's, not
   theirs, and change a file only when asked.

## Don'ts

- Don't call a reference fabricated on `not_found` alone, or wrong on a
  difference alone. Paper Nexus's record can itself be wrong: a difference is
  a field to check at the publisher.
- Don't "repair" a conflicting reference by guessing which paper was meant.
  Show both candidates (`paper` and `title_matches`) and let the user choose.
- Don't replace a reference that wasn't found with a similar paper from
  `search_papers` without saying it is a different paper.
- Volume, issue and pages are not checked, and neither is whether the paper
  supports the claim it is cited for: Paper Nexus has metadata, not full
  text. Say so if the user asks for a full citation check.
- Don't fill in missing fields from memory. Use what the tools return.
