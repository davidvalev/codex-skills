# Final QA checklist

## Brand and theme

- Brand name capitalization matches the user's input everywhere.
- Every URL uses the supplied canonical domain.
- No names, domains, company details, slogans, topics, or URLs leaked from a reference brand.
- Homepage, pricing, FAQ, chat, and chat persona describe the same product.
- Copy names specific discussion topics and useful outcomes from the supplied theme.
- No generic AI puffery or unsupported superiority claims remain.

## Claims and trust

- No fabricated testimonials, customer names, metrics, awards, certifications, partnerships, or security controls.
- Testimonial slots are clearly marked for customer-supplied material.
- Consequential themes include a precise informational boundary and escalation behavior.
- Privacy wording does not claim encryption, non-sharing, retention behavior, or regulatory compliance without verified implementation facts.

## Fixed structure

- Every page and section in `site-blueprint.md` is present and in the required order.
- The homepage has exactly four benefit items and three testimonial slots.
- Pricing has exactly three non-numeric package tiers plus pay as you go.
- FAQ covers exactly ten required question intents.
- Legal policy bodies are absent.
- Token quantities, prices, rates, discounts, free allocations, and expiry are absent.

## Copy consistency

- CTA labels point to the intended page.
- Feature names, package names, tagline, and chat role are consistent.
- UI states cover empty, loading, validation, retry, failure, and success where the blueprint requires them.
- SEO titles and descriptions are distinct, readable, and mapped to the canonical page URLs.
- Transactional messages do not invent order values, response times, or company details.

## Visual system

- Primary, mark-only, dark, light, and favicon SVGs open correctly.
- Logo spelling is exact and is not baked into generated raster art.
- Logo mark remains recognizable at 16 px.
- Four feature icons share stroke, corner, optical-size, and color rules.
- Hero, three package images, and social image exist as both PNG and WebP.
- Raster artwork contains no stray words, letters, numbers, currency symbols, watermarks, or third-party marks.
- Package images read as one family but are not duplicates.
- Palette contrast has been checked for text, controls, focus states, and hero copy.
- Typeface source, license, language support, weights, and fallbacks are recorded.

## Files and brandbook

- `manifest.json` parses and lists every final file with relative paths.
- No final file points to a temporary or machine-specific absolute path.
- `scripts/validate_package.py` exits successfully.
- Every brandbook PDF page was rendered and visually inspected after the final edit.
- The PDF has no clipped text, overlap, missing imagery, stretched logos, broken glyphs, weak contrast, or accidental blank pages.
- `qa-report.md` distinguishes passed checks, corrected issues, external inputs, and remaining limitations.
