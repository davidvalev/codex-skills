---
name: create-token-chat-brand
description: Create a complete brand, fixed-site copy set, chat persona, logo system, web imagery, and PDF brandbook for a themed token-funded AI chat site. Use when the user supplies a brand name, domain, and theme and wants a production-ready creative package, not website implementation, legal policies, or token pricing.
---

# Create a token chat brand

Create one coherent, implementation-ready package for a themed AI chat business. Preserve the fixed sitemap and content slots in [references/site-blueprint.md](references/site-blueprint.md). Do not build the website unless the user separately asks for implementation.

## Required inputs

Require these before generating deliverables:

- exact brand name
- exact domain
- theme prompt describing what users will discuss with the chat

A minimal invocation can be:

```text
Use $create-token-chat-brand.
Brand name: Exact Name
Domain: https://brand.example
Theme: A chat where users discuss ...
```

Read [references/briefing.md](references/briefing.md) before interviewing the user. Ask one compact round of theme questions only when the prompt leaves decisions that would materially change the audience, voice, visual direction, chat role, or safety boundaries. Do not ask about token prices, token quantities, exchange rates, free allowances, expiry, legal entities, or policy jurisdiction.

## Scope boundaries

- Keep the same sitemap and section structure for every brand. Tailor the words and art, not the information architecture.
- Create all public marketing copy, product UI copy, chat persona material, SEO metadata, and transactional messages named in the blueprint.
- Keep the pricing page and three package-card slots, but do not invent or encode token economics. Use non-numeric tier names and generic purchase copy.
- Do not draft privacy, refund, terms, cookie, or other legal-policy pages. Generate only the footer link labels and neutral consent-control labels required by the shared shell.
- Do not invent company-registration data, addresses, payment-provider relationships, certifications, security controls, customer counts, results, or customer testimonials.
- Do not generate Visa, Mastercard, or other third-party marks. List them as implementation-supplied assets when relevant.
- Treat themes involving health, finance, law, mental health, safety, or other consequential decisions as informational products. Define clear chat boundaries and avoid claims that the assistant replaces a qualified professional.

## Workflow

1. Confirm the required inputs and complete the theme interview when needed.
2. Write `assumptions.md` before creative production. Separate user-provided facts, creative decisions, and facts that still require implementation input.
3. Establish one creative direction: audience, positioning, promise, tagline, personality, voice, palette, typography, imagery, and prohibited motifs. Do not present several unfinished directions unless the user asks for options.
4. Create the site and product copy against the fixed blueprint. Use one canonical fact sheet for recurring names, taglines, feature terms, package names, and chat behavior.
5. Create the logo and imagery according to [references/visual-system.md](references/visual-system.md). Use editable SVG for the logo and icons. Use an image-generation tool for raster art when available, then preserve both PNG source files and optimized WebP versions.
6. Create the brandbook from [assets/brandbook-template.md](assets/brandbook-template.md). Keep the filled Markdown source and generate a polished PDF. Render every PDF page to images and inspect the result before delivery.
7. Assemble the package exactly as described in [references/output-contract.md](references/output-contract.md).
8. Run `scripts/validate_package.py <package-dir>`. Fix all errors, then complete the human review in [references/qa-checklist.md](references/qa-checklist.md).

## Content rules

- Write for the supplied theme and audience. A sentence that could be pasted unchanged into any AI-chat site is too generic.
- Explain what the chat can discuss, what a useful question looks like, and what users receive in return.
- Keep token language qualitative. It is acceptable to say that messages use tokens or that users can buy more. Do not state quantities, rates, prices, discounts, expiry, or free allowances.
- Keep the chat persona and public claims aligned. If the site promises a capability, the persona must support it. If the persona refuses a task, the marketing copy must not promise it.
- Provide three testimonial slots and the surrounding section copy, but label the quote fields as customer-supplied. Never fabricate endorsements.
- Use plain language, specific verbs, and varied sentence rhythm. Remove generic AI phrases, inflated claims, forced three-part lists, and unsupported superlatives.
- Use the exact brand spelling and canonical domain everywhere. Never reuse names, URLs, company details, or topic language from a reference site.

## Visual rules

- Generate mark-only visual concepts if exploration helps. Add the exact brand name later in editable SVG so spelling is deterministic.
- Keep text, prices, token quantities, currency symbols, logos, and watermarks out of generated raster images.
- Make all three package illustrations part of one family while giving each a distinct composition.
- Check palette contrast for normal text, large text, controls, focus states, and text placed over the hero image.
- Do not choose typefaces without recording their source and web-use license in `brand/typography.md`.

## Completion standard

Do not finish with prompts, concepts, or a partial copy deck. Deliver the filled source files, final SVG assets, PNG and WebP imagery, PDF brandbook, manifest, and QA report. State any intentionally unfilled implementation values, especially commerce configuration and legal URLs, in `assumptions.md` and `qa-report.md` without creating fake replacements.
