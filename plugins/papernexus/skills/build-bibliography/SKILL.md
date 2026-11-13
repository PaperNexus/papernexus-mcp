---
name: build-bibliography
description: Turn papers into citations for a reference manager or a manuscript - BibTeX, RIS (Zotero, Mendeley, EndNote) or CSL-JSON (pandoc, citeproc) - with the Paper Nexus tools. Use when the user asks for a .bib file, BibTeX entries, an RIS export, or a bibliography for papers named by title, DOI, arXiv id, or found earlier in the conversation.
---

# Build a bibliography with Paper Nexus

`export_citations` writes citations from Paper Nexus's records, the same
entries the Paper Nexus site exports. Use it instead of writing BibTeX from
memory: entries written from memory are where wrong years, authors and DOIs
come from.

## Workflow

1. **Name the papers.** `export_citations` takes Paper Nexus ids or links,
   DOIs, arXiv ids, PMIDs, PMCIDs and OpenAlex ids directly, so papers with
   an identifier, and papers a tool returned earlier in the conversation,
   need no search. For papers known only by title, call `search_papers` with
   all of them as `queries` (up to 20 per call) and pick the result whose
   title, year and authors match; when `closest_matches` is true or two
   results could be the one, ask rather than guess. For a collection in the
   user's library, `list_library` gives the ids (when library access was
   allowed).
2. **Choose the format.** `bibtex` (the default) for LaTeX, `ris` for
   Zotero, Mendeley or EndNote, `csl-json` for pandoc or citeproc. Ask only
   when the user's setup doesn't make it clear.
3. **Call `export_citations`** with up to 50 papers per call, in the order
   the user wants them. Each paper uses one lookup, not the allowance.
4. **Deliver `content` whole.** Write it to the file the user named, or show
   it in one code block. Don't retype or reformat entries: copy them as
   returned. With several calls, join the contents in order (for `csl-json`,
   merge the arrays into one).
5. **Say what to check.** Report:
   - `not_found`: papers Paper Nexus doesn't have, left out of the file. Name
     each one; don't write an entry for it yourself.
   - `authors_may_be_cut`: Paper Nexus keeps the first five authors of a
     paper, so these entries may be missing later authors. The user should
     complete them at the publisher before submitting.
   - The citation keys (`entries[].citation_key`) are Paper Nexus ids, with a
     `P` in front when one starts with a digit. Give the key beside each
     title so the user can cite them, and rename keys only if asked.

## Don'ts

- Don't add fields Paper Nexus didn't return (abstract, pages, month,
  publisher), and don't correct an entry from memory. Say what looks missing
  instead.
- Don't merge the export into an existing `.bib` file by overwriting it.
  Append, and point out entries that look like duplicates of ones already
  there (same DOI or title) rather than deleting either.
- An entry here is Paper Nexus's record, which can be wrong. For a
  manuscript, tell the user to check the entries before submitting.
- To check references the user already has, rather than make new ones, use
  `verify_references` (the check-references skill).
