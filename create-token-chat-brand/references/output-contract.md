# Output contract

Create one folder named from the supplied domain or brand slug:

```text
<brand-slug>/
|-- README.md
|-- assumptions.md
|-- manifest.json
|-- qa-report.md
|-- brand/
|   |-- brand-strategy.md
|   |-- voice-and-messaging.md
|   |-- palette.json
|   |-- typography.md
|   |-- logo-primary.svg
|   |-- logo-mark.svg
|   |-- logo-mono-dark.svg
|   |-- logo-mono-light.svg
|   `-- favicon.svg
|-- content/
|   |-- site-copy.md
|   |-- ui-copy.md
|   |-- chat-persona.md
|   |-- transactional-emails.md
|   `-- seo-metadata.csv
|-- images/
|   |-- hero.png
|   |-- hero.webp
|   |-- feature-01.svg
|   |-- feature-02.svg
|   |-- feature-03.svg
|   |-- feature-04.svg
|   |-- token-pack-01.png
|   |-- token-pack-01.webp
|   |-- token-pack-02.png
|   |-- token-pack-02.webp
|   |-- token-pack-03.png
|   |-- token-pack-03.webp
|   |-- social-share.png
|   |-- social-share.webp
|   `-- generation-prompts.md
`-- brandbook/
    |-- brandbook.md
    `-- brandbook.pdf
```

## File responsibilities

`README.md` explains the package, where each deliverable belongs, and which values the implementation team must still supply.

`assumptions.md` has three sections: user-provided facts, creative decisions, and implementation-supplied facts. Token economics, legal URLs, company details, payment details, and verified testimonials belong in the last section.

`manifest.json` is the machine-readable index. Include:

```json
{
  "brand_name": "Exact supplied name",
  "domain": "https://canonical.example",
  "theme_summary": "One sentence",
  "language": "en",
  "generated_at": "ISO-8601 timestamp",
  "forbidden_terms": [],
  "files": [
    {"path": "brand/logo-primary.svg", "type": "logo", "purpose": "Header and footer"}
  ]
}
```

List every final deliverable in `files`. Use repository-relative paths only. Put names and domains from any creative reference sites in `forbidden_terms`; use an empty array when no outside reference was used.

`brand/brand-strategy.md` contains audience, positioning, promise, differentiators, personality, tagline, message hierarchy, and prohibited claims.

`brand/voice-and-messaging.md` contains voice principles, vocabulary, words to avoid, headline style, CTA style, response examples, and before/after examples.

`content/site-copy.md` follows the public page order from the blueprint. `content/ui-copy.md` covers authentication, account, cart, checkout, contact, cookie controls, and error states.

`content/seo-metadata.csv` uses columns `path,title,meta_description,og_title,og_description,canonical_url,robots` and contains one row for every fixed page. Mark account, authentication, cart, and checkout pages `noindex,follow` unless the implementation requires another rule.

`images/generation-prompts.md` records the final prompt used for every generated raster asset, including any targeted revision prompts.

`qa-report.md` records the checks performed, failures corrected, intentionally external values, and remaining limitations. Do not mark an unperformed check as passed.

## Editable and optimized formats

- SVG is the editable source for logos, favicon, and icons.
- PNG is the retained source for generated raster artwork.
- WebP is the optimized website derivative.
- Markdown is the editable source for the brandbook.
- PDF is the reviewed presentation copy.

Do not leave final assets only in an image generator's default storage, a temporary directory, or an absolute local path.
