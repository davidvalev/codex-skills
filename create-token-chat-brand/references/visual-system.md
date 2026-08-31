# Visual system and asset production

## Required assets

Logo system:

- `logo-primary.svg`: horizontal mark and exact wordmark
- `logo-mark.svg`: square mark without the wordmark
- `logo-mono-dark.svg`: one-color dark variant
- `logo-mono-light.svg`: one-color light variant
- `favicon.svg`: simplified mark that remains legible at 16 px

Interface icons:

- exactly four feature icons as editable SVG

Raster artwork, each supplied as PNG source and optimized WebP:

- `hero`: wide homepage artwork, target 1920 x 900, with deliberate negative space for copy
- `token-pack-01`, `token-pack-02`, `token-pack-03`: square package-card artwork, target 1024 x 1024
- `social-share`: social preview, target 1200 x 630

Do not generate payment-network marks or other third-party trademarks.

## Logo workflow

1. Translate the theme into a simple symbol idea that works without the wordmark.
2. If raster exploration is useful, generate mark-only concepts with no letters or words.
3. Select one concept and recreate it as clean editable SVG using simple paths and shapes.
4. Add the exact brand name as deterministic SVG text. Record the selected typeface and fallback stack.
5. Produce horizontal, mark-only, dark, light, and favicon variants.
6. Inspect at 16, 32, 128, and 512 px. Remove detail that collapses at small sizes.

Do not trace a known logo, use stock-logo shapes without adaptation, or depend on text generated inside a raster image.

## Raster workflow

Use a dedicated image-generation tool when available. Make one call per distinct asset or variant. Use the same art direction, palette, lighting, and material language across the set.

Every prompt must name:

- the website slot and aspect ratio
- the theme-specific subject
- the selected visual medium
- composition and negative-space requirements
- palette
- required continuity with the other assets
- prohibited content

Always prohibit text, letters, numbers, prices, currency symbols, brand marks, UI screenshots, signatures, and watermarks. Inspect the generated image before saving it. Correct subject errors, stray lettering, anatomy problems, visible trademarks, and inconsistent style.

Preserve the selected PNG source. Create a WebP derivative for the website. Do not overwrite earlier selected work during iteration; use versioned names until the final selection is made.

## Palette

Create a role-based palette in `brand/palette.json` with:

- primary
- secondary
- accent
- background
- surface
- text
- muted_text
- border
- success
- warning
- error
- focus
- hero_overlay
- contrast_pairs

Store each color as a hex value and record its intended use. Test normal text, large text, controls, focus indicators, and hero overlays for accessible contrast. If a brand accent cannot carry white or dark text, state the safe pairing instead of forcing it.

## Typography

Choose one display family and one body/UI family, or one variable family that handles both. Record source, license, weights, fallbacks, and use. Avoid a font simply because it appears fashionable. It must support the requested language and the final brand tone.

## Brandbook PDF

Use the editable Markdown template as the source. Create a visually designed PDF, not a plain text dump. Include real logo variants, palette swatches, typography samples, image examples, icon examples, UI component examples, and do/don't comparisons.

Render all PDF pages to images after generation. Inspect for clipped text, broken glyphs, weak contrast, missing images, stretched logos, poor page breaks, inconsistent margins, and unreadable small type. Regenerate until the latest render has no visible defects.
